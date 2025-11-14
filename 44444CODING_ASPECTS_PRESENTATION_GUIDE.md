# CODING ASPECTS PRESENTATION GUIDE
*How to show technical implementation without overwhelming readers*

## 🎯 **WHAT CODE TO SHOW (Selective Approach)**

### **1. Core Algorithm Implementation** *(Priority 1)*
**SimCSE Integration Function:**
```javascript
// Show the similarity calculation logic (5-8 lines max)
const calculateSimilarity = async (text1, text2) => {
  const response = await fetch('/api/similarity', {
    method: 'POST',
    body: JSON.stringify({ text1, text2 })
  });
  return response.json();
};
```

### **2. Novel Star Rating Logic** *(Priority 2)*
**Show threshold implementation:**
```javascript
// Demonstrate the scoring algorithm (3-5 lines)
const getStars = (similarity) => {
  if (similarity >= 0.81) return 3;
  if (similarity >= 0.6) return 2;
  if (similarity >= 0.3) return 1;
  return 0;
};
```

### **3. Key Architecture Decisions** *(Priority 3)*
**Database schema or API endpoint structure (pseudocode acceptable)**

## ❌ **WHAT CODE NOT TO SHOW**
- Complete React components (too long)
- Standard CRUD operations (not novel)
- Basic HTML/CSS styling
- Third-party library implementations
- Boilerplate configuration files

## 📝 **DESCRIPTION-BASED APPROACH** *(Recommended)*

### **Instead of showing full code, describe:**

#### **Technical Architecture:**
*"The application employs a three-tier architecture with Next.js handling the presentation layer, Express.js managing business logic, and PostgreSQL providing data persistence. The similarity calculation integrates SimCSE embeddings through a dedicated API endpoint that processes text pairs and returns semantic similarity scores between 0 and 1."*

#### **Implementation Process:**
*"Development followed an iterative approach, beginning with core functionality implementation (note storage, user management) before progressing to advanced features (similarity calculation, analytics dashboard). Each component was developed using modern React patterns with hooks for state management and context for user session handling."*

#### **Algorithm Integration:**
*"The semantic similarity calculation leverages the SimCSE model through a Python backend service. User input text and reference content are converted to sentence embeddings, with cosine similarity calculated between vectors to determine semantic closeness. This score is then mapped to a four-tier star rating system with empirically determined thresholds."*

## 📊 **FORMATTING GUIDELINES**

### **When You Do Show Code:**
```latex
\lstset{
  language=JavaScript,
  style=jsstyle,  % Use the style we added to preamble
  caption={Similarity Scoring Implementation},
  label={lst:similarity}
}
\begin{lstlisting}
// Your 5-10 line code snippet here
\end{lstlisting}
```

### **Reference in Text:**
*"As shown in Listing \ref{lst:similarity}, the similarity calculation implements a straightforward threshold-based approach..."*

## 🎯 **CHAPTER PLACEMENT**

### **Chapter 3 (Methodology):**
- **Section 3.2:** System Architecture (describe overall structure)
- **Section 3.3:** Algorithm Implementation (show SimCSE integration)
- **Section 3.4:** Development Process (describe methodology, not code)

### **Chapter 4 (Implementation/Results):**
- **Section 4.1:** Core Features (describe functionality with minimal code)
- **Section 4.2:** Performance Optimization (results, not implementation)

## ✅ **BEST PRACTICES**
1. **Code snippets should be 10 lines maximum**
2. **Focus on YOUR novel contributions, not frameworks**
3. **Use pseudocode when actual code is too complex**
4. **Always explain WHY you made specific technical decisions**
5. **Emphasize problem-solving approach over syntax**

---

*Remember: Thesis readers want to understand your technical thinking, not debug your code.*