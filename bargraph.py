#install and import libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#read csv file and data in particular columns
d = pd.read_csv('hour.csv')
hour = d['hr']
rentals = d['cnt']

#bar graph
plt.bar(hour, rentals)

#label graph
plt.xlabel('Hour (24 Hour Format)')
plt.ylabel('Total Bikes Rented')
plt.title('Bike Sharing in Relation to Hour of the Day')

#show bar graph
plt.show()
