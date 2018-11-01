# O(n)

import time
start = time.clock()
data = open("AviationData.txt","r").readlines()

aviation_data = [i.split(" | ") for i in data]
search_val = "LAX94LA336"
aviation_row2 = [i[2] for i in aviation_data]
lax_code = [aviation_data[i] for i in range(len(aviation_row2)) if search_val in aviation_row2[i]]


print(time.clock() - start)
print(lax_code)
       
