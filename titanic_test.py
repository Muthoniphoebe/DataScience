import pandas as pd
import seaborn as sns
titanic_df = sns.load_dataset('titanic')
print(titanic_df.head())
print(titanic_df.shape)
print(f"DataFrame shape : {titanic_df.shape}\n=================================")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="ticks")
plt.style.use("fivethirtyeight")
sns.catplot(x='sex', data=titanic_df, kind='count')
plt.show()
sns.catplot(x='pclass', data=titanic_df, hue='sex', kind='count')
plt.show()
titanic_df['person'] = titanic_df.sex
titanic_df.loc[titanic_df['age'] < 16, 'person'] = 'child'
print(titanic_df.person.unique())
print(titanic_df.person.value_counts())
print(titanic_df.age.mean())
sns.catplot(x='pclass', data=titanic_df, hue='person', kind='count')
plt.show()
titanic_df.age.hist(bins=80)
plt.show()
fig = sns.FacetGrid(titanic_df, hue="sex", aspect=4)
fig.map(sns.kdeplot, 'age', shade=True)

oldest = titanic_df['age'].max()

fig.set(xlim=(0, oldest))

fig.add_legend()
plt.show()
fig = sns.FacetGrid(titanic_df, hue="person",aspect=4)
fig.map(sns.kdeplot, 'age', shade=True)

oldest = titanic_df['age'].max()

fig.set(xlim=(0, oldest))

fig.add_legend()
plt.show()
fig = sns.FacetGrid(titanic_df, hue="pclass",aspect=4)
fig.map(sns.kdeplot, 'age', shade=True)

oldest = titanic_df['age'].max()

fig.set(xlim=(0, oldest))

fig.add_legend()
plt.show()

