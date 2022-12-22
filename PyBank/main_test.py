import pandas as pd 


df = pd.read_csv("")

df

df["Date"].count()

df["Profit/Losses"].sum()

df["Profit/Losses"].mean()

highest_profit = df["Profit/Losses"].max()

lowest_profit = df["Profit/Losses"].min()

highest_profit

lowest_profit

df["Date"].where(df["Profit/Losses"] == highest_profit) 

df["Date"].where(df["Profit/Losses"] == highest_profit)

dex = df[df["Profit/Losses"]==highest_profit].index[0]

high_date = df.loc[dex, "Date"]

dex = df[df["Profit/Losses"]==lowest_profit].index[0]
low_date = df.loc[dex, "Date"]
high_date


low_date

df.loc[4][1]