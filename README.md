# data-visualization
A simple program written in Python3 that generates statistical metrics and visualizations from data stored in any .CSV file and produces bar graph, histogram, scatterplot, and box plot representations of provided data using numpy, pandas, matplotlib, and seaborn.

# What's in Here?
descriptivestats.py — generates mean, median, standard deviation, quartiles, standard score, and outliers of provided data. <br />
bargraph.py — generates bar graph representation of data from your inputted .csv file. <br />
histogram.py — generates histogram representation and distribution of data from your inputted .csv file. <br />
scatterplot.py — generates scatterplot representation data from your inputted .csv file. <br />
boxplot.py — generates box plot representation data from your inputted .csv file. <br />
hour.csv — example .csv file to see how the program works.<br /> 

All visual representations are built to be modular. They are divided into separate Python files so that you may pick and choose which representations you need for your personal use case.

# How Do I Use This?
1. Download the .csv file you want to use. 
2. For any statement phrased as df=pd.read_csv('hour.csv') or d=pd.read_csv('hour.csv'), replace 'hour.csv' with the name of the .csv file you want to use.
3. For any statement phrased as df['hr'] or d['cnt'], replace the titles within the brackets with the name of the column in the .csv file from which you are using the data (Don't forget the single quotes!).
4. For the graph representations, change the label of the x axis (plt.xlabel), the label of the y axis (plt.ylabel), and title (plt.title) of the graph to reflect what your representation is trying to show about your data. <br />

In each file, you'll see comments that will show you what you need to change in order to make this data visualization tool work for your use case. Feel free to adjust any formatting elements as well! I've provided an example .csv file in case you want to see how it works. Take care!
