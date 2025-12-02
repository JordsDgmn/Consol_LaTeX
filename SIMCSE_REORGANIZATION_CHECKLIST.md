# SimCSE Architecture Reorganization Checklist

## Primary Requirements (Verbatim from User):

- [ ] **The only subsections under 4.3.2.x will be the groups A to D**
  - [ ] 4.3.2.1 will be training phase
  - [ ] 4.3.2.2 will be local deployment phase  
  - [ ] 4.3.2.3 will be inference phase
  - [ ] 4.3.2.4 will be response phase

- [ ] **Section Title Rules:**
  - [ ] Do NOT mention the letter (A, B, C, D) in the section title
  - [ ] ONLY mention the letter in the section description

- [ ] **Section Description Requirements:**
  - [ ] In writing, mention that group A in the diagram starting from 1) and ending at 6)
  - [ ] Then start next subsection 4.3.2.2 local deployment phase, from 7) to 12)
  - [ ] Continue pattern until D

- [ ] **Writing Style Requirements:**
  - [ ] WITHOUT using dashing and colons and bolding
  - [ ] WITHOUT using \\paragraph on anything
  - [ ] Follow the flow of the diagram always
  - [ ] Use parenthesis numbers as an easy guide linking to the reference (1), (2), etc.

- [ ] **Content Integration:**
  - [ ] Parts like "4.3.2.1 encoder architecture design" can be tucked under appropriate section
  - [ ] Must follow the flow and be injected with references like numbering in accordance to diagram flow
  - [ ] IF content becomes redundant and only repeats what is written in main subsections for groups A-D, then COMMENT OUT these sections instead
  - [ ] This applies to: encoder design, temperature config

- [ ] **Stopping Point:**
  - [ ] Stop at 4.3.3 simcse implementation and scoring
  - [ ] This is a dedicated separate section for discussing how we got the scoring thresholds

## Implementation Plan:

### 4.3.2.1 Training Phase
- [ ] Mention "group A in the diagram starting from 1) and ending at 6)"
- [ ] Cover steps (1) through (6) with parenthetical references
- [ ] Integrate encoder architecture design content if not redundant, otherwise comment out

### 4.3.2.2 Local Deployment Phase  
- [ ] Mention "group B in the diagram from 7) to 12)"
- [ ] Cover steps (7) through (12) with parenthetical references

### 4.3.2.3 Inference Phase
- [ ] Mention "group C in the diagram" with appropriate step range
- [ ] Cover tokenization, model forward pass, embedding extraction
- [ ] Use parenthetical references for all steps

### 4.3.2.4 Response Phase
- [ ] Mention "group D in the diagram" 
- [ ] Cover similarity computation, scoring, response generation
- [ ] Use parenthetical references for all steps
- [ ] Integrate temperature parameter content if not redundant, otherwise comment out

## Content to Evaluate for Integration or Commenting Out:
- [ ] Encoder architecture design section
- [ ] Temperature parameter configuration section
- [ ] Any other existing subsections that may be redundant

## Final Check:
- [ ] Ensure no \\paragraph usage
- [ ] Ensure no dashing, colons, bolding in inappropriate places
- [ ] Verify all parenthetical number references match diagram
- [ ] Confirm flow follows diagram exactly
- [ ] Stop before 4.3.3 simcse implementation and scoring