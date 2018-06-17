def sum(arr):
    sum = sum_recursive(arr, 0)
    print(sum)
     
def sum_recursive(arr, index):
    if index == len(arr):
        return 0
    if index == len(arr) - 1:
        return arr[index]
    else:
        return arr[index] + sum_recursive(arr, index + 1)
    
sum([4])
    