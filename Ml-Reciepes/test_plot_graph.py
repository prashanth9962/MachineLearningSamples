import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
data = sm.datasets.co2.load_pandas()
y = data.data

print "========="
print y.columns.values
y = y['co2'].resample('MS').mean()
y = y.fillna(y.bfill())
y.plot(figsize=(15, 6))
plt.show()
