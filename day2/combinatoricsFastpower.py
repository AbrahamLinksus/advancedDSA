n = 5
r = 2
base = 3
exp = 13
mod = 7
p = 17
q = 5

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n-2))

def pascal(n):
    res = []
    val = 1
    for i in range(n+1):
        res.append(int(val))
        val = val * ((n - i)/(i+1))
    res = [str(i) for i in res]
    res = " ".join(res)
    return res

def fastPower(base, exp, mod):
    def baseExp(base, exp):
        if exp == 0:
            return 1
        res = baseExp(base, exp // 2)
        if exp % 2 == 0:
            return res * res
        else:
            return res * res * base

    return baseExp(base, exp) % mod
    
print("Factorial =",factorial(n))
print("nCr =", int(nCr(n, r)))
print("Pascal Row =", pascal(n))
print("Fast Power =", fastPower(base, exp, mod))
