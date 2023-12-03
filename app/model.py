import pandas as pd
from pathlib import Path

p = Path('./static/csv')
file_name = '*.csv'

csv_files  = p.glob(file_name)

for file in csv_files:
    """ CSVファイルデータをData Frameに変換 """
    df1 = pd.read_csv(file)
    print(df1)
