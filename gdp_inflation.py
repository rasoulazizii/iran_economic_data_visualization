import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')


years = data['Year'].tolist()
inflation = data['Inflation_Rate_Percent'].tolist()
gdp_raw = data['GDP_Current_USD'].tolist()
gdp_billion = [i/1000000000 for i in gdp_raw]


fig, ax1 = plt.subplots()

ax1.plot(years, gdp_billion, label='GDP', color='red')
ax1.set_ylabel('GDP (Billion current USD)')

ax2 = ax1.twinx()
ax2.plot(years, inflation, label='Inflation', color='blue')
ax2.set_ylabel('Inflation (%)')

plt.title('GDP vs Inflation')
plt.show()
