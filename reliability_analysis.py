import pandas as pd
import numpy as np

# CSV 파일 불러오기
df = pd.read_csv("data/converted_data.csv")

# 신뢰도 분석용 함수 정의
def cronbach_alpha(df_subset):
    df_corr = df_subset.corr()
    n_items = len(df_subset.columns)
    avg_corr = df_corr.values[np.triu_indices(n_items, 1)].mean()
    alpha = (n_items * avg_corr) / (1 + (n_items - 1) * avg_corr)
    return round(alpha, 3)

# 공공봉사동기 (q30_1 ~ q30_6)
public_motivation = df[['q30_1', 'q30_2', 'q30_3', 'q30_4', 'q30_5', 'q30_6']]
alpha_public = cronbach_alpha(public_motivation)
print(f"✅ 공공봉사동기 Cronbach's Alpha: {alpha_public}")

# 정서적 거리감 (q31_1 ~ q31_7)
emotional_distance = df[['q31_1', 'q31_2', 'q31_3', 'q31_4', 'q31_5', 'q31_6', 'q31_7']]
alpha_emotion = cronbach_alpha(emotional_distance)
print(f"✅ 정서적 거리감 Cronbach's Alpha: {alpha_emotion}")

# 조직몰입 (q35_1 ~ q35_4)
org_commitment = df[['q35_1', 'q35_2', 'q35_3', 'q35_4']]
alpha_commitment = cronbach_alpha(org_commitment)
print(f"✅ 조직몰입 Cronbach's Alpha: {alpha_commitment}")

#공공봉사동기 Cronbach's Alpha: 0.902
#정서적 거리감 Cronbach's Alpha: 0.881
#조직몰입 Cronbach's Alpha: 0.868