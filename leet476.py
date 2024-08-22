# Leetcode question 476: Number Compliment

def findComplement(num: int) -> int:
    # get the binary value of num
    binary_num = bin(num)[2:]
    # create binary_string to convert for compliment number
    binary_str = ""
    # loop through nums
    for n in binary_num:
        if n == '1':
            n = '0'
        else:
            n = '1'
        binary_str += n

    return int(binary_str, 2)


# Test Cases
print(findComplement(5))  # 2
print(findComplement(1))  # 0
