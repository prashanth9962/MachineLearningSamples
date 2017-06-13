from sklearn import tree

features = [[140, 0], [130, 0], [120, 0], [150, 1], [170, 1], [155, 1]]
labels = [0, 0, 0, 1, 1, 1]
clf = tree.DecisionTreeClassifier()
clf.fit(features,labels)
print clf.predict([[150, 1],[145,1]])
from sklearn import datasets, linear_model
from sklearn import covariance

from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
import pandas as pd
from pandas.tools.plotting import lag_plot,autocorrelation_plot

def parser(x):
    return datetime.strptime('190' + x, '%Y-%m')


series = pd.read_csv('/home/prashanth/sample_data_grp.csv',index_col=0, header=0, squeeze=True,error_bad_lines=False)
#print(series.columns.values)
print series.head()
#series.temperature = series.temperature.astype(str)
series.plot()
#pyplot.show()
#lag_plot(series)
#autocorrelation_plot(series)
pyplot.show()
#series.plot()
#pyplot.show()
