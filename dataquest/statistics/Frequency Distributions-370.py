## 1. Simplifying Data ##

import pandas as pd

pd.options.display.max_rows = 200
pd.options.display.max_columns = 50

data = pd.read_csv("wnba.csv")
print(data.shape)
print(data)

## 2. Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')

freq_distro_pos =  wnba["Pos"].value_counts()
freq_distro_height = wnba["Height"].value_counts()

## 3. Sorting Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
age_ascending = wnba["Age"].value_counts().sort_index()
age_descending = wnba["Age"].value_counts().sort_index(ascending=False)


## 4. Sorting Tables for Ordinal Variables ##

def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'
    
   
    
wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)

ind = ['very few points','few points', 'many, but below average','average number of points','more than average','much more than average']

# Type your answer below
pts_ordinal_desc = wnba['PTS_ordinal_scale'].value_counts()[ind[::-1]]


## 5. Proportions and Percentages ##

wnba = pd.read_csv('wnba.csv')

proportion_25 = (wnba["Age"][wnba["Age"] == 25]/wnba.shape[0]).round(2)
percentage_30 = (wnba["Age"][wnba["Age"] == 30]/wnba.shape[0]).round(2) * 100
percentage_over_30 = (wnba["Age"][wnba["Age"] >= 30]/wnba.shape[0]).round(2) * 100
percentage_below_23 = (wnba["Age"][wnba["Age"] <= 23]/wnba.shape[0]).round(2) * 100

## 6. Percentiles and Percentile Ranks ##

from scipy.stats import percentileofscore

wnba = pd.read_csv('wnba.csv')

percentile_rank_half_less = percentileofscore(wnba["Games Played"], 17, kind='weak')
percentage_half_more = 100 - percentile_rank_half_less

## 7. Finding Percentiles with pandas ##

wnba = pd.read_csv('wnba.csv')
age_upper_quartile = wnba["Age"].describe()[6]
age_middle_quartile = wnba["Age"].describe()[5]
age_95th_percentile = wnba["Age"].describe(percentiles=[.95])[5]

question1 = True
question2 = False
question3 = True


## 8. Grouped Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')

grouped_freq_table = wnba["PTS"].value_counts(bins=10, normalize=True).sort_index(ascending=False) * 100

## 10. Readability for Grouped Frequency Tables ##

wnba = pd.read_csv('wnba.csv')
interval = pd.interval_range(start=0,end=600,freq=60)
gr_freq_table_10 = pd.Series([0 for _ in range(10)], index= interval)

for row in wnba["PTS"]:
    for i in interval:
        if row in i:
            gr_freq_table_10.loc[i] +=1
            break