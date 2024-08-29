# Leetcode question 412: FizzBuzz

def fizzBuzz(n: int) -> list[str]:
    # return list
    my_list = []
    # loop starting from 1 to n + 1 to stay in bounds
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            my_list.append("FizzBuzz")
        elif i % 5 == 0:
            my_list.append("Buzz")
        elif i % 3 == 0:
            my_list.append("Fizz")
        else:
            my_list.append(str(i))
    return my_list


# Test Cases
print(fizzBuzz(3))  # ['1', '2', 'Fizz']
print(fizzBuzz(5))  # ['1', '2', 'Fizz', "4", "Buzz"]
print(fizzBuzz(15))  # ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
