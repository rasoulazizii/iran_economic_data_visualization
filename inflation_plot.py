import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('data.csv')
years = data['Year'].tolist()
inflation = data['Inflation_Rate_Percent'].tolist()

plt.plot(years, inflation, color='red', marker='o')
plt.title('Iran inflation by year')
plt.xlabel('Years')
plt.ylabel('Inflation(Percent)')
plt.grid(True)
plt.savefig("plots/inflation.png", dpi=300)
plt.show()