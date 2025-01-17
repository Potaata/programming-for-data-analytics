import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data_set = pd.read_table('floorsheet.tsv')


# Heat map of top 100 traded stock according to value of percentage change

# Calculating percentage change for each stock
price_changes = data_set.groupby('symbol').agg(
    high=('rate', 'max'),
    low=('rate', 'min')
)
price_changes['pct_change'] = ((price_changes['high'] - price_changes['low']) / price_changes['low']) * 100

# Sorting by absolute value of percentage change and selecting the top 100
top_100 = price_changes.reindex(price_changes['pct_change'].abs().sort_values(ascending=False).index).head(100)
top_100['symbol'] = top_100.index

 # Preparing data for heatmap
symbols = top_100['symbol'].values
pct_changes = top_100['pct_change'].values

# Creating 10x10 grid for heatmap
heatmap_symbols = np.array(symbols).reshape(10, 10)
heatmap_values = np.array(pct_changes).reshape(10, 10)

 
 # Creating annotated heatmap
plt.figure(figsize=(15, 10))
ax = sns.heatmap(
    heatmap_values,
    annot=heatmap_symbols + "\n" + np.round(heatmap_values, 2).astype(str),
    fmt="",
    cmap="coolwarm",
    cbar_kws={'label': 'Percentage Change (%)'}
)

 # Displaying the Heatmap
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