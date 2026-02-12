import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')


years = data['Year'].tolist()
gdp_growth_rate = data['GDP_Growth_Percent'].tolist()
inflation = data['Inflation_Rate_Percent'].tolist()

plt.figure(figsize=(10,6))

plt.plot(years, gdp_growth_rate, marker='o', linewidth=2, label='GDP Growth (%)')
plt.plot(years, inflation, marker='s', linewidth=2, label='Inflation (%)')
plt.title('Stagflation Analysis')
plt.xlabel('years')
plt.ylabel('percent (%)')
plt.legend(loc='upper left', fontsize=10)
plt.grid(True)
plt.savefig("plots/stagflation.png")
plt.show()