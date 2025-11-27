# IMAGE REPLACEMENT GUIDE

## ⚠️ CURRENT STATUS: PLACEHOLDER BOXES + RESTORED REFERENCES

Your LaTeX should now compile with restored vital references. All image references have been replaced with placeholder boxes that show exactly where each image should go.

## 📸 IMAGES TO ADD

Replace these placeholder boxes with your actual images by placing the files in `/latex_cs_thesis/images/`:

### 1. **Theoretical Architecture** 
- **File**: `images/theoretical_architecture.png` (or .jpg)
- **Location**: Chapter 3 - Theoretical Framework
- **Description**: Comprehensive diagram showing theory evolution to platform integration

### 2. **User Flow Diagram**
- **File**: `images/user_flow.png` (or .jpg) 
- **Location**: Chapter 3 - Materials and Methods
- **Description**: Complete interaction pathway from auth to analytics

### 3. **System Architecture Overview**
- **File**: `images/system_overview.png` (or .jpg)
- **Location**: Chapter 3 - Materials and Methods 
- **Description**: Simplified system components overview

### 4. **SimCSE Architecture** ⭐ NEW
- **File**: `images/simcse_architecture.png` (or .jpg)
- **Location**: Chapter 4 - Methodology 
- **Description**: Detailed SimCSE processing pipeline (your attached diagram)

### 5. **Detailed Tech Stack Architecture** ⭐ NEW
- **File**: `images/tech_stack_architecture.png` (or .jpg)
- **Location**: Chapter 4 - Methodology (Full Page)
- **Description**: Comprehensive technology integration diagram

## 🔧 TO ACTIVATE IMAGES

1. Place your image files in `/latex_cs_thesis/images/` with the exact names above
2. Replace the placeholder `\fbox{\begin{minipage}...` sections with:
   ```latex
   \includegraphics[width=\textwidth]{images/filename}
   ```

## ✅ RESTORED VITAL REFERENCES

- ✅ `fig:theoretical_matrix` - Back in theoretical framework
- ✅ `fig:simcse_test_cases` - Restored for test cases
- ✅ `table:threshold_validation` - Restored for validation results
- ✅ Added `fig:simcse_architecture` - For your SimCSE diagram
- ✅ Added `fig:tech_stack_architecture` - For detailed tech stack

## 🎯 NEXT STEPS

1. **Add your SimCSE architecture image** (the one you attached) as `simcse_architecture.png`
2. **Create/add tech stack diagram** as `tech_stack_architecture.png` 
3. **Add other image files** to `/images/` folder
4. **Replace placeholder code** with actual `\includegraphics` commands
5. **Recompile** to see your images

The original TikZ/mermaid code is saved in:
- `saved_theoretical_architecture_mermaid.txt`
- `saved_userflow_mermaid.txt`