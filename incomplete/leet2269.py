def iterate_number(num: int, k: int):
    num_str = str(num)  # Convert the number to a string
    length = len(num_str)  # Get the length of the string
    res = []
    for i in range(length - k + 1):
        # Extract a substring of length k
        substring = num_str[i:i+k]
        # Optionally, convert this substring back to an integer
        digit_group = int(substring)
        # append to res list
        res.append(digit_group)
    return len(res)


# Test Cases
print(iterate_number(240, 2))  # 2
print(iterate_number(430043, 2))  # 2
