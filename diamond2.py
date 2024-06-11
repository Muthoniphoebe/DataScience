import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

diamonds = sns.load_dataset('diamonds')
print(diamonds.head())
plt.figure(figsize=(6,10))
sns.histplot(diamonds['price'],kde = True)
plt.show()
sns.histplot(diamonds['carat'],kde = True)
plt.show()
