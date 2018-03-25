# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 15:13:17 2018

@author: rohit
"""
#classification of male and female frogs

from sklearn import tree
from sklearn.metrics import accuracy_score
#size of ears and eyes of frogs
X=[[1,1],[1.5,1.5],[2,2.5],[2.5,2],[3,3.4],[4,5.5],[5,5],[5.5,5.5]]
Y=['female', 'female' ,'male', 'male','male','male','female','female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[3.5,4]])
print(prediction)
