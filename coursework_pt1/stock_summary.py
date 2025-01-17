import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data_set = pd.read_table('floorsheet.tsv')

data_set.info()

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