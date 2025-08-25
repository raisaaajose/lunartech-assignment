# Ovarian Cancer Synthetic Data Generation for BRCA+ population 
**Submission:** LunarTech Challenge  

## Project Overview  
This project simulates a synthetic dataset for ovarian cancer diagnosis modeling, based on domain research and literature-backed distributions. Key clinical factors were modeled to reflect realistic population-level statistics and disease characteristics.

---

## Domain Insights  

- **CA-125** is an important diagnostic biomarker but unreliable in early stages, especially in **BRCA+** and younger patients.  
- **Tumor size** correlates strongly with CA-125; both increase with disease severity.  
- **USScore**, **CA-125**, and **BRCA status** are the strongest predictors of diagnosis.  

### Diagnosis Generation  
To avoid overfitting, diagnosis status was fixed at **30% positive**, and biomarker values were modeled **based on diagnosis**, not the reverse.

### Feature Classification  
- **Risk Factors:** Age, Menopause, BRCA, Family History  
- **Symptoms:** Tumor Size, USScore  
- **Biomarker:** CA-125  

---

## Feature Modeling Summary

| Feature           | Unit     | Healthy Distribution       | Cancer Distribution              | Notes                                     |
|------------------|----------|----------------------------|----------------------------------|-------------------------------------------|
| **Age**          | years    | Normal(50, 10)             | Normal(50, 10)                   | BRCA+ patients tend to be younger         |
| **CA-125**       | U/mL     | Normal(20, 10)             | TumorSize * 30 + Normal(0, 20)   | Correlated with tumor size                |
| **Tumor Size**   | cm       | Normal(3, 0.8)             | Normal(6, 1.5)                   | Higher in diagnosed patients              |
| **BRCA**         | 0 / 1    | Binomial(1, 0.1)           | Binomial(1, 0.2)                 | More prevalent among diagnosed            |
| **Menopause**    | 0 / 1    | Age-based thresholds       | Age-based thresholds             | Reflects real menopause stats             |
| **USScore**      | 0–1      | Normal(0.3, 0.15)          | Normal(0.7, 0.15)                | Imaging-based diagnostic score            |
| **Family History** | 0 / 1  | Binomial(1, 0.15)          | Binomial(1, 0.05)                | Higher risk with family history           |
| **Diagnosis**    | 0 / 1    | 0                          | 1                                | 30% diagnosed population                  |

---

## Validation Highlights  

- **Avg Tumor Size:** ~3.1 cm (lower overall due to majority healthy population)  
- **Avg CA-125:** ~25.6 U/mL (premenopausal), ~37.2 U/mL (postmenopausal)  
- **Correlations:**  
  - CA-125 ↔ Tumor Size, USScore (strong)  
  - BRCA ↔ Age (negative)  
- **Key diagnostic indicators:** CA-125, Tumor Size, and USScore (CA-125 alone is insufficient)

---

## Literature References  

- BRCA diagnosis age:  
  - [PubMed](https://pubmed.ncbi.nlm.nih.gov/29793803/)  
  - [BMC Ovarian Research](https://ovarianresearch.biomedcentral.com/articles/10.1186/s13048-021-00809-w)  

- CA-125 levels:  
  - [PMC Article 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC10315033/)  
  - [PMC Article 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC7763876/)  

- Tumor size distribution:  
  - [PMC Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2815712/)

---
