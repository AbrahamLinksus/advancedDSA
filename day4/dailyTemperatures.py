#to find relative temperatures using monotonic stacks 

#KEY TAKEAWAY: MONOTONIC STACKS 

input = [73, 74, 75, 71, 69, 72, 76, 73]
res = [0] * len(input)

stack = []

for index, value in enumerate(input):
    while stack and value > stack[-1][0]:
        stackTemperature, stackIndex = stack.pop()
        res[stackIndex] = (index - stackIndex)
    stack.append([value, index])
print(res)

