### Purpose
This document defines all **agents**, **their roles**, **responsibilities**, and **interaction workflows** within the IAP086 project.  
The goal is to ensure consistent, traceable, and explainable collaboration between AI-based and human agents involved in **EDI mapping automation and validation**.

---

## ⚙️ 1. Agent Overview

| Agent Name | Type | Primary Responsibility | Input | Output |
|-------------|------|------------------------|--------|---------|
| **Lead Developer** | Human | Defines architecture, approves mapping logic and script design. | All project artifacts. | Approved implementation plan and verified output. |
| **Mapping Architect (GPT-5)** | AI | Translates specifications into mapping logic; writes transformation scripts. | Forms, Mapping files, Guidelines, Tables, Input/Output samples. | Python transformation scripts + intermediate documentation. |
| **Validation Agent** | AI | Compares generated outputs with references; runs semantic + masked validation. | Generated and reference EDI files. | Pass/fail reports, discrepancy logs. |
| **Documentation Agent** | AI | Generates Markdown reports (`EXPLANATION.md`, `INTERMEDIATE_DOC.md`, etc.). | Logs and code commits. | Human-readable project documentation. |
| **Reviewer Agent** | Human | Performs peer review of mapping accuracy, compliance, and script quality. | Mapping logic, validation logs. | Approval feedback or change requests. |
| **Integration Agent** | AI | Merges validated mapping logic into production workflow; ensures compatibility. | Approved scripts, SAP/BOSAL mapping tables. | Production-ready transformation component. |
| **QA/Testing Agent** | Human | Conducts end-to-end test runs with real EDI data. | Compiled executable / script. | Signed-off QA report. |

---

## 🧠 2. Agent Role Definitions

### **Mapping Architect (GPT-5)**
- **Purpose:**  
  Converts EDI *forms*, *mapping*, *guidelines*, and *tables* into a fully functional Python translation engine.
- **Core Skills:**  
  EDI/IDoc standards, mapping logic synthesis, transformation validation, structured documentation.
- **Outputs:**  
  - `mapping_translator.py`
  - `EXPLANATION.md`
  - `INTERMEDIATE_DOC.md`
- **Success Criteria:**  
  Output file matches reference sample exactly (validated by Validation Agent).

---

### **Validation Agent**
- **Purpose:**  
  Ensures generated IDoc output matches the provided reference sample *semantically* and *structurally*.
- **Responsibilities:**
  - Perform **mask-aware** comparisons (allowing wildcards like “...” for redacted fields).
  - Verify all mapped fields (BGM, NAD, LIN, SCC, QTY, DTM, etc.) against mapping rules.
  - Generate validation report: ✅ *PASS* / ❌ *FAIL* with reason.
- **Inputs:**  
  Generated output, Reference output, Mapping rules.
- **Outputs:**  
  `validation_report.json` and inline validation messages in the log.

---

### **Documentation Agent**
- **Purpose:**  
  Automatically generate Markdown documentation for every stage of the pipeline.
- **Artifacts produced:**
  - `EXPLANATION.md` — overall design rationale.
  - `INTERMEDIATE_DOC.md` — phase-by-phase rationale, validations, and open issues.
  - `AGENTS.md` (this file).
- **Style Requirements:**
  - Use consistent Markdown formatting.
  - Include citations when referencing project files.
  - Ensure all documentation is human-readable and audit-friendly.

---

### **Integration Agent**
- **Purpose:**  
  Deploy validated mapping scripts into the operational EDI translation pipeline (SAP/BOSAL environments).
- **Responsibilities:**
  - Validate compatibility with SAP IDoc versions (e.g., DELFOR01, DELFOR02).
  - Ensure mapping tables (e.g., `mapping_table_partner_SAPP49_110.txt`) are synchronized.
  - Run smoke tests post-deployment.

---

### **Lead Developer**
- **Purpose:**  
  Oversees AI agents, approves deliverables, and ensures all logic adheres to the client’s EDI rules.
- **Responsibilities:**
  - Define development milestones.
  - Provide clarifications when mapping ambiguities arise.
  - Approve or reject AI-generated scripts before integration.

---

### **Reviewer Agent**
- **Purpose:**  
  Performs manual review of AI-generated outputs for correctness, maintainability, and compliance.
- **Responsibilities:**
  - Check that no field values are invented or copied directly from reference samples.
  - Ensure mapping logic follows the mapping/trantab instructions.
  - Sign off before deployment to production.

---

### **QA/Testing Agent**
- **Purpose:**  
  Conducts live data testing with the final integrated script.
- **Responsibilities:**
  - Execute multiple test cases with real EDI inbound messages.
  - Verify that output passes all SAP import validations.
  - Produce a final QA compliance report.

---

## 🔄 3. Agent Workflow

### **Process Diagram (textual)**

```
┌────────────────────┐
│ Lead Developer     │
│ defines task/specs │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│ Mapping Architect  │───reads──► forms, mapping, guideline, tables
│ (GPT-5)            │
│ builds translator  │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│ Validation Agent   │───compares──► generated vs reference
│ (GPT-5)            │
│ produces report    │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│ Reviewer Agent     │
│ human verification │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│ Integration Agent  │───deploys──► SAP/BOSAL environment
│ (GPT-5)            │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│ QA/Testing Agent   │───tests──► live EDI data
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│ Lead Developer     │
│ final approval     │
└────────────────────┘
```

---

## 🪶 4. Communication Protocol

- **Channels:**  
  - AI-to-AI: Direct internal messaging with structured JSON summaries.  
  - Human-to-AI: Markdown-based task instructions (e.g., `Developer:` or `Reviewer:` headers).  
  - Human approvals always override AI assumptions.

- **Commit Format:**  
  Each agent must commit changes or reports in this naming convention:
  ```
  [agent-type]/[file]/[short-description]
  e.g. mapping/translator/add-parsing-logic
  ```

- **Artifacts Directory Structure:**
  ```
  /artifacts
  ├── mapping/
  │   ├── mapping_delfor_d97a_bosal.delfor01_sap6xx_btc.txt
  │   └── mapping_table_partner_SAPP49_110.txt
  ├── forms/
  │   ├── forms_in_delfor_d97a_bosal.txt
  │   └── forms_out_delfor01_sap46x_btc.txt
  ├── guidelines/
  │   └── guideline.md
  ├── samples/
  │   ├── input_sample.txt
  │   ├── output_sample.txt
  └── scripts/
      └── mapping_translator.py
  ```

---

## 🧾 5. Validation Policy

| Stage | Responsible Agent | Validation Criteria |
|--------|-------------------|--------------------|
| Input parsing | Mapping Architect | Conforms to UNA/UNB/UNH separators and segment definitions. |
| Mapping logic | Mapping Architect | Follows mapping/trantab strictly; no assumptions. |
| Output generation | Validation Agent | Matches sample structure and field rules. |
| Documentation | Documentation Agent | Markdown-compliant, well-cited, human readable. |
| Review | Reviewer Agent | Compliance, maintainability, accuracy. |
| Integration | Integration Agent | System compatibility and no data loss. |
| QA Testing | QA Agent | SAP acceptance, no mapping breaks. |

---

## 🧩 6. Escalation Matrix

| Level | Trigger | Responsible |
|--------|----------|-------------|
| **L1** | Syntax or validation mismatch | Mapping Architect |
| **L2** | Rule ambiguity or conflicting spec | Lead Developer |
| **L3** | Deployment or integration failure | Integration Agent + Lead Developer |
| **L4** | SAP/Partner compliance deviation | QA Agent + Lead Developer |

---

## 🪜 7. Versioning and Traceability

- **Versioning:**  
  Every mapping script increment must increment the version header inside the file:
  ```python
  __version__ = "vX.Y.Z"
  ```
- **Traceability Tags:**  
  Each commit or doc must include:
  ```
  # Trace: IAP086-MAP-[YYMMDD]-[AgentName]
  ```
- **Audit Logs:**  
  All validation, transformation, and comparator runs are logged automatically in `/logs/validation_history.json`.

---

## 🧭 8. Quality Targets

| Metric | Goal |
|---------|------|
| EDI structural accuracy | 100% |
| Mapping compliance with spec | 100% |
| Output reference match (masked) | 100% |
| Output reference match (strict, non-redacted) | ≥ 99.9% |
| Documentation completeness | 100% |
| Review approval | Required before deployment |

---

## 🔒 9. Governance and Ethical Rules

- **No Data Invention:**  
  Agents must not introduce values not explicitly defined by provided mapping artifacts.  
- **Auditability:**  
  Every AI decision must be traceable to a rule, mapping line, or input field.  
- **Human Override:**  
  Human Lead Developer and Reviewer have final authority.  
- **Confidentiality:**  
  Mapping tables and partner data are confidential; never published externally.  

---

## ✅ 10. Final Notes

- **This AGENTS.md governs all AI and human collaboration for EDI mapping automation.**  
- It ensures reproducible, verifiable transformations and structured documentation at every phase.  
- Updates to this file must be approved by the **Lead Developer** and documented as `AGENTS.md – Revision [n]`.

---

**Document ID:** `IAP086-AGENTS-v1.0`  
**Maintained by:** *Lead Developer, IAP086 Project*  
**Last Updated:** `2025-10-23`
