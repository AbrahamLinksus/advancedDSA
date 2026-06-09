# to find the maximum of a window k in an array continuously

#KEY FINDING: MONOTONIC QUEUE
import collections

k = 3
nums = [1,2,1,0,4,2,6]
output = []
q = collections.deque()
l = r = 0

while r < len(nums):   
    while q and nums[q[-1]] < nums[r]:
        q.pop()
    q.append(r)

    if l > q[0]:
        q.popleft()
    
    if (r + 1) >= k:
        output.append(nums[q[0]])
        l += 1
    r += 1

print(output)