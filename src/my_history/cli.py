import pandas as pd
import sys
def cnt():
    df = pd.read_parquet("~/tmp/history.parquet")
    keyword=sys.argv[1]
    fdf = df[df['cmd'].str.contains(keyword)]
    cnt = fdf['cnt'].sum()
    print(cnt)

