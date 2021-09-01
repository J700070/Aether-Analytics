from dataParser import getStock
from database import countIndustries
from matplotlib import pyplot as plt
import numpy as np

def industriesChart():
    labels, sizes = countIndustries()

    sizes, labels = zip(*sorted(zip(sizes,labels)))

    x = np.arange(len(labels))
    width=0.8

    plt.bar(labels, sizes)
    plt.xticks(rotation = 90)
    plt.yscale('log')
    plt.show()



if __name__ == '__main__':
    industriesChart()