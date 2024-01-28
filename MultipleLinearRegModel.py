from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=  pd.read_excel("cleanedData.xlsx")
non_null_rows = df[df['Food&Beverages'].notnull()]
X = non_null_rows[['ValueForMoney', 'CabinStaffService','SeatComfort']]
y = non_null_rows['Food&Beverages']
 
# Separating the data into independent and dependent variables
# Converting each dataframe into a numpy array 
# since each dataframe contains only one column
# non_null_rows.dropna(inplace = True)
 
# Dropping any rows with Nan values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
 
# Splitting the data into training and testing data
regr = LinearRegression()
 
regr.fit(X_train, y_train)
print(regr.score(X_test, y_test))