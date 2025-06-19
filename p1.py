import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv('data.csv')
ds.replace('NaN', np.nan, inplace=True)

x = ds.iloc[:, :-1].values
y = ds.iloc[:, -1].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

print(x)

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
l1=LabelEncoder()
x[:,0]=l1.fit_transform(x[:,0])
h1 = OneHotEncoder(sparse_output=False)
x_encoded = h1.fit_transform(x[:, [0]])
x = np.hstack((x_encoded, x[:, 1:]))
l2=LabelEncoder()
y=l2.fit_transform(y)
print(x)

#splitting the dataset into train and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
#feature scaling standardization and normalization







