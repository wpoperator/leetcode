# Leetcode question 1614: Maximum Nesting Depth of the Parentheses

def maxDepth(s: str) -> int:
    # Variable to count outer parenthesis
    count = 0

    # Variable to track maximum depth
    max_depth = 0

    # loop through s
    for char in s:
        if char == '(':
            # Increase count for any instance '('
            count += 1
            # Separate count of highest number between count and max_depth
            max_depth = max(max_depth, count)
        elif char == ')':
            # Decrease count for any instance of ')'
            count -= 1

    return max_depth


# Test Cases
print(maxDepth("(1+(2*3)+((8)/4))+1"))  # 3
print(maxDepth("(1)+((2))+(((3)))"))  # 3
print(maxDepth("()(())((()()))"))  # 3
