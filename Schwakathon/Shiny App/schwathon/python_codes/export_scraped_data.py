import glob
import json
import pandas as pd
import os

#os.system("python C:/Users/abhin/Documents/Schwathon/financeSpiders-master/financeSpiders-master/financeScraper/crawlers.py -i C:/Users/abhin/Documents/Schwathon/financeSpiders-master/financeSpiders-master/financeScraper/stock.txt")

df = pd.DataFrame()
for g in glob.glob("C:/Users/abhin/Documents/Schwathon/financeSpiders-master/financeSpiders-master/financeScraper/data/*.jl"):
    data = []
    with open(g) as f:
        #print(f)
        for line in f:
            data.append(json.loads(line))
    dfx = pd.DataFrame(data)
    df = df.append(dfx)

df.to_csv("data_scraped.csv",encoding='utf-8')
print("Data Exported")