import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv('Position_Salaries.csv')

x = ds.iloc[:, 1:2].values 
y = ds.iloc[:, 2].values


'''
#splitting the dataset into train and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#feature scaling
from sklearn.preprocessing import StandardScaler
ssx=StandardScaler()
x_train=ssx.fit_transform(x_train)
x_test=ssx.transform(x_test)
'''




