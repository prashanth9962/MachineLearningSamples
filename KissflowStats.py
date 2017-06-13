import MySQLdb
import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

class MysqlConnector:

    def __init__(self):
        self.connection = MySQLdb.connect(host="localhost", user="root", passwd="root", db="KissflowStats")
        self.cursor = self.connection.cursor()

    def execute_query(self,query):
        return self.cursor.execute(query)

    def close(self):
        self.connection.close()


class KissStatsModel:

    def __init__(self):
        self.dbConnection = MysqlConnector()
        self.data = self.get_pandas_dataframe_sql()

    def fetch_sql_data(self):
        self.dbConnection.execute_query("Select PO_Date,PO_Total from purchase_order limit 100")
        return self.dbConnection.cursor.fetchall()

    def parse_dates(self,date):
        return pd.datetime.strptime(date, '%d-%b-%Y')

    def get_pandas_dataframe_sql(self):
        data = pd.read_sql("Select PO_Date,PO_Total,Unit_Price,Vendor_Name from purchase_order limit 500" ,con=self.dbConnection.connection)
        #data.reset_index(inplace=True)
        return data

    def show_histogram(self):
        pyplot.hist(self.data.PO_Total,bins=20, normed=True)
        pyplot.show()

    def plot_graph(self):
        self.data.plot()
        #pyplot.plot(self.data)
        pyplot.show()

    def linear_model(self):
       import seaborn as sns
       sns.lmplot(x="PO_Total",y="Unit_Price",data=self.data,hue="Vendor_Name")
       #sns.pairplot(self.data, hue="Vendor_Name")
       pyplot.show()

    def linear_model2(self):
        import seaborn as sns
        sns.lmplot(x="PO_Total", y="Unit_Price", col="Vendor_Name", hue="Vendor_Name", data=self.data,
                   col_wrap=2, ci=None, palette="muted", size=4,
                   scatter_kws={"s": 50, "alpha": 1})
        pyplot.show()




a = KissStatsModel()
print a.data.describe()
print a.plot_graph()

#
#
# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii
#
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.show()
