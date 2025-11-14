# OFFICIAL THESIS STRUCTURE - APPLIED RESEARCH

## **Document Outline and Contents for Applied Research**

### **Front Matter**
- Title Page
- Adviser's Recommendation Sheet
- Panel's Approval Sheet*
- College Acceptance Sheet*
- Acknowledgement*
- Abstract
- Table of Contents
- List of Tables
- List of Figures

### **1.0 Research Description**
- **1.1** Overview of the Current State of Technology *(Thesis Proposal 1.1)*
- **1.2** Statement of the Problem *(Thesis Proposal 1.2)*
- **1.3** Research Objectives
  - **1.3.1** General Objective *(Thesis Proposal 1.3.1)*
  - **1.3.2** Specific Objectives *(Thesis Proposal 1.3.2)*
- **1.4** Scope and Limitations of the Research *(Thesis Proposal 1.4)*
- **1.5** Significance of the Research *(Thesis Proposal 1.5)*

### **2.0 Review of Related Literature**

### **3.0 Research Methodology**
**NOTE:** Based on Chapter 3 of the Thesis Proposal, but modified to reflect what was actually done while developing the project. Part of the contents is lifted from Chapter 2 of the Thesis Proposal. Additional materials gathered during the thesis stages must also be included. **Maximum 10 pages.**

### **4.0 Theoretical Framework**
Discusses relevant theories and concepts used in designing or developing the thesis. Include only those concepts that are needed. Do not copy whole source material. Use topics from Thesis Proposal Research Objectives as guide.

### **5.0 The [System Name] System**
Overall specifications and functional requirements of the software developed.

- **5.1 System Overview**
  - Overall view of main features and capabilities of the software

- **5.2 System Objectives**
  - Specific requirements that must be met by the system

- **5.3 System Scope and Limitations**
  - Discusses scope and limitations (level of capability/extent of power) of each major function
  - Operations beyond identified limits will be invalidated/ignored with error messages
  - Include justifications for limitations and assumptions
  - Assumptions = conditions that must be satisfied for system to function properly

- **5.4 Architectural Design**
  - Initial internal design of the system
  - Major components and their interactions
  - Software components (modules, database systems, etc.)
  - Hardware components (processors, devices, etc.)
  - Graphical representation using design tools (hierarchical charts, structure charts, object models)
  - Data flow diagrams showing information flow among processes
  - Discussion on alternative choices and trade-offs

- **5.5 System Functions**
  - Listing of all functions performed/delivered by the system
  - Description of each function
  - Screen designs may be included
  - Functions usually based on menu and toolbar options
  - Include report formats if system generates reports

- **5.6 Physical Environment and Resources**
  - Hardware and software resources needed for implementation and execution
  - User specification if special target users (educational level, experience, technical expertise)
  - Discussion of why uncommon resources are necessary

### **6.0 Design and Implementation Issues**
- Design and implementation of major data structures and algorithms used
- Major issues and problems encountered
- Corresponding solutions and alternatives employed
- Parts of design tools from Technical Manual may be included as figures

### **7.0 Results and Observations**
- Analysis, interpretation and implications of summarized test results
- Observations on limits of system's capabilities
- Type(s) of testing performed on the system
- Test data used and results of tests

**Testing varies by system type:**
- Commissioned software: detailed acceptance test and system response time analysis
- Algorithm implementation: performance analysis on different machines/test data

### **8.0 Conclusion and Recommendations**
- Assessment of what happened in the project
- Explanations and justifications on how objectives were met
- To what extent and why some objectives were not met
- Discussion of possible improvements
- Future directions of research topic
- Serves as springboard for future thesis groups

### **Back Matter**
- **Bibliography** *(follow format in Thesis Proposal)*
- **Appendix A**
- **Appendix xxx**
- **Appendix (xxx)+1** Resource Persons *(follow format in Thesis Proposal)*
- **Appendix (xxx)+2** Personal Vitae *(follow format in Thesis Proposal)*
- **TECHNICAL MANUAL** *(see Chapter 5 of manual)*
- **USER'S MANUAL** *(see Chapter 6 of manual)*

---

## **IMPORTANT NOTES:**

1. **Items marked with *** are to be submitted in final (hardbound) document only
2. **Research Methodology** should reflect what was actually done, not just what was proposed
3. **Theoretical Framework** should only include concepts actually needed/used
4. **System chapter** should be comprehensive with detailed technical specifications
5. **Testing chapter** must match the type of system developed
6. **Conclusion** must directly address how objectives were met

---

## **MAPPING TO CURRENT LATEX STRUCTURE:**

| Official Structure | Current LaTeX File |
|-------------------|-------------------|
| 1.0 Research Description | `chap1/introduction_main.tex` |
| 2.0 Review of Related Literature | `chap2/lit_overview_main.tex` |
| 3.0 Research Methodology | `chap3/materials_and_methods_main.tex` |
| 4.0 Theoretical Framework | *May need new chapter or merge with chap2* |
| 5.0 The [System] System | `chap4/results_and_discussion_main.tex` |
| 6.0 Design and Implementation | `chap5/evaluation_main.tex` |
| 7.0 Results and Observations | *May need new chapter or merge with chap4* |
| 8.0 Conclusion | `chap6/conclusions_main.tex` |

---

**Reference Document Created:** `OFFICIAL_THESIS_STRUCTURE.md`
**Location:** `c:\Users\ASUS LAPTOP\Downloads\Thesis\FinalPaper_Latex\`