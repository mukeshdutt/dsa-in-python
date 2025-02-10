def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    
    return prefix

arr = [5, 6, 7, 10, 11, 21]
print(prefix_sum(arr))
