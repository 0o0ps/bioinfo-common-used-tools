import pandas as pd
def convert_string(s):
    # 提取字符串中的数字部分
    number = s[1:]
    # 构造目标字符串
    result = f"GC_NAIC_GC{number}_pre"
    return result
df = pd.read_csv("Daping hospital-RNA-seq-clinical.csv")
df["Samples"] = df["Sample ID"].apply(convert_string)
df.to_csv("Daping hospital-RNA-seq-clinical.csv", index=False)