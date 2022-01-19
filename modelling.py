import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

df=pd.read_csv("C:\\Users\\akshat.2.bansal\\Desktop\\Akshat\\Self Learning\\ExtrA\\Dockers-master\\Dockers-master\BankNote_Authentication.csv")

X=df.iloc[:,:-1]
y=df.iloc[:,-1]


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)


classifier=RandomForestClassifier()
classifier.fit(X_train,y_train)

y_pred=classifier.predict(X_test)

score=accuracy_score(y_test,y_pred)
print("Accuracy is ::::",score)

print("*************** SAVING MODEL ***********************")
import pickle
pickle_out = open("classifier.pkl","wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()
print("*******MODEL SAVED*******************")
print(classifier.predict([[2,3,4,1]]))
print("Done")