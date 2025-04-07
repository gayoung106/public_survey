import pandas as pd
from scipy.stats import pearsonr

# 1. CSV 데이터 불러오기
df = pd.read_csv("data/converted_data.csv")

# 2. 요인별 합산 점수 생성
df['공공봉사동기'] = df[['q30_1', 'q30_2', 'q30_3', 'q30_4', 'q30_5', 'q30_6']].sum(axis=1)
df['정서적거리감'] = df[['q31_1', 'q31_2', 'q31_3', 'q31_4', 'q31_5', 'q31_6', 'q31_7']].sum(axis=1)
df['조직몰입']     = df[['q35_1', 'q35_2', 'q35_3', 'q35_4']].sum(axis=1)

# 3. 상관관계 분석
variables = ['공공봉사동기', '정서적거리감', '조직몰입']

print("✅ 상관관계 분석 결과:")
for i in range(len(variables)):
    for j in range(i + 1, len(variables)):
        var1 = variables[i]
        var2 = variables[j]
        corr, p_value = pearsonr(df[var1], df[var2])
        print(f"{var1} ↔ {var2} 상관계수: {corr:.3f}, p값: {p_value:.4f}")

# 상관관계 분석 결과:
# 공공봉사동기 ↔ 정서적거리감 상관계수: -0.209, p값: 0.0000
# 공공봉사동기 ↔ 조직몰입 상관계수: 0.601, p값: 0.0000
# 정서적거리감 ↔ 조직몰입 상관계수: -0.327, p값: 0.0000