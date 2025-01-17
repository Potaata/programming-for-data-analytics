import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data_set = pd.read_table('floorsheet.tsv')

#Top 10 Most Traded Stocks
most_traded_stocks = data_set['symbol'].value_counts().head(10)
print("Most Traded Stocks:")
print(most_traded_stocks)

# Top 10 Most active total volume for each stock
top_10_active_by_volume = data_set.groupby('symbol')['volume'].sum().sort_values(ascending=False).head(10)
print("TMost Active Stocks by Volume:")
print(top_10_active_by_volume)

# Top 10 Most active stock by value
top_10_active_by_value = data_set.groupby('symbol')['amount'].sum().sort_values(ascending=False).head(10)
print("Most Active Stocks by Value:")
print(top_10_active_by_value)

# Top 10 Price Percentage Change Increase in Stock
price_change_increase = data_set.groupby('symbol').agg(
    high=('rate', 'max'),
    low=('rate', 'min')
)
price_change_increase['pct_change'] = ((price_change_increase['high'] - price_change_increase['low']) / price_change_increase['low']) * 100
top_10_biggest_increase = price_change_increase.sort_values('pct_change', ascending=False).head(10)
print("Biggest Intra-day Percentage Price Increase:")
print(top_10_biggest_increase)


# Top 10 Price Percentage Change Decrease in Stock
price_change_decrease = data_set.groupby('symbol').agg(
    high=('rate', 'max'),
    low=('rate', 'min')
)
price_change_decrease['pct_change'] = ((price_change_decrease['low'] - price_change_decrease['high']) / price_change_decrease['high']) * 100
top_10_biggest_decrease = price_change_decrease.sort_values('pct_change').head(10)
print("Top 10 Biggest Intra-day Percentage Price Decrease:")
print(top_10_biggest_decrease)
