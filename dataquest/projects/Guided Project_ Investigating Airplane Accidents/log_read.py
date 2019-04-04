# O(logn)

import time
import bisect

start = time.clock()
data = open("AviationData.txt","r").readlines()

aviation_data = [i.split(" | ") for i in data]
aviation_data = sorted(aviation_data, key=lambda i:i[2])

search_val = "LAX94LA336"
aviation_row2 = [i[2] for i in aviation_data]
lax_code = aviation_data[bisect.bisect_left(aviation_row2, search_val)]

print(time.clock() - start)
print(lax_code)
       
