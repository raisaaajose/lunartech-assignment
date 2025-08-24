import numpy as np
import pandas as pd

np.random.seed(42)
n = 500
diagnosis = np.random.binomial(1, 0.3, n)

# assuming 40% of cases are early stage (stage I-III) 
early_stage_mask = (diagnosis == 1) & (np.random.rand(n) < 0.4) 
brca = np.random.binomial(1, np.where(diagnosis == 1, 0.3, 0.1), n)

#age skews younger for BRCA+ cancer diagnosed cases
age = np.random.normal(50, 10, n)
age = np.where(brca == 1,
               np.random.normal(45, 8, n),  # younger age distribution
               np.random.normal(52, 10, n))
age=np.clip(age,20,90).astype(int)

#menopausal status flexible as in real-life
menopause = np.random.binomial(1,
                    np.where(age > 60, 1.0,
                    np.where(age > 50, 0.95,
                    np.where(age > 40,0.65, 0.0))),n)

#tumor size also depends on stage of cancer
tumor_size = np.where(diagnosis == 1,
                    np.random.normal(6, 1.5, n),
                    np.random.normal(3, 0.8, n))
tumor_size[early_stage_mask] -= np.random.normal(1.5, 1.0, early_stage_mask.sum()) #additive subtraction to prevent overwriting of existing values
tumor_size=np.clip(tumor_size,0,12).astype(int)

#CA-125 high base values, correlated with tumor size
ca125 = tumor_size * 30 + np.random.normal(0, 50, n)  # smaller noise to keep closer to tumor size

# For diagnosed patients, center around higher values with variability
ca125 = np.where(diagnosis == 1,
                 ca125,  # linked to tumor size + noise
                 np.random.normal(15, 10, n))


# young, BRCA+ populations secrete less CA-125 at early stage levels (Source: Dochez et al., 2019 (BMC Ovarian Research); Nature Reviews)
low_ca125_mask = (diagnosis == 1) & (age < 45) & (brca == 1) 
ca125[low_ca125_mask] -= np.random.normal(80, 30, low_ca125_mask.sum())

#early stage populations also secrete less CA-125 based on stage,specifically which early stage
subtraction_choices = np.random.choice([30, 40, 50], size=early_stage_mask.sum(), p=[1/3, 1/3, 1/3])
ca125[early_stage_mask] -= np.random.normal(loc=subtraction_choices, scale=5, size=early_stage_mask.sum())

ca125 = np.clip(ca125, 5, 1000).astype(int) #can reach 1000+

#US Score based on stage of cancer
us_score = np.where(diagnosis == 1,
                    np.random.normal(0.7, 0.2, n),
                    np.random.normal(0.3, 0.2, n))
us_score[early_stage_mask] -= np.random.normal(0.1, 0.05, early_stage_mask.sum())
us_score = np.clip(us_score, 0, 1)

#family history 15% likely to exist among patients with cancer
family_history = np.random.binomial(1, np.where(diagnosis == 1, 0.15, 0.05), n)

df = pd.DataFrame({
    'Age': age,
    'CA125': ca125,
    'TumorSize': tumor_size.round(1),
    'BRCA': brca,
    'Menopausal': menopause,
    'USScore': us_score.round(1),
    'FamilyHistory': family_history,
    'Diagnosis': diagnosis
})

df.to_csv('synthetic_clinical_dataset.csv', index=False)