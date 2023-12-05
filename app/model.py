from pathlib import Path
import pandas as pd

def predict_player(text):
    p = Path('./static/csv')
    file_name = '*.csv'
    result_dataframes = []

    csv_files = p.glob(file_name)
    for file in csv_files:
        df = pd.read_csv(file)
        # 選手名が1文字でない場合のみ部分一致でフィルタリング
        filtered_df = df[df['選手名'].str.contains(text)]
        if not filtered_df.empty:
            result_dataframes.append(filtered_df)

    final_result = pd.concat(result_dataframes, ignore_index=True) if result_dataframes else None
    return final_result