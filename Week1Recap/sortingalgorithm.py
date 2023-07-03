from random import randint
unsorted_list = [randint(0, 100) for i in range(10)]

n = len(unsorted_list)

for i in range(n):
    sorted = True
    for j in range(n - i - 1):
        if(unsorted_list[j] > unsorted_list[j+1]):
            unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
            sorted = False
    if sorted:
        break
print(unsorted_list)
    
