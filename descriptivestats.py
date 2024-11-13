import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

#read csv file of your choice
df=pd.read_csv('hour.csv')

#replace df name with desired column for descriptive stats
#calculate mean
mean_value=df['windspeed'].mean()
print('Mean Value:\n'+str(mean_value))

#calculate median
median_value=df['windspeed'].median()
print('\nMedian Value:\n'+str(median_value))

#calculate std
std_value=df['windspeed'].std()
print('\nStandard Deviation Value:\n'+str(std_value))

#calculate quartiles
quartile = df['windspeed'].quantile([0.25, 0.5, 0.75])
print('\nQuartile Values:\n'+str(quartile))

#set threshold for z score to calculate outliers
threshold = 3
outliers = []

#calculate z score for particular data
for x in df['windspeed']:
 z_score = (x - mean_value) / std_value
 if abs(z_score) > threshold:
   outliers.append(x)
thresholdneg = -3
for x in df['windspeed']:
 z_score = (x - mean_value) / std_value
 if abs(z_score) < thresholdneg:
   outliers.append(x)
#prints all instances of outliers
print("\nOutliers:\n", sorted(outliers))