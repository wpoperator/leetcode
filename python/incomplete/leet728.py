def selfDividingNumbers(left: int, right: int) -> list[int]:
    res = []
    for i in range(left, right):
        if left % i == 0 and right % i == 0:
            res.append(i)
    return res


# Test Cases
print(selfDividingNumbers(1, 22))
