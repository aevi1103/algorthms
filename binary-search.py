import random
import math

random_list = []
max_n = 10
for i in range(0,max_n):
    n = random.randint(0,max_n)
    random_list.append(n)

find = random.choice(random_list)
random_list.sort()

mid_index = math.floor(len(random_list) / 2)
mid = random_list[mid_index]
temp_arr = random_list

while(mid_index > 0):
    if(find < mid):
        temp_arr = temp_arr[:mid_index]
    else:
        temp_arr = temp_arr[mid_index:]

    mid_index = math.floor(len(temp_arr) / 2)
    mid = temp_arr[mid_index]
    

print(f'arr: {random_list}')
print(f'find: {find}')
print(f'result: {temp_arr}')