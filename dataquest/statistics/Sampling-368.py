## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
data = pd.read_csv('wnba.csv')
print(data.head())
print(data.tail())

parameter = data["Games Played"].max()

sample = data["Games Played"].sample(30, random_state=1)
statistic = sample.max()
sampling_error = parameter - statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('wnba.csv')

rng = list()
for i in range(100):
    rng.append(data["PTS"].sample(10,random_state=i).mean())
plt.scatter(range(1,101),rng)
plt.axhline(data["PTS"].mean())


## 7. Stratified Sampling ##

wnba['Pts_per_game'] = wnba["PTS"]/wnba["Games Played"]

strat = wnba["Pos"].unique()

points_per_position = dict()
for i in strat:
    sample = wnba["Pts_per_game"][wnba.Pos == i].sample(10, random_state=0)
    points_per_position[i] = sample.mean()
    
position_most_points = max(points_per_position, key=points_per_position.get)

## 8. Quota Sampling ##

under_12 = wnba[wnba['Games Played'] <= 12]
btw_13_22 = wnba[(wnba['Games Played'] > 12) & (wnba['Games Played'] <= 22)]
over_23 = wnba[wnba['Games Played'] > 22]

quota_sampling_means = []

for i in range(100):
    sample_under_12 = under_12['PTS'].sample(1, random_state = i)
    sample_btw_13_22 = btw_13_22['PTS'].sample(2, random_state = i)
    sample_over_23 = over_23['PTS'].sample(7, random_state = i)
    
    final_sample = pd.concat([sample_under_12, sample_btw_13_22, sample_over_23])
    quota_sampling_means.append(final_sample.mean())
    
plt.scatter(range(1,101), quota_sampling_means)
plt.axhline(wnba['PTS'].mean())

## 9. Choosing the Right Strata ##

wnba['MIN'].value_counts(bins = 3, normalize = True)

## 10. Cluster Sampling ##

cluster = pd.Series(wnba["Team"].unique()).sample(4,random_state=0)

data = pd.DataFrame()
for i in cluster:
    data =data.append(wnba[wnba["Team"] == i])
    


sampling_error_height = wnba["Height"].mean() - data["Height"].mean() 
sampling_error_age = wnba["Age"].mean() - data["Age"].mean() 
sampling_error_BMI = wnba["BMI"].mean() - data["BMI"].mean() 
sampling_error_points = wnba["PTS"].mean() - data["PTS"].mean() 