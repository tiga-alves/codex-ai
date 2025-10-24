<!-- image -->

## DELFOR Delivery Forecast Delivery Schedule Message

Document Name :

BOSAL\_EDI-DELFOR-Guideline.docx Aug, 15 th31  May 2019 3.0 Jose Manzur &amp; Akhil Navaneeth

Date :

Version :

Author :

## Table of Contents

| INTRODUCTION ................................................................................................. .....................................................3   | INTRODUCTION ................................................................................................. .....................................................3   | INTRODUCTION ................................................................................................. .....................................................3   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2 SEGMENT/SEGMENT-GROUP OVERVIEW ........................................................................................... ...........4                               | 2 SEGMENT/SEGMENT-GROUP OVERVIEW ........................................................................................... ...........4                               | 2 SEGMENT/SEGMENT-GROUP OVERVIEW ........................................................................................... ...........4                               |
| 2.1                                                                                                                                                                     | MESSAGE STRUCTURE ........................................................................................................... ......... .................               | 5                                                                                                                                                                       |
| 3 SEGMENT DETAILS ............................................................................................................. ................................... 8   | 3 SEGMENT DETAILS ............................................................................................................. ................................... 8   | 3 SEGMENT DETAILS ............................................................................................................. ................................... 8   |
| 3.1                                                                                                                                                                     | SEGMENT: UNH MESSAGE HEADER ......................................................................................................................                      | 8                                                                                                                                                                       |
| 3.2                                                                                                                                                                     | SEGMENT: BGM BEGINNING OF MESSAGE ............................................................................................................                          | 9                                                                                                                                                                       |
| 3.3                                                                                                                                                                     | SEGMENT: DTM DATE/TIME/PERIOD ....................................................................................................................                      | 10                                                                                                                                                                      |
| 3.4                                                                                                                                                                     | SEGMENT GROUP 2 : NAME AND ADDRESS .............................................................................................................                        | 11                                                                                                                                                                      |
| 3.4.1 Segment: NAD Name and Address .................................................................................................................12                 | 3.4.1 Segment: NAD Name and Address .................................................................................................................12                 |                                                                                                                                                                         |
| 3.5 SEGMENT GROUP 6 : GENERAL INDICATOR ................................................................................................... ......                      | 3.5 SEGMENT GROUP 6 : GENERAL INDICATOR ................................................................................................... ......                      | 14                                                                                                                                                                      |
| 3.5.1 Segment: GIS General Indicator ....................................................................................................................14             | 3.5.1 Segment: GIS General Indicator ....................................................................................................................14             |                                                                                                                                                                         |
| 3.6 SEGMENT GROUP 7 : NAMEAND ADDRESS ...........................................................................................................                       | 3.6 SEGMENT GROUP 7 : NAMEAND ADDRESS ...........................................................................................................                       | 15                                                                                                                                                                      |
| 3.6.1                                                                                                                                                                   | Segment: NAD Name and Address ............................................................................................................ .. ...                       | 16                                                                                                                                                                      |
| 3.7 SEGMENT GROUP 12 : LINE ITEM .................................................................................................................... ........          | 3.7 SEGMENT GROUP 12 : LINE ITEM .................................................................................................................... ........          | 17                                                                                                                                                                      |
| 3.7.1                                                                                                                                                                   | Segment: LIN Line Item ...............................................................................................................................                  | .. 18                                                                                                                                                                   |
| 3.7.2                                                                                                                                                                   | Segment: PIA Product Additional Information …........................................................................................                                   | .. 19                                                                                                                                                                   |
| 3.7.3                                                                                                                                                                   | Segment: IMD Item Description ..................................................................................................................                        | .. 20                                                                                                                                                                   |
| 3.7.4                                                                                                                                                                   | Segment: LOC Place/Location Identification …..........................................................................................                                  | ... 21                                                                                                                                                                  |
| 3.8 SEGMENT GROUP 13 : REFERENCE ..........................................................................................................................             | 3.8 SEGMENT GROUP 13 : REFERENCE ..........................................................................................................................             | 22                                                                                                                                                                      |
| 3.8.1                                                                                                                                                                   | Segment: RFF Reference ............................................................................................................................                     | ... 22                                                                                                                                                                  |
| 3.8.2                                                                                                                                                                   | Segment: DTM Date/Time/Period...............................................................................................................                            | ... 23                                                                                                                                                                  |
| 3.9 SEGMENT GROUP 15 : QUANTITY ……………….……...........................................................................................                                    | 3.9 SEGMENT GROUP 15 : QUANTITY ……………….……...........................................................................................                                    | 24                                                                                                                                                                      |
| 3.9.1                                                                                                                                                                   | Segment: QTY Quantity ...........................................................................................................                                       | ...................... 25                                                                                                                                               |
| 3.9.2                                                                                                                                                                   | Segment: DTM Date/Time/Period..................................................................................................................                         | 26                                                                                                                                                                      |
| 3. 10 SEGMENT GROUP 16 : REFERENCES RELATEDTOQUANTITY .................................................................................                                 | 3. 10 SEGMENT GROUP 16 : REFERENCES RELATEDTOQUANTITY .................................................................................                                 | 27                                                                                                                                                                      |
| 3.10.1                                                                                                                                                                  | Segment: RFF Reference ...................................................................................................................                              | ......... ... 27                                                                                                                                                        |
| 3.10.2                                                                                                                                                                  | Segment: DTM Date/Time/Period.............................................................................................................                              | .. ... 28                                                                                                                                                               |
| 3.11 SEGMENT GROUP 17 : SCHEDULING CONDITIONS ..................................................................................................                        | 3.11 SEGMENT GROUP 17 : SCHEDULING CONDITIONS ..................................................................................................                        | 29                                                                                                                                                                      |
| 3.11.1 Segment: SCC Scheduling Conditions ....................................................................................................... ....                  | 3.11.1 Segment: SCC Scheduling Conditions ....................................................................................................... ....                  | 30                                                                                                                                                                      |
| 3.12 SEGMENT GROUP 18 : QUANTITY ...........................................................................................................................            | 3.12 SEGMENT GROUP 18 : QUANTITY ...........................................................................................................................            | 31                                                                                                                                                                      |
| 3.12.1 Segment: QTY Quantity .............................................................................................................................              | 3.12.1 Segment: QTY Quantity .............................................................................................................................              | .... 31                                                                                                                                                                 |
| 3.12.2 Segment: DTM Date/Time/Period..............................................................................................................                      | 3.12.2 Segment: DTM Date/Time/Period..............................................................................................................                      | .... 32                                                                                                                                                                 |
| 3.13 SEGMENT GROUP 20: PACKAGE ...............................................................................................................................          | 3.13 SEGMENT GROUP 20: PACKAGE ...............................................................................................................................          | 33                                                                                                                                                                      |
| 3.13.1 Segment: PAC Package ……………….............................................................................................................                         | 3.13.1 Segment: PAC Package ……………….............................................................................................................                         | 33                                                                                                                                                                      |
| 3.14 SEGMENT: UNT MESSAGE TRAILER ....................................................................................................................                  | 3.14 SEGMENT: UNT MESSAGE TRAILER ....................................................................................................................                  |                                                                                                                                                                         |
| EXAMPLE MESSAGE (LN PLANT) .................................................................................................. ..................                        | EXAMPLE MESSAGE (LN PLANT) .................................................................................................. ..................                        | 32                                                                                                                                                                      |
|                                                                                                                                                                         | EXAMPLE MESSAGE (JDE PLANT) ................................................................................................. .................                         | 33                                                                                                                                                                      |
|                                                                                                                                                                         | EXAMPLE MESSAGE (IFS PLANT) ......................................................................................................... ..........                        | 34                                                                                                                                                                      |

Last Saved :   Aug, 15 th  2018

## 1 Introduction

This version of the DELFOR is not upward compatible with versions prior to D96B. DELFOR is  a  message  which  is  sent  from  a  party  who  is  planning  the  use  or  consumption  of products to a party who has to plan for the supply of the products. The message gives the requirements regarding details for short term delivery and/or medium to long scheduling for products. The scheduling can be used to authorize manufacturing and or the provision of materials. This is based on the terms and conditions defined in a purchase order or contract. Bosal uses different IT system in some plants. We have:

- LN plants
- JDE plants
- IFS plants

The DELFOR standard generated from all BOSAL plants is D 97A. Please check below the message structure.

## 2 Segment/Segment-Group Overview

## DELFOR D.97A

|   Pos. No. | Seg. ID   | Name                                                   | Req. Des.   | Max. Use   | Group Repeat   | Note and Comments   |
|------------|-----------|--------------------------------------------------------|-------------|------------|----------------|---------------------|
|       0010 | UNH       | Message Header                                         | M           | 1          |                |                     |
|       0020 | BGM       | Beginning of Message                                   | M           | 1          |                |                     |
|       0030 | DTM       | Date/Time/Period                                       | M           | 10         |                |                     |
|       0080 |           | Segment Group 2: NAD                                   | C           |            | 99             |                     |
|       0090 | NAD       | Name and Address                                       | M           | 1          |                |                     |
|       0190 |           | Segment Group 6: GIS-SG7-SG12                          | C           |            | 9999           |                     |
|       0200 | GIS       | General Indicator                                      | M           | 1          |                |                     |
|       0210 |           | Segment Group 7: NAD                                   |             |            | 1              |                     |
|       0220 | NAD       | Name and Address                                       | M           | 1          |                |                     |
|       0370 |           | Segment Group 12: LIN-PIA-IMD-LOC- SG13-SG15-SG17-SG20 | C           |            | 9999           |                     |
|       0380 | LIN       | Line Item                                              | M           | 1          |                |                     |
|       0390 | PIA       | Product Additional Information                         | C           | 10         |                |                     |
|       0400 | IMD       | Item Description                                       | C           | 10         |                |                     |
|       0450 | LOC       | Place/Location Identification                          | C           | 999        |                |                     |
|       0480 |           | Segment Group 13: RFF-DTM                              | C           |            | 10             |                     |
|       0490 | RFF       | Reference                                              | M           | 1          |                |                     |
|       0500 | DTM       | Date/Time/Period                                       | C           | 1          |                |                     |
|       0540 |           | Segment Group 15: QTY-DTM-SG16                         | C           |            | 10             |                     |
|       0550 | QTY       | Quantity                                               | M           | 1          |                |                     |
|       0560 | DTM       | Date/Time/Period                                       | C           | 2          |                |                     |
|       0570 |           | Segment Group 16: RFF-DTM                              | C           |            | 10             |                     |
|       0580 | RFF       | Reference                                              | M           | 1          |                |                     |
|       0590 | DTM       | Date/Time/Period                                       | C           | 1          |                |                     |
|       0600 |           | Segment Group 17: SCC-SG18                             | C           |            | 999            |                     |
|       0610 | SCC       | Scheduling Conditions                                  | M           | 1          |                |                     |
|       0620 |           | Segment Group 18: QTY-DTM                              | C           |            | 999            |                     |
|       0630 | QTY       | Quantity                                               | M           | 1          |                |                     |
|       0640 | DTM       | Date/Time/Period                                       | C           | 2          |                |                     |
|       0680 |           | Segment Group 20: PAC                                  | C           | 99         |                |                     |
|       0690 | PAC       | Package Information                                    | C           | 1          |                |                     |
|       1030 | UNT       | Final segment of message                               | M           | 1          |                |                     |

M = Mandatory

C = Conditional

N = Not used

Last Saved :   Aug, 15 th  2018

## 2.1 Message structure

http://www.unece.org/trade/untdid/d97a/trmd/delfor\_s.htm

<!-- image -->

|   Pos | Tag & Name             | Tag & Name             | Tag & Name             | Tag & Name                    | S   |    R |
|-------|------------------------|------------------------|------------------------|-------------------------------|-----|------|
|  0010 | UNH                    | Message Header         | Message Header         | Message Header                | M   |    1 |
|  0020 | BGM                    | Beginning of Message   | Beginning of Message   | Beginning of Message          | M   |    1 |
|  0030 | DTM                    | Date/time/period       | Date/time/period       | Date/time/period              | M   |   10 |
|  0040 | FTX                    | Free text              | Free text              | Free text                     | C   |    5 |
|  0050 | Segment Group 1        | Segment Group 1        | Segment Group 1        | Segment Group 1               | C   |   10 |
|  0060 | ├ ────                 | RFF                    | Reference              | Reference                     | M   |    1 |
|  0070 | ├ ────                 | DTM                    | Date/time/period       | Date/time/period              | C   |    1 |
|  0080 | Segment Group 2        | Segment Group 2        | Segment Group 2        | Segment Group 2               | C   |   99 |
|  0090 | ├ ────                 | NAD                    | Name and Address       | Name and Address              | M   |    1 |
|  0100 | ├ ──── Segment Group 3 | ├ ──── Segment Group 3 | ├ ──── Segment Group 3 | ├ ──── Segment Group 3        | C   |   10 |
|  0110 | │                      | ├ ────                 | RFF                    | Reference                     | M   |    1 |
|  0120 | │                      | └────                  | DTM                    | Date/time/period              | C   |    1 |
|  0100 | ├ ──── Segment Group 4 | ├ ──── Segment Group 4 | ├ ──── Segment Group 4 | ├ ──── Segment Group 4        | C   |    5 |
|  0140 | │                      | ├ ────                 | CTA                    | Contact Information           | M   |    1 |
|  0150 | │                      | └────                  | COM                    | Communication Contact         | C   |    5 |
|  0160 | Segment Group 5        | Segment Group 5        | Segment Group 5        | Segment Group 5               | C   |   10 |
|  0170 | ├ ────                 | TDT                    | Details of Transport   | Details of Transport          | M   |    1 |
|  0180 | ├ ────                 | DTM                    | Date/time/period       | Date/time/period              | C   |    5 |
|  0160 | Segment Group 6        | Segment Group 6        | Segment Group 6        | Segment Group 6               | C   | 9999 |
|  0200 | ├ ────                 | GIS                    | General Indicator      | General Indicator             | M   |    1 |
|  0210 | ├ ──── Segment Group 7 | ├ ──── Segment Group 7 | ├ ──── Segment Group 7 | ├ ──── Segment Group 7        | C   |    1 |
|  0220 | │                      | ├ ────                 | NAD                    | Name and Address              | M   |    1 |
|  0230 | │                      | ├ ────                 | LOC                    | Place/Location Identification | C   |   10 |
|  0240 | │                      | └────                  | FTX                    | Free Text                     | C   |    5 |
|  0250 | │                      | ├ ────                 | Segment Group 8        | Segment Group 8               | C   |   10 |
|  0260 | │                      | │                      | ├ ────                 | RFF Reference                 | M   |    1 |
|  0270 | │                      | │                      | └────                  | DTM Date/time/period          | C   |    1 |
|  0280 | │                      | ├ ────                 | Segment Group 9        | Segment Group 9               | C   |   10 |
|  0290 | │                      | │                      | ├ ────                 | DOC Document/message Details  | M   |    1 |
|  0300 | │                      | │ ├ ────               | └────                  | DTM Date/time/period          | C   |   10 |
|  0310 | │                      | Segment Group 10       | Segment Group 10       | Segment Group 10              | C   |    5 |
|  0320 | │                      | │                      | ├ ────                 | CTA Contact Information       | M   |    1 |
|  0330 | │                      | │                      | └────                  | COM Communication Contact     | C   |    5 |
|  0340 | │                      | ├ ────                 | Segment Group 11       | Segment Group 11              | C   |   10 |
|  0350 | │                      | │ │                    | ├ ────                 | TDT Details of Transport      | M   |    1 |
|  0360 | │                      |                        | └────                  | DTM Date/time/period          | C   |    5 |

Last Saved :   Aug, 15 th  2018

<!-- image -->

Last Saved :   Aug, 15 th  2018

<!-- image -->

|   Pos | Tag & Name   | Tag & Name   | Tag & Name       | Tag & Name              | Tag & Name                    | Tag & Name                    | Tag & Name                    | S   |   R |
|-------|--------------|--------------|------------------|-------------------------|-------------------------------|-------------------------------|-------------------------------|-----|-----|
|  0760 | │            | ├ ────       | Segment Group 22 | Segment Group 22        | Segment Group 22              | Segment Group 22              | Segment Group 22              | C   | 999 |
|  0770 | │            | │            | ├ ────           | NAD                     | Name and Address              | Name and Address              | Name and Address              | M   |   1 |
|  0780 | │            | │            | ├ ────           | LOC                     | Place/Location Identification | Place/Location Identification | Place/Location Identification | C   |  10 |
|  0790 | │            | │            | └────            | FTX                     | Free Text                     | Free Text                     | Free Text                     | C   |   5 |
|  0800 | │            | │            | ├ ────           | Segment Group 23        | Segment Group 23              | Segment Group 23              | Segment Group 23              | C   |  10 |
|  0810 | │            | │            | │                | ├ ────                  | DOC                           | Document/message Details      | Document/message Details      | M   |   1 |
|  0820 | │            | │            | │                | └────                   | DTM                           | Date/time/period              | Date/time/period              | C   |   1 |
|  0830 | │            | │            | ├ ────           | Segment Group 24        | Segment Group 24              | Segment Group 24              | Segment Group 24              | C   |   5 |
|  0840 | │            | │            | │                | ├ ────                  | CTA                           | Contact Information           | Contact Information           | M   |   1 |
|  0850 | │            | │            | │                | └────                   | COM                           | Communication Contact         | Communication Contact         | C   |   5 |
|  0860 | │            | │            | ├ ────           | Segment Group 25        | Segment Group 25              | Segment Group 25              | Segment Group 25              | C   |  10 |
|  0870 | │            | │            | │                | ├ ────                  | QTY                           | Quantity                      | Quantity                      | M   |   1 |
|  0880 | │            | │            | │                | └────                   | DTM                           | Date/time/period              | Date/time/period              | C   |   2 |
|  0890 | │            | │            | │                | ├ ──── Segment Group 26 | ├ ──── Segment Group 26       | ├ ──── Segment Group 26       | ├ ──── Segment Group 26       | C   |  10 |
|  0900 | │            | │            | │                | │                       | ├ ────                        | RFF                           | Reference                     | M   |   1 |
|  0910 | │            | │            | │                | │                       | └────                         | DTM                           | Date/time/period              | C   |   1 |
|  0920 | │            | │            | ├ ────           | Segment Group 27        | Segment Group 27              | Segment Group 27              | Segment Group 27              | M   | 999 |
|  0930 | │            | │            | └────            | ─────                   | SCC                           | Scheduling Conditions         | Scheduling Conditions         | M   |   1 |
|  0940 | │            | │            | │                | ├ ────                  | Segment Group 28              | Segment Group 28              | Segment Group 28              | M   | 999 |
|  0950 | │            | │            | │                | │                       | ├ ────                        | QTY                           | Quantity                      | M   |   1 |
|  0960 | │            | │            | │                | │                       | └────                         | DTM                           | Date/time/period              | C   |   2 |
|  0970 | │            | │            | │                | │                       | ├ ────                        | Segment Group 29              | Segment Group 29              | C   |  10 |
|  0980 | │            | │            | │                | │                       | ├ ────                        | RFF                           | Reference                     | M   |   1 |
|  0990 | │            | │            | │                | │                       | └────                         | DTM                           | Date/time/period              | C   |   1 |
|  1000 | │            | │            | ├ ────           | Segment Group 30        | Segment Group 30              | Segment Group 30              | Segment Group 30              | C   |  10 |
|  1010 | │            | │            | │                | ├ ────                  | TDT                           | Details of Transport          | Details of Transport          | M   |   1 |
|  1020 | │            | │            | │                | ├ ────                  | DTM                           | Date/time/period              | Date/time/period              | C   |   5 |
|  1030 | │            | │            | │                | └────                   | UNT                           | Message Trailer               | Message Trailer               | M   |   1 |

## 3 Segment details

## 3.1 Segment: UNH Message Header

| Position          | 0010                                                                                                                                                                                                                                                                                                            |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Group             |                                                                                                                                                                                                                                                                                                                 |
| Level             | 0                                                                                                                                                                                                                                                                                                               |
| Usage             | Mandatory                                                                                                                                                                                                                                                                                                       |
| Max Use           | 1                                                                                                                                                                                                                                                                                                               |
| Purpose           | A service segment starting and uniquely identifying a message. The message type code for the Delivery schedule message is DELFOR. Note: Delivery schedule messages conforming to this document must contain the following data in segment UNH, composite S009: Data element 0065 DELFOR 0052 D 0054 97A 0051 UN |
| Dependency Notes: |                                                                                                                                                                                                                                                                                                                 |
| Semantic Notes:   |                                                                                                                                                                                                                                                                                                                 |
| Comments          |                                                                                                                                                                                                                                                                                                                 |

## Data Element Summary

|    | Data Element   | Component Element   | Name                                                                                                                                                                                                                                                                                                                                           | Attributes   | Attributes   |
|----|----------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|--------------|
| M  | 0062           |                     | MESSAGE REFERENCE NUMBER Unique message reference assigned by the sender.                                                                                                                                                                                                                                                                      | M            | an..14       |
| M  | S009           |                     | MESSAGE IDENTIFIER Identification of the type, version etc. of the message being interchanged.                                                                                                                                                                                                                                                 | M            |              |
| M  |                | 0065                | Message type identifier Code identifying a type of message and assigned by its controlling agency. DELFOR Delivery schedule message A code to identify the delivery schedule message.                                                                                                                                                          | M            | an..6        |
| M  |                | 0052                | Message type version number Version number of a message type. D Draft version/UN/EDIFACT Directory Message approved and issued as a draft message (Valid for directories published after March 1993 and prior to March 1997). Message approved as a standard message (Valid for directories published after March 1997).                       | M            | an..3        |
| M  |                | 0054                | Message type release number Release number within the current message type version number (0052). 97A Release 1997 - A Message approved and issued in the first 1997 release of the UNTDID (United Nations Trade Data Interchange Directory). 96A Release 1996 - A                                                                             | M            | an..3        |
| M  |                | 0051                | Controlling agency Code identifying the agency controlling the specification, maintenance and publication of the message type. UN UN/ECE/TRADE/WP.4 United Nations Economic UN Economic Commission for Europe (UN/ECE), Committee on the development of trade (TRADE), Working Party on facilitation of international trade procedures (WP.4). | M            | an..2        |

## Example:

UNH+1+DELFOR:D:97A:UN'

Last Saved :   Aug, 15 th  2018

## 3.2 Segment: BGM Beginning of Message

| Position   | 0020                                                                                 |
|------------|--------------------------------------------------------------------------------------|
| Group      |                                                                                      |
| Level      | 0                                                                                    |
| Usage      | Mandatory                                                                            |
| Max Use    | 1                                                                                    |
| Purpose    | A segment for unique identification of the Delivery schedule message by means of its |
|            | name and its number and its function (original, replacement, change).                |
| Comments   |                                                                                      |

## Data Element Summary

| Data element   | Component Element   | Name                                                                                                                         | Attributes   |
|----------------|---------------------|------------------------------------------------------------------------------------------------------------------------------|--------------|
| C002           |                     | DOCUMENT/MESSAGE NAME Identification of a type of document/message by code or name. Code preferred                           | C            |
|                | 1001                | Document/message name, coded Document/message identifier expressed in code. 241 = Delivery schedule Usage of DELFOR-message. | C an..3      |
| C106           |                     | DOCUMENT/MESSAGE IDENTIFICATION Identification of a document/message by its number and eventually its version or revision.   | C            |
|                | 1004                | Document/message number Reference number assigned to the document/message by the issuer. Format: CCYYMMDDHHMMSS + SupplierID | C an..35     |
|                |                     | MESSAGE FUNCTION, CODED Code indicating the function of the message 5 = Replace Message replacing a previous message.        | C an..3      |

## Example:

BGM+241+20180807105820023270+5'

Last Saved :   Aug, 15 th  2018

## 3.3 Segment: DTM Date/Time/Period

| Position          | 0030                                                                                                                                                                                      |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Group             |                                                                                                                                                                                           |
| Level             | 1                                                                                                                                                                                         |
| Usage             | Mandatory                                                                                                                                                                                 |
| Max Use           | 10                                                                                                                                                                                        |
| Purpose           | The DTM segment shall be specified at least once to identify the Delivery schedule message date. This segment can be included to indicate the beginning and the end date of the schedule. |
| Dependency Notes: |                                                                                                                                                                                           |
| Semantic Notes:   |                                                                                                                                                                                           |
| Comments          |                                                                                                                                                                                           |

## Data Element Summary

|    | Data element   | Component Element   | Name                                                                                                                                                                                                                              | Attributes   |
|----|----------------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| M  | C507           |                     | DATE/TIME/PERIOD Date and/or time, or period relevant to the specified date/time/period type.                                                                                                                                     | M            |
| M  |                | 2005                | Date/time/period qualifier Code giving specific meaning to a date, time or period. 137 Document/message date/time (2006) Date/time when a document/message is issued. This may include authentication                             | Man..3       |
|    |                | 2380                | Date/time/period The value of a date, a date and time, a time or of a period in a specified representation.                                                                                                                       | C an..35     |
|    |                | 2379                | Date/time/period format qualifier Specification of the representation of a date, a date and time or of a period. 203 CCYYMMDDHHMMCalendar date including time with minutes: C=Century; Y=Year; M=Month; D=Day; H=Hour; M=Minutes. | C an..3      |

## Example:

DTM+137:201808071058:203'

Last Saved :   Aug, 15 th  2018

## Segment Group 2

## 3.4   Segment : NAD  Name and Address

| Position   | 0080                                                                                                                                           |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Group      |                                                                                                                                                |
| Level      | 1                                                                                                                                              |
| Usage      | Conditional (Optional)                                                                                                                         |
| Max Use    | 99                                                                                                                                             |
| Purpose    | A group of segments identifying parties by their names, addresses, locations, references and contacts relevant to the whole delivery schedule. |
| Comments   |                                                                                                                                                |

## Data Element Summary

|   Pos. | Segment ID   | Name             | Req. Desired   |   Max use | Group (repeat):   |
|--------|--------------|------------------|----------------|-----------|-------------------|
|   0090 | NAD          | Name and Address | M              |         1 |                   |

Last Saved :   Aug, 15 th  2018

## 3.4.1  Segment: NAD  Name and Address

| Position   | 0090 (Trigger Segment)                                                                                                                                                                                                                                                                                                                                                                           |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 2 (Name and Address) Conditional (Optional)                                                                                                                                                                                                                                                                                                                                        |
| Level      | 1                                                                                                                                                                                                                                                                                                                                                                                                |
| Usage      | Mandatory                                                                                                                                                                                                                                                                                                                                                                                        |
| Max Use    | 1                                                                                                                                                                                                                                                                                                                                                                                                |
| Purpose    | A segment for identifying names and addresses and their functions relevant for the whole Delivery schedule. The principal parties for the Delivery schedule message shall be identified. The identification of the recipient of the goods must be given in the NAD segment in the detail section. It is recommended that where possible only the coded form of the party ID should be specified. |
| Comments   |                                                                                                                                                                                                                                                                                                                                                                                                  |

## Data Element Summary

| Data element   | Component Element   | Name                                                                                                                                                                                                                                                                                                   | Attributes   |
|----------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| 3035           |                     | PARTY QUALIFIER . Code giving specific meaning to a party. BY Buyer (3002) Party to which merchandise is sold. SE Seller (3346) Party selling merchandise to a buyer. SU Supplier (3280) Party which manufactures or otherwise has possession of goods, and consigns or makes them available in trade. | M an..3      |
| C082           |                     | PARTY IDENTIFICATION DETAILS Identification of a transaction party by code.                                                                                                                                                                                                                            | C            |
|                | 3039                | Party id. Identification Code identifying a party involved in a transaction.                                                                                                                                                                                                                           | M an…35      |
|                | 1131                | Code list qualifier Identification of a code list. Refer to D.97A Data Element Dictionary for acceptable code values.                                                                                                                                                                                  | Not used     |
|                | 3055                | Code list responsible agency, coded Code identifying the agency responsible for a code list. Refer to D.97A Data Element Dictionary for acceptable code values 92 Assigned by buyer or buyer's agent                                                                                                   | C an..3      |
| C080           |                     | PARTY NAME Identification of a transaction party by name, one to five lines. Party name may be formatted                                                                                                                                                                                               | C            |
|                | 3036                | Party name Name of a party involved in a transaction.                                                                                                                                                                                                                                                  | M an..35     |
| C059           |                     | STREET Street address and/or PO Box number in a structured address: one to three lines.                                                                                                                                                                                                                | C            |
|                | 3042                | Street and number/p.o. box Street and number in plain language, or Post Office Box No.                                                                                                                                                                                                                 | M an..35     |
| 3164           |                     | CITY NAME Name of a city for addressing purposes.                                                                                                                                                                                                                                                      | C an..35     |
| 3229           |                     | COUNTRY SUB-ENTITY IDENTIFICATION Identification of the name of sub-entities (state, province) defined by appropriate governmental agencies.                                                                                                                                                           | C an..9      |

Last Saved :   Aug, 15 th  2018

|   Data element | Component Element   | Name                                                                                                          | Attributes   |
|----------------|---------------------|---------------------------------------------------------------------------------------------------------------|--------------|
|           3251 |                     | POSTCODE IDENTIFICATION Code defining postal zones or addresses.                                              | C an..9      |
|           3207 |                     | COUNTRY, CODED Identification of the name of a country or other geographical entity as specified in ISO 3166. | C an..3      |

## Example:

NAD+SU+23270::92' NAD+BY+45::92+BOSAL CZ, spol. s r.o'

## Segment Group 6

## 3.5 Segment: GIS  General Indicator

| Position   | 0190                                                                                                                                                                 |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 6 (General Indicator) Conditional (Optional)                                                                                                           |
| Level      | 1                                                                                                                                                                    |
| Usage      | Conditional (Optional)                                                                                                                                               |
| Max Use    | 9999                                                                                                                                                                 |
| Purpose    | A group of segments providing details on delivery points and products and related information using one of both scheduling methods (as described in 1.3 Principles). |
| Comments   |                                                                                                                                                                      |

## Data Element Summary

|   Position No. | Segment ID   | Name                              | Req. Desired   | Max use   | Group (repeat):   |
|----------------|--------------|-----------------------------------|----------------|-----------|-------------------|
|           0200 | GIS          | General Indicator                 | M              | 1         |                   |
|           0210 |              | Segment Group 7: Name and Address | C              |           | 1                 |
|           0370 |              | Segment Group 12: Line Item       | C              |           | 9999              |

## 3.5.1  Segment: GIS  General Indicator

| Position   | 0200 (Trigger Segment)                                                          |
|------------|---------------------------------------------------------------------------------|
| Group      | Segment Group 6 (General Indicator) Conditional (Optional)                      |
| Level      | 1                                                                               |
| Usage      | Conditional (Optional)                                                          |
| Max Use    | 1                                                                               |
| Purpose    | A segment to indicate which method is used by the relevant processing indicator |
| Comments   |                                                                                 |

## Data Element Summary

| Data element   | Component Element   | Name                                                                                                                     | Attributes   |
|----------------|---------------------|--------------------------------------------------------------------------------------------------------------------------|--------------|
| C529           |                     | PROCESSING INDICATOR Type of process indication.                                                                         | M            |
|                | 7365                | Processing indicator, coded Identifies the value to be attributed to indicators required by the processing system.       | M an..3      |
|                |                     | 37 Complete information Processing of information to note that complete data details (not just changes) are transmitted. |              |

## Example:

GIS+37'

Last Saved :   Aug, 15 th  2018

## Segment Group 7

## 3.6 Segment: NAD  Name and Address

| Position   | 0210                                                                                                                         |
|------------|------------------------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 6 (General Indicator) Conditional (Optional)                                                                   |
| Level      | 2                                                                                                                            |
| Usage      | Conditional (Optional)                                                                                                       |
| Max Use    | 1                                                                                                                            |
| Purpose    | A group of segments needed to identify a delivery point and its attached information when the delivery point method is used. |
| Comments   |                                                                                                                              |

## Data Element Summary

|   Position No. | Segment ID   | Name             | Req. Desired   |   Max use | Group (repeat):   |
|----------------|--------------|------------------|----------------|-----------|-------------------|
|           0220 | NAD          | Name and Address | M              |         1 |                   |

Last Saved :   Aug, 15 th  2018

## 3.6.1  Segment: NAD  Name and Address

| Position   | 0220 (Trigger Segment)                                    |
|------------|-----------------------------------------------------------|
| Group      | Segment Group 7 (Name and Address) Conditional (Optional) |
| Level      | 2                                                         |
| Usage      | Mandatory                                                 |
| Max Use    | 1                                                         |
| Purpose    | A segment for identifying the consignee.                  |
| Comments   |                                                           |

## Data Element Summary

| Group   | Data/ Component Element   | Name                                                                                                                                                            | Attributes   | Example         |
|---------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|-----------------|
| 010     | 3035                      | PARTY QUALIFIER Code giving specific meaning to a party. ST Ship to Identification of the party to where goods will be or have been shipped.                    | M an..3      | ST              |
| 020     | C082                      | PARTY IDENTIFICATION DETAILS Identification of a transaction party by code.                                                                                     | C            |                 |
|         | 3039                      | Party id. Identification Code identifying a party involved in a transaction.                                                                                    | M an..35     | 022001          |
|         | 1131                      | Code list qualifier Identification of a code list. Refer to D.97A Data Element Dictionary for acceptable code values.                                           | N an..3      |                 |
|         | 3055                      | Code list responsible agency, coded Code identifying the agency responsible for a code list. Refer to D.97A Data Element Dictionary for acceptable code values. | C an..3      | 92              |
| 030     | C058                      | NAME AND ADDRESS Unstructured name and address: one to five lines.                                                                                              | C            |                 |
|         | 3124                      | Name and address line Free form name and address description.                                                                                                   | M an..35     | BOSAL:BELGIUM   |
| 040     | C080                      | PARTY NAME Identification of a transaction party by name, one to five lines. Party name may be formatted.                                                       | C            |                 |
|         | 3036                      | Party name Name of a party involved in a transaction.                                                                                                           | M an..35     | Czech Warehouse |
| 050     | C059                      | STREET Street address and/or PO Box number in a structured address: one to three lines.                                                                         | C            |                 |
|         | 3042                      | Street and number/p.o. box Street and number in plain language, or Post Office Box No.                                                                          | M an..35     | Dellestraat 20  |
| 060     | 3164                      | CITYNAME Name of a city (a town, a village) for addressing purposes.                                                                                            | C an..35     |                 |
| 070     | 3229                      | COUNTRY SUB-ENTITY IDENTIFICATION Identification of the name of sub-entities (state, province) defined by appropriate governmental agencies.                    | C an..9      | 48              |
| 080     | 3251                      | POSTCODE IDENTIFICATION Code defining postal zones or addresses.                                                                                                | C an..9      | 603004          |
| 090     | 3207                      | COUNTRY, CODED Identification of the name of a country or other geographical entity as specified in ISO 3166.                                                   | C an..3      | RU              |

Example: Example:

GIS+37' NAD+ST+BCZB::92++BOSAL CZ, spol. s r.o++Brandys nad Labem+++CZ'

Last Saved :   Aug, 15 th  2018

## Segment Group 12

## 3.7  Segment: LIN Line Item

| Position   | 0370                                                                                 |
|------------|--------------------------------------------------------------------------------------|
| Group      | Segment Group 6 (General Indicator) Conditional (Optional)                           |
| Level      | 2                                                                                    |
| Usage      | Conditional (Optional)                                                               |
| Max Use    | 9999                                                                                 |
| Purpose    | A group of segments providing details of the individual line items for both methods. |
| Comments   |                                                                                      |

## Data Element Summary

|   Position No. | Segment ID   | Name                                    | Req. Desired   |   Max use | Group (repeat):   |
|----------------|--------------|-----------------------------------------|----------------|-----------|-------------------|
|           0380 | LIN          | Line Item                               | M              |         1 |                   |
|           0400 | IMD          | Item Description                        | C              |        10 |                   |
|           0450 | LOC          | Place/Location Identification           | C              |       999 |                   |
|           0480 |              | Segment Group 13: Reference             | C              |        10 |                   |
|           0540 |              | Segment Group 15: Quantity              | C              |        10 |                   |
|           0600 |              | Segment Group 17: Scheduling Conditions | C              |       999 |                   |

Last Saved :   Aug, 15 th  2018

## 3.7.1  Segment: LIN Line Item

| Position   | 0380 (Trigger Segment)                                                                                                                                                                               |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 12 (Line Item) Conditional (Optional)                                                                                                                                                  |
| Level      | 2                                                                                                                                                                                                    |
| Usage      | Mandatory                                                                                                                                                                                            |
| Max Use    | 1                                                                                                                                                                                                    |
| Purpose    | A segment identifying the details of the product or service to be delivered, e.g. product identification. All other segments in the detail section following the LIN segment refer to the line item. |
| Comments   |                                                                                                                                                                                                      |

## Data Element Summary

| Data element   | Component Element   | Name                                                                                       | Attributes   |
|----------------|---------------------|--------------------------------------------------------------------------------------------|--------------|
| 1082           |                     | LINE ITEM NUMBER Serial number designating each separate item within a series of articles. | C an..6      |
| C212           |                     | ITEM NUMBERIDENTIFICATION Goods identification for a specified source.                     | C            |
|                | 7140                | Item number A number allocated to a group or item.                                         | C an..35     |
|                | 7143                | Item number type, coded Identification of the type of item number. IN Buyer's item number  | C an..3      |

## Example:

LIN+3++00002612:IN'

Last Saved :   Aug, 15 th  2018

## 3.7.2  Segment: PIA Product Additional Information

| Position   | 0390                                                                                                                                                                                                 |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 12 (Line Item) Conditional (Optional)                                                                                                                                                  |
| Level      | 2                                                                                                                                                                                                    |
| Usage      | Mandatory                                                                                                                                                                                            |
| Max Use    | 1                                                                                                                                                                                                    |
| Purpose    | A segment identifying the details of the product or service to be delivered, e.g. product identification. All other segments in the detail section following the LIN segment refer to the line item. |
| Comments   | For LN &JDE plants the ' Product Additional Information ' is not used !                                                                                                                              |

## Data Element Summary

| Data element   | Component Element   | Name                                                                                         | Attributes   |
|----------------|---------------------|----------------------------------------------------------------------------------------------|--------------|
| 4347           |                     | PRODUCT ID, FUNCTION QUALIFIER Indication of the function of the product code.               | C an..6      |
| C212           |                     | ITEM NUMBERIDENTIFICATION Goods identification for a specified source.                       | C            |
|                | 7140                | Item number A number allocated to a group or item.                                           | C an..35     |
|                | 7143                | Item number type, coded Identification of the type of item number. SA Supplier's item number | C an..3      |

## Example:

PIA+1+1050020563:SA'

Last Saved :   Aug, 15 th  2018

## 3.7.3  Segment: IMD Item Description

| Position         | 0400                                                                                                                                                                         |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Group            | Segment Group 12 (Line Item) Conditional (Optional)                                                                                                                          |
| Level            | 2                                                                                                                                                                            |
| Usage            | Conditional (Optional)                                                                                                                                                       |
| Max Use          | 10                                                                                                                                                                           |
| Purpose          | A segment for describing the product or the service to be delivered. This segment should be used for products that cannot be identified by a product code or article number. |
| Dependency Notes |                                                                                                                                                                              |
| Semantic Notes   |                                                                                                                                                                              |
| Comments         | For the IFS plant, the ' Item Description ' is not used !                                                                                                                    |

## Data Element Summary

|    | Data element   | Component Element   | Name                                                                 | Attributes   |
|----|----------------|---------------------|----------------------------------------------------------------------|--------------|
|    | C273           |                     | ITEM DESCRIPTION Description of an item.                             | C            |
| X  |                | 7009                | Item description identification                                      | C an..17     |
|    |                | 7008                | Item description Plain language description of articles or products. | C an..35     |
|    |                | 7008                | Item description Plain language description of articles or products. | C an..35     |

Example:

IMD+++:::Tube B'

Last Saved :   Aug, 15 th  2018

## 3.7.4  Segment: LOC Place/Location Identification

| Position   | 0450                                                                                                                                                                                                          |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 12 (Line Item) Conditional (Optional)                                                                                                                                                           |
| Level      | 2                                                                                                                                                                                                             |
| Usage      | Conditional (Optional)                                                                                                                                                                                        |
| Max Use    | 9999                                                                                                                                                                                                          |
| Purpose    | A segment identifying a specific location to which products, as specified in the LIN-Segment group, should be placed after delivery. This function should only be used with the delivery point driven method. |
| Comments   |                                                                                                                                                                                                               |

## Data Element Summary

| Data element   | Component Element   | Name                                                                                                                                                                                                                                                                                    | Attributes   |
|----------------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
|                | 3227                | PLACE/LOCATION QUALIFIER Code identifying the function of a location. 11 Place/port of discharge (3392 + 3414) Seaport, airport, freight terminal, rail station or other place at which the goods (cargo) are unloaded from the means of transport having been used for their carriage. | C an..3      |
| C517           |                     | LOCATION IDENTIFICATION Identification of a location by code or name.                                                                                                                                                                                                                   | C            |
|                | 3225                | Place/location identification Identification of the name of place/location, other than 3164 City name.                                                                                                                                                                                  | C an..25     |

Example:

LOC+11+BCZB'

Last Saved :   Aug, 15 th  2018

## Segment Group 13

## 3.8  Segment: RFF Reference

| Position   | 0480                                                                                             |
|------------|--------------------------------------------------------------------------------------------------|
| Group      | Segment Group 12 (Line Item) Conditional (Optional)                                              |
| Level      | 3                                                                                                |
| Usage      | Conditional (Optional)                                                                           |
| Max Use    | 10                                                                                               |
| Purpose    | A group of segments giving references related to the line item and where necessary, their dates. |
| Comments   |                                                                                                  |

## Data Element Summary

|    |   Position No. | Segment ID   | Name             | Req. Desired   |   Max use | Group (repeat):   |
|----|----------------|--------------|------------------|----------------|-----------|-------------------|
| M  |           0490 | RFF          | Reference        | M              |         1 |                   |
|    |           0500 | DTM          | Date/Time/Period | C              |         1 |                   |

## 3.8.1  Segment: RFF Reference

| Position   | 0490 (Trigger Segment)                                                                                                                                                             |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 13 (Reference) Conditional (Optional)                                                                                                                                |
| Level      | 3                                                                                                                                                                                  |
| Usage      | Conditional (Optional)                                                                                                                                                             |
| Max Use    | 1                                                                                                                                                                                  |
| Purpose    | A segment for identifying references to the line item, e.g. a contract and its appropriate line item, original message number, previous message number if different per line item. |
| Comments   | For LN &JDE plants neither the ' Delivery Schedule Number ' nor the ' Previous Delivery Instruction Number ' are used !                                                            |

## Data Element Summary

| Data element   | Component Element   | Name                                                                                                                                                                                                                                                                                   | Attributes   |
|----------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| C506           |                     | REFERENCE Identification of a reference.                                                                                                                                                                                                                                               | M            |
|                | 1153                | REFERENCE QUALIFIER Code giving specific meaning to a reference segment or a reference number. AAN Delivery Schedule Number Reference number assigned by buyer to a delivery schedule. AIF Previous Delivery Instruction Number The identification of a previous delivery instruction. | Man..3       |
|                | 1154                | Reference number Identification number the nature and function of which can be qualified by an entry in data element 1153 Reference qualifier.                                                                                                                                         | C an..35     |

Example:

RFF+AAN:55'

RFF+AIF:32'

Last Saved :   Aug, 15 th  2018

## 3.8.2  Segment: DTM Date/Time/Period

| Position   | 0500                                                                               |
|------------|------------------------------------------------------------------------------------|
| Group      | Segment Group 13 (Reference) Conditional (Optional)                                |
| Level      | 3                                                                                  |
| Usage      | Conditional (Optional)                                                             |
| Max Use    | 1                                                                                  |
| Purpose    | Date/time/period of the reference.                                                 |
| Comments   | For LN &JDE plants neither the ' Date/Time/Period ' of the REFERENCE is not used ! |

## Data Element Summary

|    | Data element   | Component Element   | Name                                                                                                                                                                              | Attributes   |
|----|----------------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| M  | C507           |                     | DATE/TIME/PERIOD Date and/or time, or period relevant to the specified date/time/period type.                                                                                     | M            |
| M  |                | 2005                | Date/time/period qualifier Code giving specific meaning to a date, time or period. 171 Reference date/time Date/time on which the reference was issued.                           | Man..3       |
|    |                | 2380                | Date/time/period The value of a date, a date and time, a time or of a period in a specified representation.                                                                       | C an..35     |
|    |                | 2379                | Date/time/period format qualifier Specification of the representation of a date, a date and time or of a period. 102 CCYYMMDD Calendar date: C = Century Y = Year M=Month D = Day | C an..3      |

## Example:

DTM+171:20180801:102'

Last Saved :   Aug, 15 th  2018

## Segment Group 15

## 3.9  Segment: QTY Quantity

| Position   | 0540                                                                                                                            |
|------------|---------------------------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 12 (Line Item) Conditional (Optional)                                                                             |
| Level      | 3                                                                                                                               |
| Usage      | Conditional (Optional)                                                                                                          |
| Max Use    | 10                                                                                                                              |
| Purpose    | A group of segments specifying product quantities and associated dates not related to schedules and where relevant, references. |
| Comments   |                                                                                                                                 |

## Data Element Summary

|   Position No. | Segment ID   | Name             | Req. Desired   |   Max use | Group (repeat):   |
|----------------|--------------|------------------|----------------|-----------|-------------------|
|           0550 | QTY          | Quantity         | M              |         1 |                   |
|           0560 | DTM          | Date/Time/Period | C              |         2 |                   |

Last Saved :   Aug, 15 th  2018

## 3.9.1  Segment: QTY Quantity

| Position   | 0550 (Trigger Segment)                                                                                                   |
|------------|--------------------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 15 (Quantity) Conditional (Optional)                                                                       |
| Level      | 3                                                                                                                        |
| Usage      | Mandatory                                                                                                                |
| Max Use    | 1                                                                                                                        |
| Purpose    | A segment to specify pertinent quantities not related to schedule(s) e.g. cumulative quantity, last quantity considered. |
| Comments   |                                                                                                                          |

## Data Element Summary

|    | Data element   | Component Element   | Name                                                                                                                                                                                                                                                                                                                                         | Attributes   |
|----|----------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| M  | C186           |                     | QUANTITY DETAILS Quantity information in a transaction, qualified when relevant.                                                                                                                                                                                                                                                             | M            |
| M  |                | 6063                | Quantity qualifier Code giving specific meaning to a quantity. 70 Cumulative quantity received Cumulative quantity of all deliveries of this article received by the buyer. 79 Previous cumulative quantity Cumulative quantity prior the actual order. 83 Backorder quantity 194 Received and accepted Quantity which has been received and | Man..3       |
| M  |                | 6060                | Quantity Numeric value of a quantity.                                                                                                                                                                                                                                                                                                        | Mn..15       |
|    |                | 6411                | Measure unit qualifier Indication of the unit of measurement in which weight (mass), capacity, length, area, volume or other quantity is expressed.                                                                                                                                                                                          | C an..3      |

## Example:

QTY+194:7700:PCE'

QTY+70:21199:PCE'

Last Saved :   Aug, 15 th  2018

## 3.9.2  Segment: DTM Date/Time/Period

| Position   | 0560                                                                                                                                       |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 15 (Scheduling Conditions) Conditional (Optional)                                                                            |
| Level      | 3                                                                                                                                          |
| Usage      | Mandatory                                                                                                                                  |
| Max Use    | 1                                                                                                                                          |
| Purpose    | A segment specifying the status of the schedule. Optionally a delivery pattern can be established, e.g. firm or proposed delivery pattern. |
| Comments   |                                                                                                                                            |

## Data Element Summary

| Position   | 0560                                                                        |
|------------|-----------------------------------------------------------------------------|
| Group      | Segment Group 15 (Quantity) Conditional (Optional)                          |
| Level      | 4                                                                           |
| Usage      | Conditional (Optional)                                                      |
| Max Use    | 2                                                                           |
| Purpose    | A segment indicating the date/time/period details relating to the quantity. |
| Comments   |                                                                             |

## Data Element Summary

|    | Data element   | Component Element   | Name                                                                                                                                                                                    | Attributes   |
|----|----------------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| M  | C507           |                     | DATE/TIME/PERIOD Date and/or time, or period relevant to the specified date/time/period type.                                                                                           | M            |
| M  |                | 2005                | Date/time/period qualifier Code giving specific meaning to a date, time or period. 51 Cumulative quantity start date First Date for accumulation of delivery quantities. 2 Backlog Date | Man..3       |
|    |                | 2380                | Date/time/period The value of a date, a date and time, a time or of a period in a specified representation.                                                                             | C an..35     |
|    |                | 2379                | Date/time/period format qualifier Specification of the representation of a date, a date and time or of a period. 102 CCYYMMDD Calendar date: C = Century Y = Year M= Month D = Day      | C an..3      |

## Example:

DTM+51:20171213:102'

DTM+2:20190531:102'

Last Saved :   Aug, 15 th  2018

## Segment Group 16

## 3.10  Segment: RFF Reference

| Position   | 0570                                                                                           |
|------------|------------------------------------------------------------------------------------------------|
| Group      | Segment Group 16 (Line Item) Conditional (Optional)                                            |
| Level      | 4                                                                                              |
| Usage      | Conditional (Optional)                                                                         |
| Max Use    | 10                                                                                             |
| Purpose    | A group of segments giving references related to the quantity and where necessary, their date. |
| Comments   |                                                                                                |

## Data Element Summary

|    |   Position No. | Segment ID   | Name             | Req. Desired   |   Max use | Group (repeat):   |
|----|----------------|--------------|------------------|----------------|-----------|-------------------|
| M  |           0580 | RFF          | Reference        | M              |         1 |                   |
|    |           0590 | DTM          | Date/Time/Period | C              |         1 |                   |

## 3.10.1  Segment: RFF Reference

| Position   | 0580 (Trigger Segment)                                                            |
|------------|-----------------------------------------------------------------------------------|
| Group      | Segment Group 16 (Reference) Conditional (Optional)                               |
| Level      | 3                                                                                 |
| Usage      | Conditional (Optional)                                                            |
| Max Use    | 4                                                                                 |
| Purpose    | A segment for identifying reference to the quantity, e.g. despatch advice number. |
| Comments   | For JDE & IFS plants the dispatch advice number is not used!                      |

## Data Element Summary

| Data element   | Component Element   | Name                                                                                                                                                                                       | Attributes   |
|----------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| C506           |                     | REFERENCE Identification of a reference.                                                                                                                                                   | M            |
|                | 1153                | REFERENCE QUALIFIER Code giving specific meaning to a reference segment or a reference number. AAU Despatch note number [1128] Reference number assigned by the seller to a Despatch Note. | Man..3       |
|                | 1154                | Reference number Identification number the nature and function of which can be qualified by an entry in data element 1153 Reference qualifier.                                             | C an..35     |

## Example:

RFF+AAU:DN1041180628-02'

Last Saved :   Aug, 15 th  2018

## 3.10.2  Segment: DTM Date/Time/Period

| Position          | 0590                                                |
|-------------------|-----------------------------------------------------|
| Group             | Segment Group 16 (Reference) Conditional (Optional) |
| Level             | 4                                                   |
| Usage             | Conditional (Optional)                              |
| Max Use           | 1                                                   |
| Purpose           | Date/time/period of the reference.                  |
| Dependency Notes: |                                                     |
| Semantic Notes:   |                                                     |
| Comments          |                                                     |

## Data Element Summary

|    | Data element   | Component Element   | Name                                                                                                                                                                              | Attributes   |
|----|----------------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| M  | C507           |                     | DATE/TIME/PERIOD Date and/or time, or period relevant to the specified date/time/period type.                                                                                     | M            |
| M  |                | 2005                | Date/time/period qualifier Code giving specific meaning to a date, time or period. 171 Reference date/time Date/time on which the reference was issued.                           | Man..3       |
|    |                | 2380                | Date/time/period The value of a date, a date and time, a time or of a period in a specified representation.                                                                       | C an..35     |
|    |                | 2379                | Date/time/period format qualifier Specification of the representation of a date, a date and time or of a period. 102 CCYYMMDD Calendar date: C = Century Y = Year M=Month D = Day | C an..3      |

## Example:

DTM+171:20180628:102'

Last Saved :   Aug, 15 th  2018

## Segment Group 17

## 3.11  Segment: SCC Scheduling Conditions

| Position   | 0600                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 12 (Line Item) Conditional (Optional)                                                                                                                                                                                                                                                                                                                                                              |
| Level      | 3                                                                                                                                                                                                                                                                                                                                                                                                                |
| Usage      | Conditional (Optional)                                                                                                                                                                                                                                                                                                                                                                                           |
| Max Use    | 999                                                                                                                                                                                                                                                                                                                                                                                                              |
| Purpose    | A group of segments specifying the schedule information for the product identified in the LIN segment. With the delivery point driven method this segment group provides the schedule for the identified delivery point and product. With the product driven method this segment group can be used to summarize all schedules provided with the subsequent delivery point information given in segment group 22. |
| Comments   |                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Data Element Summary

|   Position No. | Segment ID   | Name                       | Req. Desired   | Max use   | Group (repeat):   |
|----------------|--------------|----------------------------|----------------|-----------|-------------------|
|           0610 | SCC          | Scheduling Conditions      | M              | 1         |                   |
|           0620 |              | Segment Group 18: Quantity | C              |           | 999               |

Last Saved :   Aug, 15 th  2018

## 3.11.1 Segment: SCC Scheduling Conditions

| Position   | 0610 (Trigger Segment)                                                                                                                     |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 17 (Scheduling Conditions) Conditional (Optional)                                                                            |
| Level      | 3                                                                                                                                          |
| Usage      | Mandatory                                                                                                                                  |
| Max Use    | 1                                                                                                                                          |
| Purpose    | A segment specifying the status of the schedule. Optionally a delivery pattern can be established, e.g. firm or proposed delivery pattern. |
| Comments   |                                                                                                                                            |

## Data Element Summary

| Data element   | Component Element   | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Attributes   |
|----------------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| 4017           |                     | DELIVERY PLAN STATUS INDICATOR, CODED Code indicating the level of commitment of schedule information. 1 Firm Indicates that the scheduling information is a firm commitment. 10 Immediate Indicates that the scheduling information is for immediate execution (backlog) 4 Planning/forecast Self-explanatory                                                                                                                                                        | M an..3      |
| C329           |                     | PATTERN DESCRIPTION Shipment, delivery or production interval pattern and timing.                                                                                                                                                                                                                                                                                                                                                                                     | C            |
|                | 2013                | Frequency, coded Code specifying interval grouping of the delivery, production, etc. of the schedule D Discrete Flexible frequency according to planning process. Y Daily Code defining a forecast for daily intervals W Weekly Code defining a forecast for weekly intervals. M Monthly Code defining a forecast for monthly intervals. F Flexible interval (from date X through date Y) Code defining a forecasted usage that is planned between two defined dates. | C an..3      |

Example:

SCC+1++Y' SCC+4++M'

Last Saved :   Aug, 15 th  2018

## Segment Group 18

## 3.12  Segment: QTY Quantity

| Position   | 0620                                                                    |
|------------|-------------------------------------------------------------------------|
| Group      | Segment Group 17 (Scheduling Conditions) Conditional (Optional)         |
| Level      | 4                                                                       |
| Usage      | Conditional (Optional)                                                  |
| Max Use    | 999                                                                     |
| Purpose    | A group of segments specifying product quantities and associated dates. |
| Comments   |                                                                         |

## Data Element Summary

|   Position No. | Segment ID   | Name             | Req. Desired   |   Max use | Group (repeat):   |
|----------------|--------------|------------------|----------------|-----------|-------------------|
|           0630 | QTY          | Quantity         | M              |         1 |                   |
|           0640 | DTM          | Date/Time/Period | C              |         2 |                   |

## 3.12.1 Segment: QTY Quantity

| Position   | 0630 (Trigger Segment)                                                                                                                                                               |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 18 (Quantity) Conditional (Optional)                                                                                                                                   |
| Level      | 4                                                                                                                                                                                    |
| Usage      | Mandatory                                                                                                                                                                            |
| Max Use    | 1                                                                                                                                                                                    |
| Purpose    | A segment to specify scheduled quantities which may be related to schedule(s) and, or pattern established in the following DTM segment, e.g. delivery quantity for a specified date. |
| Comments   |                                                                                                                                                                                      |

## Data Element Summary

| Data element   | Component Element   | Name                                                                                                                                                          | Attributes   |
|----------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
|                | C186                | QUANTITY DETAILS Quantity information in a transaction, qualified when relevant.                                                                              | M            |
| 6063           |                     | Quantity qualifier Code giving specific meaning to a quantity. 113 Quantity to be delivered The quantity to be delivered.                                     | M an…3       |
| 6060           |                     | Quantity Numeric value of a quantity.                                                                                                                         | M n…15       |
| 6411           |                     | Measure unit qualifier Indication of the unit of measurement in which weight (mass), capacity, length, area, volume or other quantity is expressed. PCE Piece | C an…3       |

## Example:

QTY+113:8400:PCE'

Last Saved :   Aug, 15 th  2018

## 3.12.2 Segment: DTM Date/Time/Period

| Position   | 0640                                                                          |
|------------|-------------------------------------------------------------------------------|
| Group      | Segment Group 18 (Quantity) Conditional (Optional)                            |
| Level      | 5                                                                             |
| Usage      | Conditional (Optional)                                                        |
| Max Use    | 2                                                                             |
| Purpose    | A segment indicating date/time/period details relating to the given quantity. |
| Comments   |                                                                               |

## Data Element Summary

|    | Data Element   | Component Element   | Name                                                                                                                                                                                     | Attributes   |
|----|----------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| M  | C507           |                     | DATE/TIME/PERIOD Date and/or time, or period relevant to the specified date/time/period type.                                                                                            | M            |
| M  |                | 2005                | Date/time/period qualifier Code giving specific meaning to a date, time or period. 2 Delivery date/time, requested Date on which buyer requests goods to be delivered.                   | Man..3       |
|    |                | 2380                | Date/time/period The value of a date, a date and time, a time or of a period in a specified                                                                                              | C an..35     |
|    |                | 2379                | Date/time/period format qualifier Specification of the representation of a date, a date and time or of a period. 102 CCYYMMDD Calendar date: C = Century ; Y = Year ; M=Month ; D = Day. | C an..3      |

## Example:

DTM+2:20181001:102'

## Remarks

:

For Weekly (W), Monthly (M) &amp; Flexible (F) demands, this date means the starting date of the period.

Last Saved :   Aug, 15 th  2018

## Segment Group 20

## 3.13  Segment: PAC Package

| Position   | 0680                                                                                                                                             |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 20 (Package) Conditional (Optional)                                                                                                |
| Level      | 3                                                                                                                                                |
| Usage      | Conditional (Optional)                                                                                                                           |
| Max Use    | 99                                                                                                                                               |
| Purpose    | A group of segments identifying the packaging, physical dimensions, and marks and numbers for goods referenced in the line item to be delivered. |
| Comments   |                                                                                                                                                  |

## Data Element Summary

|   Position No. | Segment ID   | Name    | Req. Desired   |   Max use | Group (repeat):   |
|----------------|--------------|---------|----------------|-----------|-------------------|
|           0690 | PAC          | Package | M              |         1 |                   |

## 3.13.1 Segment: PAC Package

| Position   | 0690                                                                                                       |
|------------|------------------------------------------------------------------------------------------------------------|
| Group      | Segment Group 20 (Quantity) Conditional (Optional)                                                         |
| Level      | 3                                                                                                          |
| Usage      | Conditional (Optional)                                                                                     |
| Max Use    | 1                                                                                                          |
| Purpose    | A segment specifying the number of package units and the type of packaging for the line item, e.g. pallet. |
| Comments   | For LN &JDE plants the ' Package Information ' is not used !                                               |

## Data Element Summary

|    | Data Element   | Component Element   | Name                                                                                                                                                                | Attributes   |
|----|----------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
|    |                | 7224                | NUMBER OF PACKAGES Number of individual parts of a shipment either unpacked, or packed in such a way that they cannot be divided without first undoing the packing. | C            |
| M  | C202           |                     | PACKAGE TYPE Type of package by name or by code from a specified source.                                                                                            | C            |
|    |                | 7065                | Types of Packages Identification Coded description of the form in which goods are presented.                                                                        | C an..35     |

## Example:

PAC+700++CB (1200 x 1000)'

Last Saved :   Aug, 15 th  2018

## 3.12 Segment: UNT Message Trailer

| Position   | 1030                                                                                                                                   |
|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Group      |                                                                                                                                        |
| Level      | 0                                                                                                                                      |
| Usage      | Mandatory                                                                                                                              |
| Max Use    | 1                                                                                                                                      |
| Purpose    | A service segment ending a message, giving the total number of segments in the message and the control reference number of the message |
| Comments   |                                                                                                                                        |

## Data Element Summary

|    |   Data Element | Component Element   | Name                                                                              | Attributes   |
|----|----------------|---------------------|-----------------------------------------------------------------------------------|--------------|
| M  |           0074 |                     | NUMBER OF SEGMENTS IN A MESSAGE Control count of number of segments in a message. | Mn..6        |
| M  |           0062 |                     | MESSAGE REFERENCE NUMBER Unique message reference assigned by the sender.         | Mn..14       |

## Example:

UNT+31+1'

Last Saved :   Aug, 15 th  2018

- 4 Example message (LN Plant)

UNB+UNOC:1+O0013BOSALSFID+O0013TESTSUPPLIER+140113:1435+4' UNH+1+DELFOR:D:97A:UN' BGM+241+020000004+5' DTM+137:201401131634:203' NAD+SU+000000005::92++Test Supplier GmbH' NAD+BY+BOSAL::92' GIS+37' NAD+ST+022001::92+:+Raw Material++Nizhny Novgorod+48++RU' LIN+1++1150022821:IN' IMD+++:::Tube B' LOC+11+027101' RFF+ON:020000001' QTY+70:0:PCE' DTM+51:20130903:102' SCC+1++D' QTY+113:1002:PCE' DTM+2:20131106:102' SCC+1++D' QTY+113:25:PCE' DTM+2:20131109:102' SCC+1++D' QTY+113:25:PCE' DTM+2:20131121:102' UNT+23+1' UNZ+1+4'

## 5 Example message (JDE Plant)

UNB+UNOC:1+OSENDER:OD+ORECEIVER:OD+160519:1722+13' UNH+1+DELFOR:D:97A:UN' BGM+241+201605121208050944+5' DTM+137:201605121408:203' NAD+SU+50944::92' NAD+BY+00045::92++BOSAL CZ, spol. s r.o.' GIS+37' NAD+ST+BCZB::92++BOSAL CZ, spol. s r.o.++Brandys nad Labem Brandys nad Labem+++CZ ' LIN+3++2550020320:IN' IMD+++:::KLAPPEELEKTRISCH-4H0253691H' LOC+11+BCZB' RFF+ON:460' SCC+1++D' QTY+113:120:PCE' DTM+2:20160520:102' SCC+10++D' QTY+113:27:PCE' DTM+2:20160401:102' SCC+4++D' QTY+113:0:PCE' DTM+2:20160613:102' SCC+4++D' QTY+113:0:PCE' DTM+2:20160620:102' UNT+24+1' UNZ+1+13'

## 6 Example message (IFS Plant)

UNB+UNOA:1+O01770000000000A04CBCZB:OD+O0942CZ2713180740001ACM:OD+180814:0742+74' UNH+1+DELFOR:D:97A:UN' BGM+241+20180807105820023270+5' DTM+137:201808071058:203' NAD+SU+23270::92' NAD+BY+45::92+BOSAL CZ, spol. s r.o' GIS+37' NAD+ST+BCZB::92++BOSAL CZ, spol. s r.o++Brandys nad Labem+++CZ' LIN+3++00002612:IN' PIA+1+1050020563:SA' LOC+11+BCZB' RFF+ON:000001' RFF+AAN:55' DTM+171:20180801:102' RFF+AIF:32' DTM+171:20180701:102' QTY+194:7700:PCE' RFF+AAU:DN1041180628-02' DTM+171:20180628:102' QTY+70:21199:PCE' DTM+51:20171213:102' SCC+4++M' QTY+113:8400:PCE' DTM+2:20180801:102' SCC+4++M' QTY+113:9100:PCE' DTM+2:20180903:102' SCC+4++M' QTY+113:2100:PCE' DTM+2:20181001:102' PAC+700++CB (1200 x 1000)' UNT+31+1' UNZ+1+74'

Last Saved :   Aug, 15 th  2018