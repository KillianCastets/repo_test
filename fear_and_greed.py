import requests
from datetime import datetime
import pandas as pd

def get_indicator_history() -> pd.DataFrame:
    r = requests.get("https://api.alternative.me/fng/?limit=0")
    df = pd.DataFrame.from_dict(r.json()['data'])
    df['date'] = df['timestamp'].apply(lambda x : datetime.fromtimestamp(int(x)))
    df.to_csv('dataframes/fear_and_greed.csv')

    return df

get_indicator_history()