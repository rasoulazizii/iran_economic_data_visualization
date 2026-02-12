import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')


years = data['Year'].tolist()

trade_balance = (data['Exports_USD'] - data['Imports_USD']) / 1_000_000_000


plt.figure(figsize=(10,6))

plt.plot(years, trade_balance, marker='o', linewidth=2, label='trade balance')
plt.axhline(0)
plt.title('Trade Balance')
plt.xlabel('years')
plt.ylabel('Trade Balance (Billion USD)')
plt.legend(loc='upper left', fontsize=10)
plt.grid(True)
plt.savefig("data/trade_balance.png", dpi=300)
plt.show()