
#!/usr/bin/env python3
"""Translate BOSAL DELFOR D97A EDIFACT streams into SAP DELFOR01 IDoc files.

The implementation follows the mapping logic defined in
`mapping_delfor_d97a_bosal.delfor01_sap6xx_btc.txt` and uses the structural
constraints from `forms_out_delfor01_sap46x_btc.txt`.  Only the artefacts
provided with this project (forms, mappings, partner/modification tables,
samples) are referenced.  External defaults such as ports or archival keys are
exposed via the JSON configuration file to remain auditable.
"""

from __future__ import annotations

import argparse
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

__version__ = "v1.0.0"


# --------------------------------------------------------------------------- #
# EDIFACT parsing utilities (cf. forms_in_delfor_d97a_bosal.txt header sec.)  #
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class EDIFACTSeparators:
    segment: str = "'"
    data: str = "+"
    component: str = ":"
    release: str = "?"
    decimal: str = "."
    reserved: str = " "


@dataclass
class Segment:
    tag: str
    elements: List[List[str]]


def parse_edifact(payload: str) -> Tuple[List[Segment], EDIFACTSeparators]:
    """Split an EDIFACT interchange into ordered segments."""
    separators = EDIFACTSeparators()
    cursor = 0
    segments: List[str] = []

    if payload.startswith("UNA"):
        if len(payload) < 9:
            raise ValueError("Malformed UNA segment; too short to define separators.")
        separators = EDIFACTSeparators(
            component=payload[3],
            data=payload[4],
            decimal=payload[5],
            release=payload[6],
            reserved=payload[7],
            segment=payload[8],
        )
        cursor = 9
        while cursor < len(payload) and payload[cursor] in {"\r", "\n"}:
            cursor += 1

    raw_stream = payload[cursor:]
    current: List[str] = []
    i = 0
    while i < len(raw_stream):
        char = raw_stream[i]
        if char == separators.release:
            i += 1
            if i < len(raw_stream):
                current.append(raw_stream[i])
        elif char == separators.segment:
            segment_text = "".join(current).strip()
            if segment_text:
                segments.append(segment_text)
            current = []
        else:
            current.append(char)
        i += 1

    parsed_segments: List[Segment] = []
    for raw_segment in segments:
        parts = split_with_empty(raw_segment, separators.data)
        tag = parts[0]
        element_values: List[List[str]] = []
        for element in parts[1:]:
            element_values.append(split_with_empty(element, separators.component))
        parsed_segments.append(Segment(tag=tag, elements=element_values))

    return parsed_segments, separators


def split_with_empty(value: str, sep: str) -> List[str]:
    if value == "":
        return [""]
    tokens: List[str] = []
    accumulator: List[str] = []
    for char in value:
        if char == sep:
            tokens.append("".join(accumulator))
            accumulator = []
        else:
            accumulator.append(char)
    tokens.append("".join(accumulator))
    return tokens


# --------------------------------------------------------------------------- #
# Configuration and auxiliary data loading (cf. AGENTS.md §7)                #
# --------------------------------------------------------------------------- #


@dataclass
class MappingConfig:
    partner: str
    system_client: str
    mandt: str
    sndpor: str
    sndprt: str
    sndpfc: str
    sndprn: str
    sndsad: str
    sndlad: str
    rcvpor: str
    rcvprt: str
    rcvpfc: str
    rcvprn: str
    rcvsad: str
    rcvlad: str
    docrel: str
    direct: str
    outmod: str
    exprss: str
    test_indicator: str
    cimtyp: str
    mestyp: str
    std: str
    stdvrs: str
    stdmes: str
    archiv_key: str
    partner_table: Path
    modifications_table: Path
    forms_out: Path
    force_sysdate_from_docdate: bool = True
    force_systime_from_unb: bool = False
    override_credat: Optional[str] = None
    override_cretim: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, object]) -> "MappingConfig":
        required_keys = [
            "partner",
            "system_client",
            "mandt",
            "sndpor",
            "sndprt",
            "sndpfc",
            "sndprn",
            "sndsad",
            "sndlad",
            "rcvpor",
            "rcvprt",
            "rcvpfc",
            "rcvprn",
            "rcvsad",
            "rcvlad",
            "docrel",
            "direct",
            "outmod",
            "exprss",
            "test_indicator",
            "cimtyp",
            "mestyp",
            "std",
            "stdvrs",
            "stdmes",
            "archiv_key",
            "partner_table",
            "modifications_table",
            "forms_out",
        ]
        missing = [key for key in required_keys if key not in data]
        if missing:
            raise KeyError(f"Missing configuration keys: {', '.join(missing)}")

        return cls(
            partner=str(data["partner"]),
            system_client=str(data["system_client"]),
            mandt=str(data["mandt"]),
            sndpor=str(data["sndpor"]),
            sndprt=str(data["sndprt"]),
            sndpfc=str(data["sndpfc"]),
            sndprn=str(data["sndprn"]),
            sndsad=str(data["sndsad"]),
            sndlad=str(data["sndlad"]),
            rcvpor=str(data["rcvpor"]),
            rcvprt=str(data["rcvprt"]),
            rcvpfc=str(data["rcvpfc"]),
            rcvprn=str(data["rcvprn"]),
            rcvsad=str(data["rcvsad"]),
            rcvlad=str(data["rcvlad"]),
            docrel=str(data["docrel"]),
            direct=str(data["direct"]),
            outmod=str(data["outmod"]),
            exprss=str(data["exprss"]),
            test_indicator=str(data["test_indicator"]),
            cimtyp=str(data["cimtyp"]),
            mestyp=str(data["mestyp"]),
            std=str(data["std"]),
            stdvrs=str(data["stdvrs"]),
            stdmes=str(data["stdmes"]),
            archiv_key=str(data["archiv_key"]),
            partner_table=Path(data["partner_table"]),
            modifications_table=Path(data["modifications_table"]),
            forms_out=Path(data["forms_out"]),
            force_sysdate_from_docdate=bool(data.get("force_sysdate_from_docdate", True)),
            force_systime_from_unb=bool(data.get("force_systime_from_unb", False)),
            override_credat=(str(data["override_credat"]) if data.get("override_credat") else None),
            override_cretim=(str(data["override_cretim"]) if data.get("override_cretim") else None),
        )

def default_config(base_path: Path) -> Dict[str, object]:
    """Provide project defaults derived from provided artefacts."""
    artifacts_root = base_path / "artifacts"
    return {
        "partner": "BOSAL",
        "system_client": "SAPP49_110",
        "mandt": "110",
        "sndpor": "A000000002",
        "sndprt": "KU",
        "sndpfc": "AG",
        "sndprn": "",
        "sndsad": "",
        "sndlad": "",
        "rcvpor": "SAPP49",
        "rcvprt": "LS",
        "rcvpfc": "",
        "rcvprn": "",
        "rcvsad": "",
        "rcvlad": "",
        "docrel": "46B",
        "direct": "2",
        "outmod": " ",
        "exprss": " ",
        "test_indicator": " ",
        "cimtyp": "CONN0000",
        "mestyp": "DELINS",
        "std": " ",
        "stdvrs": "      ",
        "stdmes": "DELINS",
        "archiv_key": "",
        "partner_table": str(artifacts_root / "mapping_tables" / "mapping_table_partner_SAPP49_110.txt"),
        "modifications_table": str(
            artifacts_root / "mapping_tables" / "mapping_table_modifications_BOSAL_SAPP49_110.txt"
        ),
        "forms_out": str(artifacts_root / "forms" / "forms_out_delfor01_sap46x_btc.txt"),
    }


def load_config(base_path: Path, config_path: Optional[Path]) -> MappingConfig:
    """Merge defaults with optional user supplied overrides."""
    config_data = default_config(base_path)
    if config_path:
        with config_path.open("r", encoding="utf-8") as handle:
            user_data = json.load(handle)
        config_data.update(user_data)
    return MappingConfig.from_dict(config_data)


def load_table(table_path: Path) -> Dict[str, str]:
    """Parse partner/modification tables (key=value per line)."""
    if not table_path.exists():
        raise FileNotFoundError(f"Mapping table not found: {table_path}")

    entries: Dict[str, str] = {}
    with table_path.open("r", encoding="latin-1") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line or line.startswith("#") or line.startswith("##") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            entries[key.strip()] = value.strip()
    if not entries:
        raise ValueError(f"Mapping table {table_path} has no usable entries.")
    return entries


# --------------------------------------------------------------------------- #
# IDoc segment metadata loader (cf. forms_out_delfor01_sap46x_btc.txt)       #
# --------------------------------------------------------------------------- #


@dataclass
class FieldDefinition:
    length: int
    default: str = ""


@dataclass
class SegmentDefinition:
    name: str
    fields: List[str]


def load_segment_metadata(forms_path: Path, segment_names: Sequence[str]) -> Tuple[Dict[str, SegmentDefinition], Dict[str, FieldDefinition]]:
    """Extract field order and lengths for the required IDoc segments."""
    if not forms_path.exists():
        raise FileNotFoundError(f"Forms description not found: {forms_path}")

    raw_lines = forms_path.read_text(encoding="latin-1").splitlines()
    field_defs: Dict[str, FieldDefinition] = {}

    for line in raw_lines:
        stripped = line.strip()
        if ":" not in stripped:
            continue
        head, tail = stripped.split(":", 1)
        if "{" not in tail or "}" not in tail:
            continue
        body = tail.split("{", 1)[1].split("}", 1)[0]
        if "LENGTH" not in body:
            continue
        length_token = body.split("LENGTH", 1)[1].split("=", 1)[1].split(",", 1)[0].strip()
        length = int(length_token)
        default = ""
        if "DEFAULT" in body:
            default_part = body.split("DEFAULT", 1)[1].split("=", 1)[1].strip()
            if default_part.startswith('"'):
                default = default_part.strip('" ')
        field_defs[head.strip()] = FieldDefinition(length=length, default=default)

    segment_defs: Dict[str, SegmentDefinition] = {}
    for segment_name in segment_names:
        collecting = False
        fields: List[str] = []
        for line in raw_lines:
            stripped = line.strip()
            if not collecting:
                if stripped.startswith(segment_name) and "{" in stripped:
                    collecting = True
                continue
            if stripped.startswith("#"):
                continue
            if stripped == ";":
                break
            without_comment = line.split("#", 1)[0].strip()
            if not without_comment or without_comment.startswith("REST"):
                continue
            token = without_comment.rstrip(";").strip()
            if not token:
                continue
            field_name = token.split()[0].rstrip(":")
            fields.append(field_name)
        prefix = f"{segment_name}_"
        deduped: List[str] = []
        seen: set[str] = set()
        for field in fields:
            if not (field == segment_name or field.startswith(prefix)):
                continue
            if field in field_defs and field not in seen:
                seen.add(field)
                deduped.append(field)
        fields = deduped
        if not fields:
            raise ValueError(f"No field definitions found for segment {segment_name}")
        segment_defs[segment_name] = SegmentDefinition(name=segment_name, fields=fields)

    return segment_defs, field_defs

# --------------------------------------------------------------------------- #
# Mapping state models (cf. mapping_delfor_d97a_bosal... lines 100+)          #
# --------------------------------------------------------------------------- #


@dataclass
class PartyInfo:
    number: str = ""
    name: str = ""


@dataclass
class HeaderReferences:
    order_number: str = ""
    release_number_new: str = ""
    release_number_old: str = ""


@dataclass
class ScheduleLine:
    quantity: Decimal
    unit: str
    ettyp: str = ""
    prgrs: str = ""
    start_date: str = ""
    end_date: str = ""
    time: str = "0000"


@dataclass
class LineItem:
    line_id: str
    customer_item: str = ""
    unit: str = ""
    mapped_unit: str = ""
    plant: str = ""
    unloading_point: str = ""
    consumption_point: str = ""
    cumulative_qty: Optional[Decimal] = None
    last_delivery_qty: Optional[Decimal] = None
    last_delivery_note: str = ""
    last_delivery_date: str = ""
    labky: str = ""
    abrab: str = ""
    abrbi: str = ""
    schedules: List[ScheduleLine] = field(default_factory=list)
    design_revision: str = ""


@dataclass
class MappingState:
    separators: EDIFACTSeparators
    config: MappingConfig
    partner_table: Dict[str, str]
    modifications_table: Dict[str, str]
    header_docdate: str = "00000000"
    header_startdate: str = "00000000"
    header_enddate: str = "00000000"
    header_refs: HeaderReferences = field(default_factory=HeaderReferences)
    message_ref: str = ""
    supplier: PartyInfo = field(default_factory=PartyInfo)
    buyer: PartyInfo = field(default_factory=PartyInfo)
    ship_to: PartyInfo = field(default_factory=PartyInfo)
    labky: str = ""
    filedate: str = ""
    filetime: str = ""
    lines: List[LineItem] = field(default_factory=list)
    current_line: Optional[LineItem] = None
    pending_schedule: Optional[ScheduleLine] = None
    schedule_context: Optional[Tuple[str, str]] = None
    last_rff_qualifier: Optional[str] = None
    debitor: str = ""
    rcvprn: Optional[str] = None


# --------------------------------------------------------------------------- #
# Core mapping helpers (direct traces to mapping file line comments).         #
# --------------------------------------------------------------------------- #


NUMERIC_FIELDS = {
    "E2EDP10_AKUEM",
    "E2EDP10_LFIMG",
    "E2EDP10_MFRFZ",
    "E2EDP10_MFADT",
    "E2EDP10_ABMDE",
    "E2EDP10_ABFDE",
    "E2EDP10_AKUBM",
    "E2EDP10_FZDIF",
    "E2EDP16_WMENG",
    "E2EDP16_FZABR",
}


def normalise_date(value: str) -> str:
    cleaned = "".join(ch for ch in value if ch.isdigit())
    if len(cleaned) < 8:
        return cleaned.ljust(8, "0")
    return cleaned[:8]


def format_quantity(raw: Decimal) -> str:
    quantised = raw.normalize()
    if quantised == quantised.to_integral():
        return str(int(quantised))
    return format(quantised, "f").rstrip("0").rstrip(".")


def date_add(base: str, days: int) -> str:
    dt = datetime.strptime(base, "%Y%m%d")
    return (dt + timedelta(days=days)).strftime("%Y%m%d")


def date_sub(base: str, days: int) -> str:
    dt = datetime.strptime(base, "%Y%m%d")
    return (dt - timedelta(days=days)).strftime("%Y%m%d")


def min_date(values: Iterable[str]) -> str:
    filtered = [v for v in values if v and v != "00000000"]
    if not filtered:
        return "00000000"
    return min(filtered)


def max_date(values: Iterable[str]) -> str:
    filtered = [v for v in values if v and v != "00000000"]
    if not filtered:
        return "00000000"
    return max(filtered)


def extract_component(elements: List[List[str]], element_index: int, component_index: int = 0) -> str:
    if element_index >= len(elements):
        return ""
    element = elements[element_index]
    if component_index >= len(element):
        return ""
    return element[component_index]


def extract_party_name(elements: List[List[str]]) -> str:
    for idx in (2, 3, 4, 5):
        name = extract_component(elements, idx, 0)
        if name:
            return name
    return ""


def resolve_unit(state: MappingState, raw_unit: str) -> str:
    if not raw_unit:
        return raw_unit
    if not state.ship_to.number:
        raise ValueError("Cannot resolve unit without ship-to number (NAD+ST missing).")
    key = f"EDI6411-E-{state.ship_to.number}-{raw_unit}"
    mapped = state.modifications_table.get(key)
    if not mapped:
        raise KeyError(f"Missing unit mapping for {key} in modifications table.")
    return mapped


def resolve_rcvprn(state: MappingState) -> str:
    if state.rcvprn:
        return state.rcvprn
    supplier_num = state.supplier.number
    key = f"RCVPRN-E-{supplier_num}"
    mapped = state.modifications_table.get(key)
    if mapped:
        state.rcvprn = mapped
        return mapped
    if state.config.rcvprn:
        state.rcvprn = state.config.rcvprn
        return state.rcvprn
    raise KeyError(f"No receiver partner override found for {supplier_num}; expected entry {key}.")


def resolve_debitor(state: MappingState, line: LineItem) -> str:
    if state.debitor:
        return state.debitor
    base_key = f"DELFOR-D97A-{state.config.partner}-{state.supplier.number}-{state.buyer.number}-{state.ship_to.number}"
    candidate = state.partner_table.get(base_key)
    if not candidate and line.unloading_point:
        candidate = state.partner_table.get(f"{base_key}-{line.unloading_point}")
    if not candidate:
        if state.config.sndprn:
            state.debitor = state.config.sndprn
            return state.debitor
        raise KeyError(
            f"Missing debitor mapping for {base_key} (and -{line.unloading_point}). "
            "Update partner table or provide sndprn override."
        )
    state.debitor = candidate[:10]
    return state.debitor


def start_new_line(state: MappingState, line_id: str, customer_item: str) -> None:
    if state.current_line:
        finalise_current_line(state)
    abrab_origin = state.header_startdate if state.header_startdate != "00000000" else state.header_docdate
    state.current_line = LineItem(
        line_id=line_id,
        customer_item=customer_item,
        abrab=abrab_origin,
        labky=state.labky,
    )


def finalise_current_line(state: MappingState) -> None:
    if not state.current_line:
        return
    line = state.current_line
    if line.unit and not line.mapped_unit:
        line.mapped_unit = resolve_unit(state, line.unit)
    if line.cumulative_qty is not None and not line.mapped_unit:
        line.mapped_unit = resolve_unit(state, line.unit or state.current_line.mapped_unit)
    schedule_end = max_date(schedule.end_date for schedule in line.schedules)
    line.abrbi = max_date(
        value for value in (state.header_enddate, schedule_end, line.abrab) if value and value != "00000000"
    )
    if not line.abrbi:
        line.abrbi = line.abrab
    if line.mapped_unit:
        line.unit = line.mapped_unit
    state.lines.append(line)
    state.current_line = None


def append_schedule(state: MappingState, schedule: ScheduleLine) -> None:
    line = state.current_line
    if not line:
        raise ValueError("Schedule encountered without active line.")
    line.schedules.append(schedule)
    if not line.mapped_unit and schedule.unit:
        line.mapped_unit = schedule.unit
    line.abrab = min_date([line.abrab, schedule.start_date, state.header_startdate])
    if not line.last_delivery_date:
        line.last_delivery_date = ""


def compute_schedule_dates(
    state: MappingState,
    schedule: ScheduleLine,
    context: Tuple[str, str],
    dtm_qualifier: str,
    raw_value: str,
    format_code: str,
) -> ScheduleLine:
    classification, frequency = context
    date_value = normalise_date(raw_value)
    time_value = "0000" if format_code == "102" else (raw_value[8:12] if len(raw_value) >= 12 else "0000")

    if dtm_qualifier in {"2", "10"}:
        schedule.start_date = date_value
        schedule.end_date = (
            date_add(date_value, 6)
            if frequency == "W"
            else date_add(date_value, 27)
            if frequency == "F"
            else date_value
        )
        schedule.time = time_value
    elif dtm_qualifier == "158":
        schedule.start_date = date_value
        if not schedule.end_date or schedule.end_date == "00000000":
            schedule.end_date = (
                date_add(date_value, 6)
                if frequency == "W"
                else date_add(date_value, 27)
                if frequency == "F"
                else date_value
            )
    elif dtm_qualifier == "159":
        schedule.end_date = date_value
        if not schedule.start_date or schedule.start_date == "00000000":
            schedule.start_date = (
                date_sub(date_value, 6)
                if frequency == "W"
                else date_sub(date_value, 27)
                if frequency == "F"
                else date_value
            )

    schedule.prgrs = "W" if frequency == "W" else "I" if frequency == "F" else "D"
    if state.header_docdate != "00000000" and schedule.start_date and schedule.start_date < state.header_docdate:
        schedule.ettyp = "2"
    else:
        schedule.ettyp = classification or schedule.ettyp
    return schedule


def parse_decimal(value: str) -> Decimal:
    try:
        return Decimal(value.replace(",", "."))
    except InvalidOperation as exc:
        raise ValueError(f"Invalid numeric value '{value}' in input message.") from exc

# --------------------------------------------------------------------------- #
# EDIFACT -> IDoc transformation (primary orchestration).                    #
# --------------------------------------------------------------------------- #


def translate(segments: List[Segment], config: MappingConfig, separators: EDIFACTSeparators) -> MappingState:
    partner_table = load_table(config.partner_table)
    modifications_table = load_table(config.modifications_table)
    state = MappingState(
        separators=separators,
        config=config,
        partner_table=partner_table,
        modifications_table=modifications_table,
    )

    for segment in segments:
        tag = segment.tag

        if tag == "UNB":
            state.filedate = extract_component(segment.elements, 3, 0)
            state.filetime = extract_component(segment.elements, 3, 1)
            continue

        if tag == "UNH":
            state.message_ref = extract_component(segment.elements, 0, 0)
            continue

        if tag == "BGM":
            state.message_ref = extract_component(segment.elements, 1, 0) or state.message_ref
            continue

        if tag == "DTM":
            qualifier = extract_component(segment.elements, 0, 0)
            value = extract_component(segment.elements, 0, 1)
            format_code = extract_component(segment.elements, 0, 2)

            if state.current_line is None:
                if qualifier == "137":
                    state.header_docdate = normalise_date(value)
                    if state.header_startdate == "00000000":
                        state.header_startdate = state.header_docdate
                elif qualifier == "158":
                    state.header_startdate = normalise_date(value)
                elif qualifier == "159":
                    state.header_enddate = normalise_date(value)
                continue

            if state.last_rff_qualifier:
                if state.last_rff_qualifier == "AAU" and qualifier in {"171", "242"}:
                    state.current_line.last_delivery_date = normalise_date(value)
                state.last_rff_qualifier = None
                continue

            if state.pending_schedule and state.schedule_context and qualifier in {"2", "10", "158", "159"}:
                pending = compute_schedule_dates(state, state.pending_schedule, state.schedule_context, qualifier, value, format_code)
                if pending.start_date and pending.end_date:
                    append_schedule(state, pending)
                    state.pending_schedule = None
                continue

            continue

        if tag == "NAD":
            qualifier = extract_component(segment.elements, 0, 0)
            identifier = extract_component(segment.elements, 1, 0)
            name = extract_party_name(segment.elements)
            if qualifier == "SU":
                state.supplier = PartyInfo(number=identifier, name=name)
            elif qualifier == "BY":
                state.buyer = PartyInfo(number=identifier, name=name)
            elif qualifier == "ST":
                state.ship_to = PartyInfo(number=identifier, name=name)
            continue

        if tag == "GIS":
            code = extract_component(segment.elements, 0, 0)
            if code == "37":
                state.labky = "2"
            continue

        if tag == "LIN":
            line_id = extract_component(segment.elements, 0, 0)
            customer_item_component = extract_component(segment.elements, 2, 0)
            start_new_line(state, line_id=line_id, customer_item=customer_item_component)
            continue

        if tag == "PIA" and state.current_line:
            qualifier = extract_component(segment.elements, 2, 0)
            value = extract_component(segment.elements, 1, 0)
            if qualifier == "RY":
                state.current_line.design_revision = value
            continue

        if tag == "LOC" and state.current_line:
            qualifier = extract_component(segment.elements, 0, 0)
            location = extract_component(segment.elements, 1, 0)
            if qualifier == "11":
                state.current_line.unloading_point = location
                state.current_line.plant = location or state.current_line.plant
            elif qualifier == "159":
                state.current_line.consumption_point = location
            continue

        if tag == "RFF":
            qualifier = extract_component(segment.elements, 0, 0)
            reference = extract_component(segment.elements, 0, 1)
            state.last_rff_qualifier = qualifier
            if qualifier == "ON":
                state.header_refs.order_number = reference
            elif qualifier == "AAN":
                state.header_refs.release_number_new = reference
            elif qualifier == "AIF":
                state.header_refs.release_number_old = reference
            elif qualifier == "AAU" and state.current_line:
                state.current_line.last_delivery_note = reference
            continue

        if tag == "QTY" and state.current_line:
            qualifier = extract_component(segment.elements, 0, 0)
            quantity_value = extract_component(segment.elements, 0, 1)
            unit = extract_component(segment.elements, 0, 2)
            if not quantity_value:
                continue
            quantity = parse_decimal(quantity_value)

            if state.schedule_context:
                mapped_unit = resolve_unit(state, unit)
                state.current_line.unit = unit
                state.pending_schedule = ScheduleLine(quantity=quantity, unit=mapped_unit, ettyp="", prgrs="")
                continue

            if qualifier == "70":
                state.current_line.cumulative_qty = quantity
                state.current_line.unit = unit or state.current_line.unit
                state.current_line.mapped_unit = resolve_unit(state, unit) if unit else state.current_line.mapped_unit
            elif qualifier == "194":
                state.current_line.last_delivery_qty = quantity
                state.current_line.unit = unit or state.current_line.unit
            elif qualifier == "113":
                mapped_unit = resolve_unit(state, unit)
                state.current_line.unit = unit
                state.pending_schedule = ScheduleLine(quantity=quantity, unit=mapped_unit)
            continue

        if tag == "SCC" and state.current_line:
            classification = extract_component(segment.elements, 0, 0)
            frequency = extract_component(segment.elements, 2, 0)
            state.schedule_context = (classification, frequency)
            state.pending_schedule = None
            continue

        if tag == "UNT":
            finalise_current_line(state)
            break

    finalise_current_line(state)
    return state
# --------------------------------------------------------------------------- #
# IDoc rendering helpers                                                      #
# --------------------------------------------------------------------------- #


class IDocFormatter:
    def __init__(self, segment_defs: Dict[str, SegmentDefinition], field_defs: Dict[str, FieldDefinition]):
        self.segment_defs = segment_defs
        self.field_defs = field_defs

    def render(self, segment_name: str, field_values: Dict[str, str]) -> str:
        if segment_name not in self.segment_defs:
            raise KeyError(f"Unknown segment definition {segment_name}")
        segment_def = self.segment_defs[segment_name]
        rendered_parts: List[str] = []
        for field_name in segment_def.fields:
            definition = self.field_defs[field_name]
            value = field_values.get(field_name, definition.default)
            rendered_parts.append(format_field(field_name, value, definition))
        return "".join(rendered_parts)


def format_field(field_name: str, value: Optional[str], definition: FieldDefinition) -> str:
    if value is None or value == "":
        value = definition.default
    if value is None:
        value = ""
    text = str(value).strip()
    padded = text.ljust(definition.length)
    if len(padded) > definition.length:
        return padded[: definition.length]
    return padded


def build_idoc_lines(state: MappingState, formatter: IDocFormatter) -> List[str]:
    lines: List[str] = []

    rcvprn_value = resolve_rcvprn(state)
    debitor_value = resolve_debitor(state, state.lines[0]) if state.lines else ""

    credat = (
        state.config.override_credat
        or (state.header_docdate if state.config.force_sysdate_from_docdate and state.header_docdate else datetime.utcnow().strftime("%Y%m%d"))
    )
    if len(credat) != 8:
        credat = credat.zfill(8)
    if state.config.override_cretim:
        cretim = state.config.override_cretim
    elif state.config.force_systime_from_unb and state.filetime:
        cretim = (state.filetime + "00").ljust(6, "0")[:6]
    else:
        cretim = datetime.utcnow().strftime("%H%M%S")

    control_fields = {
        "EDI_DC40_MANDT": state.config.mandt,
        "EDI_DC40_DOCREL": state.config.docrel,
        "EDI_DC40_STATUS": "  ",
        "EDI_DC40_DIRECT": state.config.direct,
        "EDI_DC40_OUTMOD": state.config.outmod,
        "EDI_DC40_EXPRSS": state.config.exprss,
        "EDI_DC40_TEST": state.config.test_indicator,
        "EDI_DC40_IDOCTYP": "DELFOR01",
        "EDI_DC40_CIMTYP": state.config.cimtyp,
        "EDI_DC40_MESTYP": state.config.mestyp,
        "EDI_DC40_STD": state.config.std,
        "EDI_DC40_STDVRS": state.config.stdvrs,
        "EDI_DC40_STDMES": state.config.stdmes,
        "EDI_DC40_SNDPOR": state.config.sndpor,
        "EDI_DC40_SNDPRT": state.config.sndprt,
        "EDI_DC40_SNDPFC": state.config.sndpfc,
        "EDI_DC40_SNDPRN": debitor_value,
        "EDI_DC40_SNDSAD": state.config.sndsad,
        "EDI_DC40_SNDLAD": state.config.sndlad,
        "EDI_DC40_RCVPOR": state.config.rcvpor,
        "EDI_DC40_RCVPRT": state.config.rcvprt,
        "EDI_DC40_RCVPFC": state.config.rcvpfc,
        "EDI_DC40_RCVPRN": rcvprn_value,
        "EDI_DC40_RCVSAD": state.config.rcvsad,
        "EDI_DC40_RCVLAD": state.config.rcvlad,
        "EDI_DC40_CREDAT": credat,
        "EDI_DC40_CRETIM": cretim,
        "EDI_DC40_ARCKEY": state.config.archiv_key,
    }
    lines.append(formatter.render("EDI_DC40", control_fields))

    header_fields = {
        "E2EDK09_MANDT": state.config.mandt,
        "E2EDK09_VTRNR": state.header_refs.order_number,
        "E2EDK09_LABNK": state.header_refs.release_number_new,
        "E2EDK09_ABNRA": state.header_refs.release_number_old,
        "E2EDK09_BSTDK": state.header_docdate,
    }
    lines.append(formatter.render("E2EDK09", header_fields))

    lines.append(
        formatter.render(
            "E2EDKA1_LF",
            {
                "E2EDKA1_LF_MANDT": state.config.mandt,
                "E2EDKA1_LF_PARTN": state.supplier.number,
            },
        )
    )
    lines.append(
        formatter.render(
            "E2EDKA1_WE",
            {
                "E2EDKA1_WE_MANDT": state.config.mandt,
                "E2EDKA1_WE_PARTN": state.ship_to.number,
                "E2EDKA1_WE_NAME1": state.ship_to.name,
            },
        )
    )
    lines.append(
        formatter.render(
            "E2EDKA1_OMI",
            {
                "E2EDKA1_OMI_MANDT": state.config.mandt,
                "E2EDKA1_OMI_PARTN": state.buyer.number,
            },
        )
    )

    for line in state.lines:
        qty_cumulative = format_quantity(line.cumulative_qty) if line.cumulative_qty is not None else ""
        qty_last_delivery = format_quantity(line.last_delivery_qty) if line.last_delivery_qty is not None else ""

        e2edp10_fields = {
            "E2EDP10_MANDT": state.config.mandt,
            "E2EDP10_SEGNAM2": "   ",
            "E2EDP10_SEGNAM3": "",
            "E2EDP10_IDNKD": line.customer_item,
            "E2EDP10_VRKME": line.mapped_unit,
            "E2EDP10_KWERK": line.plant,
            "E2EDP10_DFABL": line.unloading_point,
            "E2EDP10_VBRST": line.consumption_point,
            "E2EDP10_BELNR": line.last_delivery_note,
            "E2EDP10_LFIMG": qty_last_delivery,
            "E2EDP10_AKUEM": qty_cumulative,
            "E2EDP10_LIDTL": line.last_delivery_date,
            "E2EDP10_ABRAB": line.abrab,
            "E2EDP10_ABRBI": line.abrbi,
            "E2EDP10_SCREL": "03",
            "E2EDP10_LABKY": line.labky,
            "E2EDP10_DESRE": line.design_revision,
            "E2EDP10_BSTDK": state.header_docdate,
        }
        lines.append(formatter.render("E2EDP10", e2edp10_fields))

        for schedule in line.schedules:
            schedule_fields = {
                "E2EDP16_MANDT": state.config.mandt,
                "E2EDP16_ETTYP": schedule.ettyp,
                "E2EDP16_PRGRS": schedule.prgrs,
                "E2EDP16_EDATUV": schedule.start_date,
                "E2EDP16_EZEIT": schedule.time,
                "E2EDP16_EDATUB": schedule.end_date,
                "E2EDP16_WMENG": format_quantity(schedule.quantity),
            }
            lines.append(formatter.render("E2EDP16", schedule_fields))

    return lines
# --------------------------------------------------------------------------- #
# Command-line interface                                                      #
# --------------------------------------------------------------------------- #


def configure_logging(verbosity: int) -> None:
    level = logging.WARNING
    if verbosity == 1:
        level = logging.INFO
    elif verbosity >= 2:
        level = logging.DEBUG
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert BOSAL DELFOR D97A messages into SAP DELFOR01 IDoc text.",
    )
    parser.add_argument("--input", required=True, help="Path to the EDIFACT input file.")
    parser.add_argument("--output", required=True, help="Target path for the generated IDoc file.")
    parser.add_argument("--config", help="Optional JSON configuration file overriding defaults.")
    parser.add_argument("--verify", help="Optional reference file; enables byte-for-byte comparison.")
    parser.add_argument("--log-level", action="count", default=0, help="Increase log verbosity (-v, -vv).")
    args = parser.parse_args()

    configure_logging(args.log_level)

    base_path = Path.cwd()
    config = load_config(base_path, Path(args.config) if args.config else None)

    segments, separators = parse_edifact(Path(args.input).read_text(encoding="utf-8"))
    print(f"[check] parsed {len(segments)} EDIFACT segments using separators {separators}.")

    state = translate(segments, config, separators)

    required_segments = ["EDI_DC40", "E2EDK09", "E2EDKA1_LF", "E2EDKA1_WE", "E2EDKA1_OMI", "E2EDP10", "E2EDP16"]
    segment_defs, field_defs = load_segment_metadata(config.forms_out, required_segments)
    formatter = IDocFormatter(segment_defs, field_defs)
    idoc_lines = build_idoc_lines(state, formatter)

    output_path = Path(args.output)
    output_path.write_text("\n".join(idoc_lines) + "\n", encoding="utf-8")

    print(f"[check] generated {len(idoc_lines)} IDoc segments; output written to {output_path}.")

    if args.verify:
        reference = Path(args.verify).read_text(encoding="utf-8")
        produced = output_path.read_text(encoding="utf-8")
        if produced == reference:
            print("[check] verification succeeded: output matches reference sample exactly.")
        else:
            raise SystemExit("Verification failed: generated output differs from reference.")


if __name__ == "__main__":
    main()
