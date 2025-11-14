# TESTING METHODOLOGY & DOCUMENTATION GUIDE
*Complete guide for similarity fairness testing and UX evaluation*

## 🧪 **TEST 1: SIMILARITY SCORING FAIRNESS**

### **Methodology Design:**
**Comparative Analysis Approach**
- **Participants:** 1 teacher, 3-4 students of varying levels
- **Content:** Same educational material (choose 2-3 topics)
- **Comparisons:** Teacher vs Student, Student vs ChatGPT, Student vs Consol, ChatGPT vs Consol

### **Testing Protocol:**
1. **Content Selection:** Choose 2-3 academic topics (different complexity levels)
2. **Reference Creation:** Teacher provides "gold standard" content summary
3. **Response Generation:**
   - Students write summaries (handwritten → typed)
   - ChatGPT generates summaries (controlled prompts)
   - Consol processes student recall sessions
4. **Scoring Comparison:**
   - Manual teacher scoring (1-10 scale)
   - SimCSE/Consol automatic scoring (0-1 scale)
   - Convert scores to common scale for comparison

### **Data Collection Sheet:**
```
Content Topic: _______________
Reference Text: [Teacher's gold standard]

Participant Type | Response Text | Manual Score (1-10) | Consol Score (0-1) | Normalized Scores
Teacher          | [text]        | N/A                 | [score]            | N/A
Student 1        | [text]        | [score]             | [score]            | [comparison]
Student 2        | [text]        | [score]             | [score]            | [comparison]
ChatGPT          | [text]        | [score]             | [score]            | [comparison]
```

### **Analysis Approach:**
- **Correlation Analysis:** Pearson correlation between manual and automatic scores
- **Bias Detection:** Check if system consistently over/under-scores certain participant types
- **Threshold Validation:** Verify 30%, 60%, 81% cutoffs align with teacher expectations

---

## 👥 **TEST 2: USER EXPERIENCE TESTING**

### **Participant Selection:**
- **College Student (1):** Advanced academic writing experience
- **Senior High Students (2):** Moderate academic experience
- **High School Student (1):** Basic academic experience  
- **Teacher (1):** Professional educational perspective

### **Testing Protocol (45-60 minutes per participant):**

#### **Phase 1: Orientation (5 minutes)**
- Brief Consol explanation (without bias)
- Account setup and initial login
- No detailed tutorial (test intuitiveness)

#### **Phase 2: Guided Tasks (20 minutes)**
**Task Sequence:**
1. **Create a note** (provide sample content)
2. **Start a study session** (attempt recall)
3. **Review performance metrics** (understand dashboard)
4. **Navigate to profile** (explore analytics)
5. **Try different features** (settings, help modal)

#### **Phase 3: Free Exploration (10 minutes)**
- Let participants explore independently
- Observe behavior, note confusion points
- No intervention unless they're completely stuck

#### **Phase 4: Questionnaire (10 minutes)**
**Google Forms Questions:**

### **UX QUESTIONNAIRE STRUCTURE:**

#### **Usability Assessment (1-5 Likert Scale)**
1. The interface was easy to understand
2. I could complete tasks without confusion
3. The system response time was acceptable
4. The performance feedback was clear and helpful
5. The navigation was intuitive

#### **Feature-Specific Questions**
6. How useful was the star rating system? (1-5)
7. Did the similarity scoring seem accurate? (1-5)
8. Would you use this app for your studies? (1-5)
9. How would you rate the overall user experience? (1-5)

#### **Open-Ended Questions**
10. What did you find most confusing about the app?
11. What features did you find most valuable?
12. What would you change or improve?
13. How does this compare to your current study methods?
14. Additional comments or suggestions?

#### **Demographic Questions**
15. Age: ___
16. Education Level: ___
17. Technology comfort level (1-5): ___
18. Current study apps used: ___

### **Observation Data Collection:**
**Create observation sheet for each participant:**
```
Participant ID: _____ (College/SHS/HS/Teacher)
Date: _____

Task Completion Times:
- Note Creation: ___ seconds
- Session Start: ___ seconds  
- Performance Review: ___ seconds
- Profile Navigation: ___ seconds

Confusion Points Observed:
- [timestamp] [description]
- [timestamp] [description]

Positive Reactions:
- [timestamp] [description]
- [timestamp] [description]

Technical Issues:
- [timestamp] [description]

Overall Impression: ___/5
```

---

## 📊 **DOCUMENTATION FOR THESIS**

### **Chapter 4: Testing and Validation**

#### **Section 4.1: Similarity Scoring Validation**
**Content Structure:**
1. **Testing Methodology** (describe protocol)
2. **Participant Demographics** (teacher + student profiles)
3. **Data Collection Process** (reference materials, scoring procedures)
4. **Results Analysis** (correlation coefficients, bias assessment)
5. **Threshold Validation** (alignment with human judgment)

#### **Section 4.2: User Experience Evaluation**
**Content Structure:**
1. **Study Design** (participant selection criteria)
2. **Testing Protocol** (task sequence, observation methods)
3. **Quantitative Results** (Likert scale analysis, completion times)
4. **Qualitative Findings** (thematic analysis of open responses)
5. **Usability Assessment** (overall experience ratings)

### **Required Tables/Figures:**

#### **Table 4.1: Similarity Scoring Comparison**
| Participant | Manual Score | Consol Score | Difference | Normalized Correlation |
|-------------|--------------|--------------|------------|----------------------|
| Teacher     | N/A          | 0.85         | N/A        | N/A                  |
| Student 1   | 7.5/10       | 0.73         | -0.02      | 0.87                 |
| [etc...]    | [data]       | [data]       | [data]     | [data]               |

#### **Table 4.2: User Experience Metrics**
| Metric                    | Mean Score | Std Dev | Range |
|---------------------------|------------|---------|-------|
| Interface Clarity         | 4.2/5      | 0.8     | 3-5   |
| Task Completion Ease      | 3.8/5      | 1.1     | 2-5   |
| Performance Feedback      | 4.0/5      | 0.9     | 3-5   |
| Overall Experience        | 4.1/5      | 0.7     | 3-5   |

#### **Figure 4.1: Scoring Correlation Analysis**
- Scatter plot: Manual scores vs Consol scores
- Show correlation coefficient and trend line

#### **Figure 4.2: User Experience Distribution**
- Bar chart of Likert scale responses by question
- Show participant type breakdown

### **Statistical Analysis Required:**
- **Pearson correlation** for scoring validation
- **Descriptive statistics** for UX metrics  
- **Thematic coding** for qualitative responses
- **Inter-rater reliability** if multiple evaluators

---

## ⏰ **TIMELINE FOR NEXT WEEK**

### **Preparation (Before Testing):**
- [ ] Finalize test content topics
- [ ] Create Google Forms questionnaire  
- [ ] Prepare observation sheets
- [ ] Set up testing environment
- [ ] Recruit participants (start ASAP)

### **Testing Week Schedule:**
- **Day 1-2:** Similarity fairness testing
- **Day 3-5:** UX testing (1 participant per day)
- **Day 6-7:** Data analysis and initial writeup

### **Post-Testing (Following Week):**
- [ ] Complete statistical analysis
- [ ] Write Chapter 4 content
- [ ] Create required tables and figures
- [ ] Integrate results into conclusions

---

*This testing approach provides both technical validation and user-centered evaluation, strengthening your thesis significantly.*