import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix

#get data
x = np.arange(10).reshape (-1,1)
y = np.array([0,0,0,0,1,1,1,1,1,1])

#view the data
print ('For x, we have:',x)
print ('...and for y:',y)

#create a model and train it
ex4_2 = LogisticRegression(solver ='liblinear',random_state =0)

#to fit,or train it
ex4_2.fit(x,y)

#evaluate the model
print('The probablity is:',ex4_2.predict_proba(x))

#the actual predictions
print ('These are the predictions:')
print(ex4_2.predict(x))

#accuracy
print(ex4_2.score(x,y))

#
print(confusion_matrix(y,ex4_2.predict(x)))

#visualize
cm = confusion_matrix(y,ex4_2.predict(x))
fig,ax =plt.subplots(figsize =(8,8))

ax.imshow(cm)
ax.grid(False)
ax.xaxis.set(ticks =(0,1),ticklabels =('predicted 0s','predicted 1s'))
ax.yaxis.set(ticks =(0,1),ticklabels =('Actual 0s','Actual 1s'))
ax.set_ylim(1.5,-0.5)
for i in range (2):
    for j in range (2):
        ax.text(j,i,cm[i,j],ha='center',va='center',color='red')
plt.show()


print(classification_report(y,ex4_2.predict(x)))
