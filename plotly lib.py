#x = [1,2,3,4]
#y = [1,2,3,4]
import seaborn as sns
diamonds = sns.load_dataset('diamonds')
print(diamonds.info())
import plotly.express as px
#fig = px.line(diamonds.sample(5), x='price', y='carat')
#fig.show()
#fig = px.line(diamonds.sample(5), x ='price', y='y')
#fig.show()
#fig = px.line(diamonds.sample(5), x ='price', y='z')
#fig.show()

#fig = px.histogram(diamonds.sample(50), x='price')
#fig.show()
#fig = px.histogram(diamonds.sample(50), x='cut')
#fig.show()

#fig = px.violin(diamonds, x ='cut', y='price')
#fig.show()
#fig = px.violin(diamonds, x ='cut', y='carat')
#fig.show()

fig = px.scatter(diamonds, x ='cut', y='price')
fig.show()
fig = px.scatter(diamonds, x ='cut', y='carat')
fig.show()






