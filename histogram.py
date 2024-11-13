#install and import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read data from csv file
d = pd.read_csv('hour.csv')

#plot histogram, identify bins, distribution, colors
#change d['column'] to change the column]
#change bins to desired number
#change kernel to desired function (or false if you don't want kde)
#change formatting to desired colors
sns.histplot(d['cnt'], bins=10, kde=True, color='green', edgecolor='lightgreen')
#sns.kdeplot for more variety

#histogram labels
#change title to desired title
plt.xlabel('Interval of Amount of Rentals')
plt.ylabel('Frequency of Bike Rentals')
plt.title('Histogram of Total Bike Count')

#show histogram
plt.show()
