import time
start = time.clock()
data = open("AviationData.txt","r").readlines()

aviation_data = [i.split(" | ") for i in data]
search_val = "LAX94LA336"

lax_code = [i for i in aviation_data if search_val in i]

print(time.clock() - start)
print(lax_code)
       
