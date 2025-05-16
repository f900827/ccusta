import pandas as pd
import os

# 輸入檔案名稱（請改為你的檔案名稱）
input_file = 'agg.csv'

# 讀取 CSV 並清理欄位名稱空白
df = pd.read_csv(input_file)
df.columns = df.columns.str.strip()  # ✅ 移除欄位名稱前後空白

# 欲依據分割的欄位名稱
group_column = 'no'

# 建立輸出資料夾
output_dir = 'split_by_no'
os.makedirs(output_dir, exist_ok=True)

# 分組並儲存每組為獨立 CSV，保證表頭一致
for no_value, group_df in df.groupby(group_column):
    # 再保險一次：確保每個子表的欄位名稱也乾淨
    group_df.columns = group_df.columns.str.strip()
    output_path = os.path.join(output_dir, f'{no_value}.csv')
    group_df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"✅ 已完成，分割出 {df[group_column].nunique()} 個 CSV 檔案，儲存在：{output_dir}")