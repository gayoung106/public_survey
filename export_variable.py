import pandas as pd

df = pd.read_csv("data/converted_data.csv")

selected_vars = [
    # 공공봉사동기
    "q30_1", "q30_2", "q30_3", "q30_4", "q30_5", "q30_6",

    # 정서적 거리감
    "q31_1", "q31_2", "q31_3", "q31_4", "q31_5", "q31_6", "q31_7",

    # 조직몰입
    "q35_1", "q35_2", "q35_3", "q35_4",

    # 통제변인
    "dq1", "dq2", "dq3", "dq5_1", "dq5_2", "dq9_2", "dq11", "dq10"
]

filtered_vars = [var for var in selected_vars if var in df.columns]
print("✅ 필터링된 변수:", filtered_vars)

df_filtered = df[filtered_vars]
print(df_filtered.head())