import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("anscombe")
print df.describe()
print df.tail()
# sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
#            col_wrap=2, ci=None, palette="muted", size=4,
#            scatter_kws={"s": 50, "alpha": 1})
plt.show()
