import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')


years = data['Year'].tolist()
trade_balance = (data['Exports_USD'] - data['Imports_USD']) / 1_000_000_000
exchange_rate = data['Official_Exchange_Rate'].tolist()


fig, ax1 = plt.subplots(figsize=(10,6))

ax1.plot(years, trade_balance, marker='o', color='red', label='Trade Balance')
ax1.set_ylabel('Trade balance (Billion USD)')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.axhline(0)
ax2 = ax1.twinx()
ax2.plot(years, exchange_rate, marker='s', color='blue', label='exchnage rate')
ax2.set_ylabel('Exchange Rate')

plt.title('Trade Balance vs Exchange Rate')
plt.xticks(rotation=45)

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()

plt.savefig("plots/tradeblance_vs_exchnagerate.png")
plt.show()
