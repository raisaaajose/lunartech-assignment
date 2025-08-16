import numpy as np 
import pandas as pd 

np.random.seed(42)

n_samples=500

cancer_rate=0.3
n_cancer=int(n_samples*cancer_rate)
n_healthy=n_samples-n_cancer

#creating all columns

Diagnosis=np.array([1]*n_cancer+[0]*n_healthy)
np.random.shuffle(Diagnosis)

Age=np.random.normal(loc=55,scale=10,size=n_samples).clip(20,90)

BMI=np.random.normal(loc=26,scale=4,size=n_samples).clip(15,45)

#to fix:make menopausal status more flexible
Menopausal=np.where(Age>=50,1,0)

BRCA_rate=0.2
n_BRCA=int(n_samples*BRCA_rate)
BRCA=np.array([1]*n_BRCA+[0]*(n_samples-n_BRCA))
np.random.shuffle(BRCA)

ca125 = np.zeros(n_samples)

for i in range(n_samples):
    if Diagnosis[i] == 1:
        ca125[i] = np.random.normal(100, 50) if np.random.rand() < 0.85 else np.random.normal(20, 10)
        
    else:
        ca125[i] = np.random.normal(20, 10) if np.random.rand() < 0.90 else np.random.normal(60, 20)
        
df = pd.DataFrame({
    'Diagnosis': Diagnosis,
    'Age': Age.round(),
    'BMI': BMI.round(1),
    'menopausal_status': Menopausal,
    'CA125': ca125.round(1),
})

df.to_csv('generated.csv', index=False)