import pandas as pd
import os
DIR = "./data"

def load_data(filename):
    abs_path = os.path.abspath(DIR)
    df = pd.read_csv(f'{abs_path}/{filename}')
    df.Date = pd.to_datetime(df.Date)
    return df