import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5,15,25,35,45,55]).reshape((-1,1))
y = np.array([5,20,14,32,22,38])

print('These are values in x:',x)
print('These are values in y:',y)

#creating a model
ex4_1 = LinearRegression()
print(ex4_1)

#Training
ex4_1.fit(x,y)

#Validation
r_sq = ex4_1.score(x,y)
print(r_sq)

#interpretation
phoebe = ex4_1.intercept_
muthoni = ex4_1.coef_

print('The y intercept is:',phoebe)
print('The gradient is:',muthoni)

#applying the results
 #using existing values
y_pred = ex4_1.predict(x)
print(y_pred)
 #using forecast values
x_new = np.arange(5).reshape((-1,1))
print(x_new)

y_new = ex4_1.predict(x_new)
print('New y values are:',y_new)


