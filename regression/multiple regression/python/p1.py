# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 13:37:29 2025

@author: Varun
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

ds = pd.read_csv('50_Startups.csv')


x = ds.iloc[:, :-1].values
y = ds.iloc[:, 4].values
#categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
l1=LabelEncoder()
x[:,3]=l1.fit_transform(x[:,3])
h1 = OneHotEncoder(sparse_output=False)
x_encoded = h1.fit_transform(x[:, [3]])
x = np.hstack((x_encoded, x[:, :3],x[:,4:]))

#avoiding dummy variable trap
x=x[:,1:]




#splitting the dataset into train and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

#multiple linear 
from sklearn.linear_model import LinearRegression
re=LinearRegression()
re.fit(x_train,y_train)

#predicting the test set result
y_pred=re.predict(x_test)

#using backward elimination

x = np.append(arr=np.ones((x.shape[0], 1)).astype(float), values=x, axis=1)
x_opt = x[:, [0, 3 ]]
re1 = sm.OLS(y.astype(float), x_opt.astype(float)).fit()
re1.summary()
