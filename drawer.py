import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame


class Drawer:
    def __init__(self):
        pass

    def drawDiagram(self, data: DataFrame):
        plt.pie(data, labels=data.index)
        plt.savefig('plot.png')