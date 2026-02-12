import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')


years = data['Year'].tolist()
inflation = data['Inflation_Rate_Percent'].tolist()
gdp_raw = data['GDP_Current_USD'].tolist()
gdp_billion = [i/1000000000 for i in gdp_raw]


fig, ax1 = plt.subplots(figsize=(10,6))

ax1.plot(years, gdp_billion, marker='o', color='red', label='GDP')
ax1.set_ylabel('GDP (Billion USD)')
ax1.grid(True, linestyle='--', alpha=0.5)

ax2 = ax1.twinx()
ax2.plot(years, inflation, marker='s', color='blue', label='Inflation')
ax2.set_ylabel('Inflation (%)')

plt.title('GDP vs Inflation')
plt.xticks(rotation=45)

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()


plt.show()
