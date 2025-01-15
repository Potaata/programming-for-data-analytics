import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data_set = pd.read_table('floorsheet.tsv')

data_set.info()

column_names = data_set.columns
print("Column names:", column_names)

print("Dataset shape:", data_set.shape)

# total turnover

total_turnover = data_set['amount'].sum()
print("Total Turnover:", total_turnover)

#total traded shares

total_traded_shares = data_set['volume'].sum()
print("Total Traded Shares:", total_traded_shares)

#total transactions

total_transactions = len(data_set)
print("Total Transactions:", total_transactions)

#total stocks traded

total_stocks_traded = data_set['symbol'].nunique()
print("Total Stocks Traded:", total_stocks_traded)

#total trading brokers

total_trading_brokers = pd.concat([data_set['buyer'], data_set['seller']]).nunique()
print("Total Trading Brokers:", total_trading_brokers)

#creating DataFrame
stock_details = data_set.groupby('symbol').agg(
    open=('rate', 'first'),   # First trading price of the day
    high=('rate', 'max'),     # Highest trading price of the day
    low=('rate', 'min'),      # Lowest trading price of the day
    close=('rate', 'last'),   # Last trading price of the day
    volume=('volume', 'sum')  # Total volume traded
).reset_index()

# Display the resulting DataFrame
print(stock_details)

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


# Heat map of top 100 traded stock according to value of percentage change

# Calculating percentage change for each stock
price_changes = data_set.groupby('symbol').agg(
    high=('rate', 'max'),
    low=('rate', 'min')
)
price_changes['pct_change'] = ((price_changes['high'] - price_changes['low']) / price_changes['low']) * 100

# # Sorting by absolute value of percentage change and selecting the top 100
top_100 = price_changes.reindex(price_changes['pct_change'].abs().sort_values(ascending=False).index).head(100)
top_100['symbol'] = top_100.index

# # Preparing data for heatmap
symbols = top_100['symbol'].values
pct_changes = top_100['pct_change'].values

# # Creating 10x10 grid for heatmap
heatmap_symbols = np.array(symbols).reshape(10, 10)
heatmap_values = np.array(pct_changes).reshape(10, 10)

# # Creating annotated heatmap
plt.figure(figsize=(15, 10))
ax = sns.heatmap(
    heatmap_values,
    annot=heatmap_symbols + "\n" + np.round(heatmap_values, 2).astype(str),
    fmt="",
    cmap="coolwarm",
    cbar_kws={'label': 'Percentage Change (%)'}
)

# # Displaying the Heatmap
plt.title("Top 100 Traded Stocks by Percentage Change", fontsize=12)
plt.show()

# Creating graph of most traded stock by resampling the data for each minutes

# Converting the ts column to datetime
data_set['ts'] = pd.to_datetime(data_set['ts'], errors='coerce')

# Droping rows with invalid timestamps
data_set = data_set.dropna(subset=['ts'])

# Finding the most traded stock based on total volume
most_traded_stock = data_set.groupby('symbol')['volume'].sum().idxmax()
print(f"The most traded stock is: {most_traded_stock}")

# Filtering data for the most traded stock
most_traded_data = data_set[data_set['symbol'] == most_traded_stock]

# Setting the timestamp as the index for resampling
most_traded_data = most_traded_data.set_index('ts')

# Resampling data for each minute, summing the volume
resampled_data = most_traded_data['volume'].resample('1T').sum()

# Plotting the graph
plt.figure(figsize=(12, 6))
plt.plot(resampled_data, marker='o', linestyle='-', color='b')
plt.title(f"Trading Volume of {most_traded_stock} Over Time (1-Minute Intervals)", fontsize=16)
plt.xlabel("Time", fontsize=14)
plt.ylabel("Volume Traded", fontsize=14)
plt.grid(True)
plt.show()