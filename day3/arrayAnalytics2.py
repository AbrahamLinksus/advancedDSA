arr = [-3,5,-2,5,-3]
def max_subarray_sum(arr):
    max_so_far = arr[0]
    current = arr[0]
    for i in range(1, len(arr)):
        current = current + arr[i]
        max_so_far = max(max_so_far, current)
    return max_so_far

def equilibrium_index(arr):
    return 0


print(max_subarray_sum(arr))