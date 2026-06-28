# Literature Review & Key Resources

Annotated bibliography for hockey player/goalie evaluation methodology.
Update this file as you read papers — add notes, key findings, and how each informs the project.

---

## 1. Foundational RAPM / Ridge Regression Papers

**Macdonald, B. (2011)**
"A Regression-Based Adjusted Plus-Minus Statistic for NHL Players"
- *Journal of Quantitative Analysis in Sports*
- THE foundational paper for hockey RAPM. Introduced ridge regression to
  control for teammates and opponents simultaneously. Start here.
- https://doi.org/10.2202/1559-0410.1323
- *Notes:* [ Add your notes after reading ]

**Gramacy, R.B., Jensen, S.T., & Taddy, M. (2013)**
"Estimating Player Contribution in Hockey with Regularization"
- *Journal of Quantitative Analysis in Sports*
- Extends Macdonald with better regularization choices and a Bayesian framing.
  Introduces a more principled approach to selecting the regularization parameter alpha.
- https://doi.org/10.1515/jqas-2012-0001
- *Notes:* [ Add your notes after reading ]

**Macdonald, B. (2012)**
"An Expected Goals Model for Evaluating NHL Teams and Players"
- *MIT Sloan Sports Analytics Conference*
- Early formalization of xG for hockey. Connects shot quality to the RAPM framework.
- *Notes:* [ Add your notes after reading ]

---

## 2. Expected Goals (xG) Methodology

**Schuckers, M. & Curro, J. (2013)**
"Total Hockey Rating (THoR): A comprehensive statistical rating of NHL forwards and defensemen"
- *RITHAC (Rochester Institute of Technology Hockey Analytics Conference)*
- Integrates shot quality (proto-xG) into a comprehensive player rating.
  Important precursor to modern xG + RAPM combinations.
- *Notes:* [ Add your notes after reading ]

**Pettigrew, S. (2015)**
"Assessing the offensive productivity of NHL players using in-game win probabilities"
- *MIT Sloan Sports Analytics Conference*
- Win probability framework — useful for thinking about how player actions
  connect to team outcomes rather than just counting stats.
- *Notes:* [ Add your notes after reading ]

**Moneypuck xG Methodology (Practitioner)**
- https://moneypuck.com/about.htm
- Best public documentation of a working xG model. Read the feature list
  and calibration approach carefully — this is the practical benchmark.
- *Notes:* [ Add your notes after reading ]

**Evolving Hockey xG & WAR Documentation (Practitioner)**
- https://evolving-hockey.com/about/
- Describes how they combine RAPM + xG to produce WAR. Key reference
  for understanding the current state of the art we aim to improve on.
- *Notes:* [ Add your notes after reading ]

---

## 3. Goalie Evaluation

**Evolving Hockey GSAx Methodology**
- https://evolving-hockey.com/about/
- Current best-practice goalie evaluation. Understand this deeply before
  proposing improvements — know what you're beating.
- *Notes:* [ Add your notes after reading ]

**Kuehn, J. (2016)**
"Accounting for complementary contributions in hockey"
- Addresses the teammate/defense adjustment problem directly.
  Central to the goalie-defense entanglement challenge.
- Search Google Scholar for full text.
- *Notes:* [ Add your notes after reading ]

---

## 4. Causal Inference & Contextual Adjustment

**Franks, A., Miller, A., Bornn, L., & Goldsberry, K. (2015)**
"Counterpoints: Advanced Defensive Metrics for NBA Basketball"
- *MIT Sloan Sports Analytics Conference*
- Spatial + contextual adjustment framework. Directly transferable to the
  problem of separating goalie performance from defensive structure.
- *Notes:* [ Add your notes after reading ]

---

## 5. Machine Learning Extensions

**Decroos, T. et al. (2019)**
"Actions Speak Louder Than Goals: Valuing Player Actions in Football"
- *KDD 2019*
- Not hockey, but the VAEP framework (valuing every on-ball action) is the
  best example of moving beyond shots to full action valuation.
  Directly relevant if we want to model all player contributions, not just shot-related ones.
- https://arxiv.org/abs/1802.07127
- *Notes:* [ Add your notes after reading ]

---

## 6. Conference Proceedings to Search Regularly

- **MIT Sloan Sports Analytics Conference (SSAC)**
  https://www.sloansportsconference.com/research/papers
  Annual — search for "hockey" or "NHL" in the paper archive

- **RITHAC (Rochester Institute of Technology Hockey Analytics Conference)**
  Search GitHub and Google Scholar for proceedings

- **Stathletes Big Data Cup**
  Open competition with real NHL tracking data and submitted methodology papers
  https://github.com/stathletes/big-data-cup

---

## 7. Practitioner Blogs & Resources

- **Hockey Graphs** — hockey-graphs.com
  Community blog with rigorous methodology posts; excellent archive
- **Evolving Hockey Blog** — evolving-hockey.com
  Methodology deep dives from the team behind the best public WAR model
- **HockeyViz (Micah Blake McCurdy)** — hockeyviz.com
  Spatial shot quality work; important for understanding shot location adjustments
- **Natural Stat Trick** — naturalstattrick.com
  Best free data explorer; useful for sanity-checking model outputs

---

## 8. General ML / Statistics References

**Hastie, T., Tibshirani, R., & Friedman, J. — "The Elements of Statistical Learning" (2nd ed.)**
- Chapter 3 (Linear Methods for Regression) is essential for understanding RAPM
- Free PDF: https://hastie.su.domains/ElemStatLearn/

**Murphy, K. — "Probabilistic Machine Learning: An Introduction" (2022)**
- Bayesian framing and uncertainty quantification — key for producing
  credible intervals on player ratings
- Free: https://probml.github.io/pml-book/

**James, G. et al. — "An Introduction to Statistical Learning" (ISLR)**
- More accessible than ESL; good for ridge regression intuition
- Free: https://www.statlearning.com/

---

## 9. Key Search Terms for Google Scholar

- "NHL adjusted plus-minus"
- "hockey expected goals model"
- "goalie performance evaluation stabilization"
- "ice hockey player rating regularization"
- "sports RAPM ridge regression"
- "hockey analytics player valuation"
- "NHL shot quality model"
