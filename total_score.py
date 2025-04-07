import pandas as pd

# CSV 파일 로드
df = pd.read_csv("data/converted_data.csv")

# 각 요인에 해당하는 문항들
public_service_motivation = ['q30_1', 'q30_2', 'q30_3', 'q30_4', 'q30_5', 'q30_6']
emotional_distance = ['q31_1', 'q31_2', 'q31_3', 'q31_4', 'q31_5', 'q31_6', 'q31_7']
organizational_commitment = ['q35_1', 'q35_2', 'q35_3', 'q35_4']

# 결측치 무시하고 평균 점수 계산
df['psm_score'] = df[public_service_motivation].mean(axis=1)
df['emotional_distance_score'] = df[emotional_distance].mean(axis=1)
df['commitment_score'] = df[organizational_commitment].mean(axis=1)

# 확인
print(df[['psm_score', 'emotional_distance_score', 'commitment_score']].head())
