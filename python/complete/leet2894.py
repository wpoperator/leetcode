# Lettcode question 2894: Divisible and Non-divisible Sums Difference

def differenceOfSums(n: int, m: int) -> int:
    # create sum list for n
    n_sumlist = []
    # create sum list for m
    m_sumlist = []
    # loop through each value from 1 to n
    for i in range(n + 1):
        # if i does not divide evenly into m, append i to n_sumlist
        if i % m != 0:
            n_sumlist.append(i)
        # if i evenly divides into m, append i to m_sumlist
        else:
            m_sumlist.append(i)
    # return the difference between each sublist
    return sum(n_sumlist) - sum(m_sumlist)


# Test Cases
print(differenceOfSums(10, 3))  # 19
print(differenceOfSums(5, 6))  # 15
print(differenceOfSums(5, 1))  # -15
