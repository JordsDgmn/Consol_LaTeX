# Semi-Final Revision Checklist

## Chapter Structure & Introduction Updates
- [ ] Write intros after every chapter number, before going into any subsection
- [ ] Remove any subsection x.1 that acts as an intro and place it above before the subsection x.1

## Chapter 4 Specific Changes

### 4.1 System Architecture Design
- [ ] Remove "basic" from "Basic System Architecture" (rename section 4.1.1)
- [ ] Change the word "layer" to "component" throughout
- [ ] User does not count as one of the five components - make it just 4 components (frontend, API, AI, database)
- [ ] In 4.1.2, use the proper titles from the diagram and not the ones made by AI

### 4.3 Semantic Comparison
- [ ] 4.3.2 must introduce the labelling of "A to D" also, after the figure introduction
- [ ] 4.3.2 must follow the exact flow of the diagram, numbered and explained per number
- [ ] Add more subsections under 4.3.2.x covering all SimCSE processes from pretraining to end result with threshold
- [ ] Somewhere in test case explanation, say that swapping S1 and S2 does not change the result
- [ ] Change 4.3.4 table 4.1 to say the original threshold given by ChatGPT
- [ ] Say somewhere in 4.3.4 or 4.3.x that the initial threshold was changed due to observed results
- [ ] Remember which test cases caused threshold adjustment and state it was arbitrary to the researcher
- [ ] Make another subsection back in 4.3 (SimCSE) that discusses the new range of scores being arbitrarily adjusted
- [ ] Explain table of test case results - example: Test 1 score is 0.89 because ~89% of sentence is similar, only colors different, SimCSE doesn't value correctness but similarity

### 4.4 Prototype Development
- [ ] Remove 4.4.3 since it doesn't make sense
- [ ] Remove 4.4.6 and its subsequent sections since prototype was not deployed
- [ ] Remove 4.4.8 since it's not in the architecture

### 4.5 Usability Testing
- [ ] 4.5.3.1 remove bold letters like "Experimental Design" etc.
- [ ] 4.5.4 has no introduction - please add one

## Chapter 5 Changes
- [ ] 5.2 is empty - find reference to start writing
- [ ] 5.1.1 shouldn't be bulleted - convert to paragraph form
- [ ] 5.1.3 looks weird - fix indentation and justify importance of subsection
- [ ] Key observations in table 5.1 must be in paragraph form
- [ ] Add key observations for figure 5.2 in paragraph form
- [ ] 5.3.4 must not be in bullets - make into table instead
- [ ] 5.9.1 and 5.9.3 must not be in bullets - convert to paragraph form

## Figure/Table/Diagram Requirements

### General Formatting
- [ ] Figure/table/diagram descriptions must be smaller than usual font used for body text
- [ ] All tables must have descriptions on top
- [ ] All figures must have descriptions below
- [ ] All figure/table descriptions must be aligned with the width of the table/figure itself

### Diagram-Specific Requirements
- [ ] Titles of diagram labels must be bold to separate from subtitles
- [ ] Use bounding boxes to enclose server side vs user side
- [ ] Make letters in line with title (except C.x and D because there's not enough space)
- [ ] Fix parentheses for all groups
- [ ] Let all diagram explanations follow the exact flow of the diagram - nothing unexplained or unmentioned

## Global Content Changes
- [ ] Remove all occurrences of the word "educational" and similar words as much as possible

## Status Tracking
- [ ] **Started:** ___/___/_____
- [ ] **Completed:** ___/___/_____
- [ ] **Reviewed:** ___/___/_____

---

## Notes Section
*Add any additional notes or observations during revision process here:*
