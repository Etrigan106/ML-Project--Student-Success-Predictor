# %%
#import libraries
import os
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

# %%
#import dataset
d=pd.read_csv('Student_Data.csv')

# %%
d

# %%
# handle text column using label encoding
activities=LabelEncoder()
d['Ext_Act']=activities.fit_transform(d['Extracurricular_Activities'])

# %%
d

# %%
#remove extra column
data=d.drop('Extracurricular_Activities',axis='columns')
data

# %%
# information of dataset
data.info()

# %%
#check null values
data.isnull().sum()

# %%
#correlation
cor=data.corr()

# %% [markdown]
# A value of +1 indicates a perfect positive correlation, meaning as one variable increases, the other also increases. A value of -1 indicates a perfect negative correlation, meaning as one variable increases, the other decreases. A value of 0 indicates no correlation.

# %%
# sns.heatmap(cor, annot=True, cmap='Greens')

# %% [markdown]
# Seperate X & Y 

# %%
# separate variables X and Y,
# X is feature (These are the input variables or attributes used to predict the outcome)
# Y is label (These are the input variables or attributes used to predict the outcome.)
X=data.drop('Performance_Index',axis='columns')
X

# %%
Y=data.Performance_Index
Y

# %%
# split data set into training and testing parts
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

# %%
#checking length of training and testing data
print(len(X_train))
print(len(X_test))
print(len(Y_train))
print(len(Y_test))

# %%
#applying Model
M=LinearRegression()

# %%
M.fit(X_train,Y_train)

# %%
# R-Squared
M.score(X_test,Y_test)

# %% [markdown]
# R-squared (R²), also known as the coefficient of determination, is a statistical measure that indicates the proportion of the variance in the dependent variable that is predictable from the independent variables. An R² value close to 1 indicates that the model explains a large portion of the variance in the dependent variable, whereas an R² close to 0 indicates that the model does not explain much of the variance.

# %%
# root mean squared error
# rmse = np.sqrt(mean_squared_error(Y_test, Y_pred))
# rmse

# # %%
# # Mean absoute error
# mae = mean_absolute_error(Y_test, Y_pred)
# mae

# %%
#some random values of features (X)
x=[[6,7,5,81,93,92,90,1]]

# %%
#intercept
b=M.intercept_
# coefficient
m=M.coef_

# %%
#predicting y using mathematical formula
mx=m*x
mx=mx.sum()
y=mx+b
y

# %%
#predicting y using model (algorithm)
y1=M.predict(x)
y1=float(y1)
y1

# %%
# Predicted values
Y_pred = M.predict(X_test)
# Plotting the predicted vs actual values
plt.figure(figsize=(10, 6))
plt.scatter(Y_test, Y_pred, color='blue', label='Predicted vs Actual')
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color='red', label='Ideal fit')
plt.title('Actual vs Predicted Performance Index')
plt.legend()
# plt.show()

# %%





