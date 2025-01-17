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