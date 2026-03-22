import pandas as pd
 
def extract(file_path):
    print(f"Extracting data from {file_path}...")
    data = pd.read_csv(file_path, encoding='latin1')
    print(f"Extracted {len(data)} rows and {len(data.columns)} columns.")
    print(f"Columns: {data.columns.tolist()}")
    return data