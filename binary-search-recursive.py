from operator import truediv
import random
import math

random_list = []
max_n = 10
for i in range(0,max_n):
    n = random.randint(0,max_n)
    random_list.append(n)

find = random.choice(random_list)
random_list.sort()

def binary_search(arr, target):
    mid_index = math.floor(len(arr) / 2)
    mid = arr[mid_index]

    if (mid == target):
        return 'Found it'

    if (mid_index == 0):
        return 'Not found'

    if (target < mid):
        return binary_search(arr[:mid_index], target)
    else:
        return binary_search(arr[mid_index:], target)
        
test_arr = [1,2,3,4,5,6,7,8,9]
found = binary_search(test_arr, 6)
print(found)