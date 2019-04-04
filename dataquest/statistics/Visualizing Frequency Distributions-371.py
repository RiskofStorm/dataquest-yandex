## 2. Bar Plots ##

wnba["Exp_ordinal"].value_counts().iloc[[3,0,2,1,4]].plot.bar()
plt.show()

## 3. Horizontal Bar Plots ##

wnba["Exp_ordinal"].value_counts().iloc[[3,0,2,1,4]].plot.barh(title="Number of players in WNBA by level of experience")

## 4. Pie Charts ##

wnba["Exp_ordinal"].value_counts().plot.pie()

## 5. Customizing a Pie Chart ##


wnba['Exp_ordinal'].value_counts().plot.pie(figsize=(6,6),autopct="%.2f%%", title='Percentage of players in WNBA by level of experience')
plt.ylabel('')

## 6. Histograms ##

wnba["PTS"].plot.hist()

## 7. The Statistics Behind Histograms ##

wnba["Games Played"].describe()
wnba["Games Played"].plot.hist()

## 9. Binning for Histograms ##

wnba['Games Played'].plot.hist(range = (0,32), bins = 8, xticks = range(0,33,4),
                               title = 'The distribution of players by games played')
plt.xlabel('Games played')

## 10. Skewed Distributions ##

wnba["AST"].plot.hist()
plt.show()
wnba["FT%"].plot.hist()
plt.show()

assists_distro = "right skewed"
ft_percent_distro = "left skewed"



## 11. Symmetrical Distributions ##

wnba["Age"].plot.hist()
plt.show()
wnba["Height"].plot.hist()
plt.show()
wnba["MIN"].plot.hist()
plt.show()

normal_distribution = "Height" 