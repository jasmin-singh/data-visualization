#install and import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#read data points from any csv file
df = pd.read_csv("hour.csv")
# extrapolate info from any column of csv
X = df['hr']
Y = df['cnt']

#find the regression eq
A = np.vstack([X, np.ones(len(X))]).T
b1, b0 = np.linalg.lstsq(A, Y, rcond=None)[0]
print(f'yhat = {b0} + {b1}*x')

#create scatterplot
plt.scatter(X, Y)
plt.plot(X, b0 + b1 * X, 'r')

#labels for graph
plt.xlabel('Hour (24 Hour Format)')
plt.ylabel('Total Bikes Rented')
plt.title('Bike Sharing in Relation to Hour of the Day')

#show scatterplot and plot line of best fit
plt.show()
print(np.corrcoef(X, Y))
