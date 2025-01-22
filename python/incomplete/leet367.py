# Leetcode question 367: Valid perfect square

def isPerfectSquare(num: int) -> bool:
    # boolean value to return
    perfect = False
    # result number at zero for while loop
    result = 0
    # new variable equal to num to perform loop operations
    new_num = num
    # test case if num = 1
    if num == 1:
        return True
    # loop until conditions are met
    while result != num:
        # current is new_num with floor division by 2
        current = new_num // 2
        # if current does not evenly divide, it will never be a sqrt
        if current % 2 != 0:
            # break out of loop and return default perfect value as False
            break
        # multiply the current value by itself and compare to original num value
        elif current * current != num:
            # if current is not equal to num, assign new_num the value of current to continue loop
            new_num = current
            continue
        # once current is equal to num, a square root has been found
        else:
            # change perfect to True as square root has been found
            perfect = True
            # break out of loop
            break
    # Return perfect
    return perfect


# Test Cases
print(isPerfectSquare(16))  # True
print(isPerfectSquare(14))  # False
