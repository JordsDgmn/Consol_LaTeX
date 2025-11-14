# Consol Thesis - LaTeX Version

This repository contains the LaTeX source files for the **Consol: A Notes-to-Recollection Application Using SimCSE for its Textual Semantic Comparison** thesis.

## 📁 Structure

```
FinalPaper_Latex/
├── latex_cs_thesis/           # Main LaTeX project
│   ├── cs_thesis_main.tex     # Main compilation file
│   ├── frontmatter/           # Title page, abstract, TOC, etc.
│   ├── chap1/                 # Introduction
│   ├── chap2/                 # Literature Review  
│   ├── chap3/                 # Theoretical Framework
│   ├── chap4/                 # Methodology
│   ├── chap5/                 # Results and Discussion
│   ├── chap6/                 # Conclusions
│   ├── appA/, appB/, appC/    # Appendices
│   └── images/                # Figures and diagrams
├── nawawi_reference_thesis/   # ClassiFish reference (approved format)
└── Documentation/             # Guides and checklists
```

## 🔧 Compilation

To compile the thesis:

```bash
cd latex_cs_thesis
pdflatex cs_thesis_main.tex
pdflatex cs_thesis_main.tex  # Run twice for TOC and references
```

Or use LaTeX Workshop extension in VS Code for live preview.

## 📋 Progress Tracking

- ✅ **Structure Setup** - Matches ClassiFish approved format
- ✅ **LaTeX Packages** - All essential packages added
- ✅ **Chapter Framework** - All 6 chapters created
- 🔄 **Content Development** - In progress
- ⏳ **Testing Phase** - Planned for next week

## 📚 Key Features

- **Theoretical Framework** - Academic foundation for approach
- **Methodology** - Research and development methodology  
- **Results & Discussion** - Implementation and validation results
- **Progress Tracking** - Terminology updated per professor feedback
- **Comprehensive RRL** - 15+ references with gap analysis

## 🎯 Thesis Focus

**Consol** - A web-based learning application that uses SimCSE semantic similarity to evaluate memory recall, featuring:
- Real-time similarity scoring (0-1 scale → 0-3 stars)
- Progress tracking and learning analytics
- Next.js 15 + React 19 + PostgreSQL architecture
- Comprehensive user experience testing

## 📖 University Requirements

- **Format**: University of Malta LaTeX template
- **Length**: Target 80-120 pages (ClassiFish reference ~100 pages)
- **Structure**: 6 chapters + appendices + comprehensive bibliography
- **Timeline**: Testing phase week of Nov 18, final submission TBD

---

*This thesis documents the development and validation of an innovative semantic similarity-based learning platform.*