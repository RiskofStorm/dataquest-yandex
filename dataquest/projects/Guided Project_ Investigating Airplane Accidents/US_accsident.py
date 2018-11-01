# O()

import time
from collections import Counter


start = time.clock()
data = open("AviationData.txt","r").readlines()
filter_val = 'Location'

aviation_data = [i.split(" | ") for i in data]

aviation_loc_list = [i[4] for i in aviation_data]
print(aviation_loc_list[0])
location_count = Counter(aviation_loc_list)
name = location_count.most_common(1)
print(time.clock() - start)
print(name)

start = time.clock()
data = open("AviationData.txt","r").readlines()
filter_val = 'Event Date'

aviation_data = [i.split(" | ") for i in data]
aviation_date_list = [i[3].split("/")[0] for i in aviation_data[1:]]

month_count = dict(Counter(aviation_date_list))
month_count.pop('', None)
moths_data = [v for k,v in sorted(month_count.items())]

month_names = ["jan", "feb", "mar", "apr", "may", "june","jule", "aug", "sep", "oct","nov","dec"]
monthly_injuries  = list(zip(month_names, moths_data))
    
print(time.clock() - start)
print(monthly_injuries )
    

