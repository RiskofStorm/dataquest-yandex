import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression

data = pd.read_csv("sphist.csv")
data["Date"] = pd.to_datetime(data["Date"])
# print(data.head(2))
# print(data['Date'].dtypes)

# data["Date"] = data[data["Date"] > datetime(year=2015,month=4, day=1)]
data["Date"] = data["Date"].sort_values(ascending=True)
data_shifted = data.shift(periods=1)



data["Avg 5 days"] = data_shifted["Close"].rolling(5).mean()
data["Avg 30 days"] = data_shifted["Close"].rolling(30).mean()
data["Std 5 days"] = data_shifted["Close"].rolling(5).std()

# The standard deviation of the average volume over the past five days.
# data["Std past 5 Avg days"] =  data["Avg 5 days"].rolling(5).std() <- increases rmse
data["Avg high-low"] = (data["High"].abs() - data["Low"].abs())/(data["High"].std() + data["Low"].std()) 


# print(data[["Avg 5 days","Avg 30 days","Std 5 days"]])

data = data[data["Date"] > datetime(year=1951, month=1, day=3)]
data.dropna(axis=0, inplace=True)


train_test_index = datetime(year=2013, month=1, day=1)
train = data[data["Date"] < train_test_index]
test = data[data["Date"] > train_test_index]
# print(train.shape)
# print(test.shape)


model = LinearRegression()
features = list(data.columns.drop(["Close","Date", "Volume",'Avg high-low']))
target = "Close"
print(features)

model.fit(train[features], train[target])
predictions = model.predict(test[features])
mse = mean_squared_error(predictions, test[target])
rmse = np.sqrt(mse)
print("rmse:", float(rmse))
print("mse", float(mse))
# print(predictions)



"""
Previous output of model with features below
['Open', 'High', 'Low', 'Volume', 'Adj Close', 'Avg 5 days', 'Avg 30 days', 'Std 5 days', 'Avg high-low']
2.0735552641700114e-10
4.2996314335671655e-20


['Open', 'High', 'Low', 'Volume', 'Adj Close', 'Avg 5 days', 'Avg 30 days']
2.077340593697352e-10
4.3153439422228663e-20



['Open', 'High', 'Low', 'Adj Close', 'Avg 5 days', 'Avg 30 days']
1.8649889116516263e-13
3.478183640583517e-26


['Open', 'High', 'Low', 'Adj Close', 'Avg 5 days', 'Avg 30 days', 'Std 5 days', 'Avg high-low']
rmse: 6.120883512998964e-13
mse 3.746521497970254e-25

['Open', 'High', 'Low', 'Adj Close', 'Avg 5 days', 'Avg 30 days', 'Std 5 days']
rmse: 1.5402307714779736e-12
mse 2.372310829407634e-24
"""

import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(data.corr())
plt.show()
data.corr()





"""
if we remove "Std 5 days" and "Avg high low" we would decrease rmse but what it would be in real data.
As for Linear Regression, i think here is would better fit ARIMA model.

As the results in multi-comment above we see that removing "Std 5 days" and "Avg high low" how it would effect on rmse w/o "Volume".
But after removal of Volume the most correlated feature we've dereased rmse succsessfully.
Now I would like to test with "Std 5 days" and "Avg high low" again.
"""