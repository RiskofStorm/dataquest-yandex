## 2. Overview of the Data ##

import pandas as pd
submissions = pd.read_csv("sel_hn_stories.csv")
submissions.columns = ["submission_time", "upvotes", "url", "headline"]
submissions = submissions.dropna()


## 3. Tokenizing the Headlines ##

tokenized_headlines = []
for i in submissions['headline']:
    tokenized_headlines.append(i.split())

## 4. Preprocessing Tokens to Increase Accuracy ##

punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []
for i in tokenized_headlines:
    tokens = []
    for token in i:
        for punc in punctuation:
            token = token.lower().replace(punc,"")
        tokens.append(token)
    clean_tokenized.append(tokens)

## 5. Assembling a Matrix of Unique Words ##

import numpy as np
unique_tokens = []
single_tokens = []

unique_tokens = set([item for row in clean_tokenized for item in row])
counts = pd.DataFrame(0,index=np.arange(len(clean_tokenized)), columns=unique_tokens)


## 6. Counting Token Occurrences ##

# We've already loaded in clean_tokenized and counts
for ind,row in enumerate(clean_tokenized):
    for token in row:
        if token in unique_tokens:
            counts.iloc[ind][token] +=1
            
    


## 7. Removing Columns to Increase Accuracy ##

# We've already loaded in clean_tokenized and counts
word_counts = counts.sum(axis=0)
counts = counts.loc[:, (word_counts>= 5) & (word_counts <= 100)]



## 8. Splitting the Data Into Train and Test Sets ##

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(counts, submissions["upvotes"], test_size=0.2, random_state=1)

## 9. Making Predictions With fit() ##

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train,y_train)
predictions = model.predict(X_test)


## 10. Calculating Prediction Error ##

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test,predictions)