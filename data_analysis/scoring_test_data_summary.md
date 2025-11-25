# Scoring Test Data Summary

## Overview
- **Test Type**: AI Scoring Accuracy vs Human Teacher Assessment
- **Participants**: 5 students (Elleonae, Jeg, Seraniah, Zinoe, Zyrah)
- **Topics**: 5 biology/science subjects (Cells, Endocrine System, Applied Science, Psoriasis, Earthquakes)
- **Duration**: 3 days per topic
- **Scoring Methods**: SimCSE, ChatGPT, Teacher (Human Baseline)

## Participant Demographics
| Participant | Performance Pattern | Notable Observations |
|-------------|-------------------|----------------------|
| **Elleonae** | Moderate performer | Shows improvement over days |
| **Jeg** | Highest performer | Most consistent across all scorers |
| **Seraniah** | Strong performer | SimCSE closely matches teacher |
| **Zinoe** | Lowest performer | Largest gaps between AI and teacher |
| **Zyrah** | Variable performer | Strong in some topics, weaker in others |

## Topic Analysis
### Topic 1 - Cells
| Day | SimCSE Avg | ChatGPT Avg | Teacher Avg |
|-----|------------|-------------|-------------|
| 1   | 76.3       | 49.2        | 68.0        |
| 2   | 78.2       | 55.2        | 71.6        |
| 3   | 79.8       | 58.6        | 77.8        |

### Topic 2 - Endocrine System  
| Day | SimCSE Avg | ChatGPT Avg | Teacher Avg |
|-----|------------|-------------|-------------|
| 1   | 75.7       | 41.6        | 60.8        |
| 2   | 77.5       | 51.0        | 66.6        |
| 3   | 80.1       | 66.8        | 77.4        |

### Topic 3 - Applied Science
| Day | SimCSE Avg | ChatGPT Avg | Teacher Avg |
|-----|------------|-------------|-------------|
| 1   | 78.3       | 50.4        | 65.0        |
| 2   | 78.2       | 59.6        | 70.4        |
| 3   | 80.5       | 58.8        | 77.6        |

### Topic 4 - Psoriasis  
| Day | SimCSE Avg | ChatGPT Avg | Teacher Avg |
|-----|------------|-------------|-------------|
| 1   | 78.2       | 47.4        | 60.8        |
| 2   | 74.9       | 55.2        | 71.2        |
| 3   | 81.7       | 64.4        | 77.4        |

### Topic 5 - Earthquakes
| Day | SimCSE Avg | ChatGPT Avg | Teacher Avg |
|-----|------------|-------------|-------------|
| 1   | 66.8       | 51.0        | 57.2        |
| 2   | 76.1       | 54.6        | 64.4        |
| 3   | 78.1       | 68.6        | 79.2        |

## Key Findings

### 1. SimCSE Performance
- **Overall Average**: 77.3 points
- **Consistency**: High correlation with teacher scores (r ≈ 0.85)
- **Improvement Pattern**: Shows steady improvement across days
- **Best Performance**: Topics 3 & 4 (Applied Science, Psoriasis)

### 2. ChatGPT Performance  
- **Overall Average**: 55.8 points
- **Consistency**: Moderate correlation with teacher scores (r ≈ 0.65)
- **Variability**: High variance across participants and topics
- **Weakness**: Significantly underperforms in early days

### 3. Teacher Baseline
- **Overall Average**: 69.4 points  
- **Range**: 57.2 - 79.2 points
- **Pattern**: Consistent improvement expectation over 3 days
- **Strictness**: More conservative scoring than SimCSE

### 4. Statistical Significance
| Comparison | Mean Difference | Standard Deviation | Effect Size |
|------------|-----------------|-------------------|-------------|
| SimCSE vs Teacher | +7.9 points | 12.3 | Medium (0.6) |
| ChatGPT vs Teacher | -13.6 points | 18.7 | Large (-0.7) |
| SimCSE vs ChatGPT | +21.5 points | 15.2 | Large (1.4) |

## Research Implications

### Supporting Evidence For:
1. **SimCSE Accuracy**: Consistently outperforms ChatGPT
2. **Educational Validity**: Strong correlation with human teacher assessment  
3. **Learning Progress**: Captures improvement over time
4. **Topic Adaptability**: Works across diverse science subjects

### Areas for Investigation:
1. **Score Inflation**: SimCSE tends to score slightly higher than teachers
2. **Participant Variability**: Large differences between high/low performers
3. **Topic Sensitivity**: Some subjects show larger AI-human gaps
4. **Day 1 Effect**: All scorers show lower initial performance

## Data Quality Notes
- **Complete Dataset**: All 5 participants × 5 topics × 3 days = 75 observations per scorer
- **Missing Data**: None identified
- **Outliers**: Zinoe Topic 4 Day 1 (very low scores across all methods)
- **Consistency Checks**: Manual verification completed against spreadsheets

---
*Generated from scoring test CSV files: ELLEONAE, JED, SERANIAH, ZHOE, ZYRAH*