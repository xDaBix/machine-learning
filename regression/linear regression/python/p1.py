# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 09:46:06 2025

@author: Varun
"""

#simple linear regression y=b0+b1*x1

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ds1 = pd.read_csv('Salary_Data.csv')


x1 = ds1.iloc[:, :-1].values
y1 = ds1.iloc[:, 1].values


#splitting the dataset into train and test set
from sklearn.model_selection import train_test_split
x_train1, x_test1, y_train1, y_test1 = train_test_split(x1, y1, test_size=1/3, random_state=0)


"""
#feature scaling
from sklearn.preprocessing import StandardScaler
ssx=StandardScaler()
x_train1=ssx.fit_transform(x_train1)
x_test1=ssx.transform(x_test1)
"""

#fitting simple Linear regression model to the training set
from sklearn.linear_model import LinearRegression
re=LinearRegression()
re.fit(x_train1, y_train1)

#predicting the test set resuts
y_pred=re.predict(x_test1)

#visualizing the training set result

plt.scatter(x_train1, y_train1,color='red')
plt.plot(x_train1, re.predict(x_train1),color='blue')
plt.title('salary vs exp (trainig set)')
plt.xlabel('years of experience')
plt.ylabel('salary')
plt.show()


#visualizing the test set result

plt.scatter(x_test1, y_test1,color='red')
plt.plot(x_train1, re.predict(x_train1),color='blue')
plt.title('salary vs exp (test set)')
plt.xlabel('years of experience')
plt.ylabel('salary')
plt.show()
