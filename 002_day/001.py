def findSum():
    s = 0
    for v in range(1, 100000000000):
        s += v
    return s


def findSumOp(n):
    return (n * (n + 1)) / 2


print(findSumOp(10))
