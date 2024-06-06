def maximum69Number(num: int) -> int:
    # convert num to str to iterate through
    str_num = str(num)
    # number as string value
    string_num = ""
    # list to append each num after increasing/decreasing by 3
    # max_list = []
    # loop
    for n in range(len(str_num)):
        if n == "9":
            n = 3


# Test Cases
print(maximum69Number(9969))
