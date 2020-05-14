import pandas as pd


def data_to_csv():
    df = pd.read_excel("某井可压性参数.xlsx", sheet_name="property", usecols=[0,1,2,3,4,5])
    df.to_csv("某井可压性参数.csv",
              index = False,
              sep = "\t",
              encoding="utf-8-sig")

data_to_csv()