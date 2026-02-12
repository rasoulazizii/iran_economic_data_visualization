import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data.csv')

years = data['Year'].tolist()
gdp = data['GDP_Current_USD'].tolist()

gdp_billion = [i/1000000000 for i in gdp]

plt.plot(years, gdp_billion, color='red', marker='o')
plt.title('iran GDP by year')
plt.xlabel('Years')
plt.ylabel('USD(Billion USD)')
plt.grid(True)
plt.savefig("plots/gdp.png")
plt.show()