# O()

import time


start = time.clock()
data = open("AviationData.txt","r").readlines()
search_val = "LAX94LA336"

aviation_data = [i.split(" | ") for i in data]

header = aviation_data[0]
print(header)

aviation_dict_list = [dict(zip(header,i)) for i in aviation_data[1:]]
lax_dict = [i for i in aviation_dict_list if i.get('Accident Number') == search_val]

print(time.clock() - start)
print(lax_dict)
       
