import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

# 데이터 불러오기
df = pd.read_csv("data/converted_data.csv")

# 요인별 점수 계산
df["psm_score"] = df[["q30_1", "q30_2", "q30_3", "q30_4", "q30_5", "q30_6"]].mean(axis=1)
df["edg_score"] = df[["q31_1", "q31_2", "q31_3", "q31_4", "q31_5", "q31_6", "q31_7"]].mean(axis=1)
df["om_score"] = df[["q35_1", "q35_2", "q35_3", "q35_4"]].mean(axis=1)

# 통제변수 포함한 독립변수
X = df[[
    "psm_score", "edg_score",
    "dq1", "dq2", "dq3", "dq5_1", "dq5_2", "dq9_2", "dq10"
]]

# 범주형 변수 더미화
X = pd.get_dummies(X, columns=["dq2", "dq3", "dq5_1", "dq5_2", "dq9_2", "dq10"], drop_first=True)

# 상수항 추가
X = add_constant(X)

# 모든 변수를 숫자형으로 변환
X = X.astype(float)

# VIF 계산
vif_data = pd.DataFrame()
vif_data["변수명"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# 결과 출력
print(vif_data)

#             변수명          VIF
# 0         const  7147.192229
# 1     psm_score     1.200127
# 2     edg_score     1.118738
# 3           dq1     1.160103
# 4    dq2_1965.0    16.164315
# ..          ...          ...
# 336  dq10_716.0     1.051248
# 337  dq10_717.0     1.159734
# 338  dq10_750.0     1.897445
# 339  dq10_754.0     1.045274
# 340  dq10_840.0     1.151373

# [341 rows x 2 columns]