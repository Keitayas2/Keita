from pathlib import Path
import pandas as pd
import csv

from pathlib import Path
import pandas as pd

def predict_player1(text):
    p = Path('./static/csv')
    file_name = '*-batter.csv'
    result_dataframes = []

    csv_files = p.glob(file_name)
    for file in csv_files:
        df = pd.read_csv(file)
        filtered_df = df[df['選手名'].str.contains(text)]
        if not filtered_df.empty:
            result_dataframes.append(filtered_df)

    final_result = pd.concat(result_dataframes, ignore_index=True) if result_dataframes else None
    if final_result is not None:
        # 各選手ごとにNaNを含む列を削除して表示
        final_result = final_result.apply(lambda x: x.dropna().reset_index(drop=True), axis=1)

        if not final_result.empty:
            final_result = final_result.to_string(index=False, header=False)  # indexとheaderを除外して文字列に変換
            print(final_result)
            return final_result
        else:
            return None
    else:
        return None


def predict_player2(text):
    p = Path('./static/csv')
    file_name = '*-pitcher.csv'
    result_dataframes = []

    csv_files = p.glob(file_name)
    for file in csv_files:
        df = pd.read_csv(file)
        filtered_df = df[df['選手名'].str.contains(text)]
        if not filtered_df.empty:
            result_dataframes.append(filtered_df)

    final_result = pd.concat(result_dataframes, ignore_index=True) if result_dataframes else None
    if final_result is not None:
        # 各選手ごとにNaNを含む列を削除して表示
        final_result = final_result.apply(lambda x: x.dropna().reset_index(drop=True), axis=1)

        if not final_result.empty:
            final_result = final_result.to_string(index=False, header=False)  # indexとheaderを除外して文字列に変換
            print(final_result)
            return final_result
        else:
            return None
    else:
        return None
