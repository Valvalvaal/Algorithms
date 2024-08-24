def countdown(n:int):
    print(n)
    if n<= 0:
        print('Go')
    else:
        countdown(n-1)

#countdown(15)

def fact(x:int):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

#fact(3)

def array_sum(arr:list):
    if arr == []:
        return 0
    return arr[0] + array_sum(arr[1:])

array_sum([0,9,583,4,5,6,7,8,9,21])

# Function to count number of items in a list
def count(arr:list):
    if arr == []:
        return 0
    return 1 + count(arr[1:])

count([3,2])

def array_max(arr:list):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = array_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

array_max([0,-1,-4,9])