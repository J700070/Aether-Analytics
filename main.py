from dataParser import getStock
from matplotlib import pyplot as plt
import numpy as np

#Get Stock
stock = getStock('AAPL')


width = 0.8
x_pos = np.arange(len(stock["dates"]))
print(x_pos)
#fig, ax = plt.subplots()

#ax.bar(stock["dates"],stock["revenue"], width, color= "#003f5c")  
plt.bar(x_pos, stock["revenue"])
plt.xticks(x_pos, stock["dates"], color='black', rotation=45)
""" plt.set_title(stock["ticker"] + " revenues")
plt.set_ylabel("Revenue (millions)")
plt.set_xlabel("Period") """
plt.show()
