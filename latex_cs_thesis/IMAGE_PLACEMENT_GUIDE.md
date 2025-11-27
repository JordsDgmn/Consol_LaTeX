# Image Figure Placement Guide

## Required Images to Place in /images/ folder:

### 1. **theoretical_architecture.png/jpg**
- **Location**: Chapter 3 - theoretical_architecture_fig.tex
- **Figure**: First image (theoretical architecture diagram)
- **Caption**: Comprehensive theoretical architecture showing evolution from research domains through Consol implementation
- **Size**: Full width (\textwidth)

### 2. **user_flow.png/jpg**
- **Location**: Chapter 3 - materials_and_methods_main.tex (around line 30)
- **Figure**: Second image (detailed user flow)
- **Caption**: Complete user flow with authentication, note management, sessions, and analytics
- **Size**: Full width (\textwidth)

### 3. **system_architecture.png/jpg**
- **Location**: Chapter 4 - methodology.tex (full page figure)
- **Figure**: Third image (master system architecture)
- **Caption**: Complete technology stack from frontend through database and AI services
- **Size**: Full page (width=\textwidth, height=0.9\textheight, keepaspectratio)

### 4. **system_overview.png/jpg** (optional)
- **Location**: Chapter 3 - materials_and_methods_main.tex (sys_arch figure)
- **Figure**: Simplified overview version of system architecture
- **Caption**: Overview of main system components and interactions
- **Size**: 85% width (0.85\linewidth)

## Saved Placeholder Code:
- **saved_theoretical_architecture_mermaid.txt**: Original TikZ → Mermaid conversion
- **saved_userflow_mermaid.txt**: Original user flow diagrams → Mermaid conversion
- **multipage_userflow_placeholder.tex**: Blank placeholder for phase-based diagrams

## Files Modified:
1. **chap3/theoretical_architecture_fig.tex**: Replaced TikZ with image reference
2. **chap3/materials_and_methods_main.tex**: Updated both user flow and system overview figures
3. **chap4/methodology.tex**: Added full-page system architecture figure
4. **multipage_userflow_*.tex**: Content cleared, placeholders created

## Next Steps:
1. Place the corresponding image files in the `/images/` folder
2. Ensure image names match the references above
3. Compile LaTeX to verify figure placement
4. Decide whether to keep or remove the blank phase placeholders