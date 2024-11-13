#import and install libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#read any csv file
d = pd.read_csv('hour.csv')

#boxplot representation of any column from csv file
sns.boxplot(d['cnt'])

#labels for graph
plt.xlabel('Count of Bikes Rented')
plt.title('Box Plot of Total Bikes Rented')

#show graph
plt.show()
