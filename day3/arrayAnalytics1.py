arr = [1,2,3,4,6]

def kadane(arr):
    current = arr[0]
    best = arr[0]
    for index in range(1, len(arr)):
        current = max(arr[index], current + arr[index])
        best = max(current, best)
    return best

def equillibriumIndex(arr):
    sum = 0
    for element in arr:
        sum += element
    rsum, lsum = sum, 0
    for index in range(len(arr)):
        rsum -= arr[index]
        if rsum == lsum:
            return index
        lsum += arr[index]
    
    return "invalid"


print("Max subarray sum =",kadane(arr))
print("Equilibrium Index =",equillibriumIndex(arr))