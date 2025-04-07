import pyreadstat
import os

input_path = "data/한국행정연구원_공직생활실태조사_데이터_2024.sav"
output_path = "data/converted_data.csv"

df, meta = pyreadstat.read_sav(input_path)
df.to_csv(output_path, index=False)

print("변환 완료: converted_data.csv 저장됨")
