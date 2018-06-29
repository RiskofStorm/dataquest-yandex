## 1. Recap ##

import pandas as pd

loans = pd.read_csv('cleaned_loans_2007.csv')
print(loans.info())

## 3. Picking an error metric ##

import pandas as pd

true_neg = (loans['loan_status']==0) &  (predictions==0)
false_neg = (loans['loan_status']==1) &  (predictions==0)
true_pos = (loans['loan_status']==1) &  (predictions==1)
false_pos = (loans['loan_status']==0) &  (predictions==1)

tn = len(predictions[true_neg])
tp = len(predictions[true_pos])
fn = len(predictions[false_neg])
fp = len(predictions[false_pos])


## 5. Class imbalance ##

import pandas as pd
import numpy

# Predict that all loans will be paid off on time.
predictions = pd.Series(numpy.ones(loans.shape[0]))
# False positives.
fp_filter = (predictions == 1) & (loans["loan_status"] == 0)
fp = len(predictions[fp_filter])

# True positives.
tp_filter = (predictions == 1) & (loans["loan_status"] == 1)
tp = len(predictions[tp_filter])

# False negatives.
fn_filter = (predictions == 0) & (loans["loan_status"] == 1)
fn = len(predictions[fn_filter])

# True negatives
tn_filter = (predictions == 0) & (loans["loan_status"] == 0)
tn = len(predictions[tn_filter])


tpr = tp/(tp+fn)
fpr = fp/(fp+tn)

print(tpr)
print(fpr)

## 6. Logistic Regression ##

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

features = loans.drop("loan_status",axis=1)
target = loans["loan_status"]

lr.fit(features,target)
predictions = lr.predict(features)

## 7. Cross Validation ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
lr = LogisticRegression()

predictions = pd.Series(cross_val_predict(lr,features,target,cv=3))
true_pos = (predictions==1)&(loans["loan_status"])
false_pos = (predictions==1)&(loans["loan_status"])
tp,fp = loans[true_pos], loans[false_pos]

tpr = tp/(tp+fn)
fpr = fp/(fp+tn)
print(tpr)
print(fpr)


## 9. Penalizing the classifier ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict

lr = LogisticRegression(class_weight='balanced')
predictions = pd.Series(cross_val_predict(lr,features,target))
# False positives.
fp_filter = (predictions == 1) & (loans["loan_status"] == 0)
fp = len(predictions[fp_filter])

# True positives.
tp_filter = (predictions == 1) & (loans["loan_status"] == 1)
tp = len(predictions[tp_filter])

# False negatives.
fn_filter = (predictions == 0) & (loans["loan_status"] == 1)
fn = len(predictions[fn_filter])

# True negatives
tn_filter = (predictions == 0) & (loans["loan_status"] == 0)
tn = len(predictions[tn_filter])

tpr = tp/(tp+fn)
fpr = fp/(fp+tn)

print(tpr)
print(fpr)


## 10. Manual penalties ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict

penalty = {
    0:10,
    1:1
}
lr = LogisticRegression(class_weight=penalty)
predictions = pd.Series(cross_val_predict(lr,features,target))
# False positives.
fp_filter = (predictions == 1) & (loans["loan_status"] == 0)
fp = len(predictions[fp_filter])

# True positives.
tp_filter = (predictions == 1) & (loans["loan_status"] == 1)
tp = len(predictions[tp_filter])

# False negatives.
fn_filter = (predictions == 0) & (loans["loan_status"] == 1)
fn = len(predictions[fn_filter])

# True negatives
tn_filter = (predictions == 0) & (loans["loan_status"] == 0)
tn = len(predictions[tn_filter])

tpr = tp/(tp+fn)
fpr = fp/(fp+tn)

print(tpr)
print(fpr)

## 11. Random forests ##

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_predict


rf = RandomForestClassifier(random_state=1,class_weight='balanced')
predictions = pd.Series(cross_val_predict(rf,features,target))
# False positives.
fp_filter = (predictions == 1) & (loans["loan_status"] == 0)
fp = len(predictions[fp_filter])

# True positives.
tp_filter = (predictions == 1) & (loans["loan_status"] == 1)
tp = len(predictions[tp_filter])

# False negatives.
fn_filter = (predictions == 0) & (loans["loan_status"] == 1)
fn = len(predictions[fn_filter])

# True negatives
tn_filter = (predictions == 0) & (loans["loan_status"] == 0)
tn = len(predictions[tn_filter])

tpr = tp/(tp+fn)
fpr = fp/(fp+tn)

print(tpr)
print(fpr)