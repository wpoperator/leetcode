from collections import Counter


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    # Use Counter to create frequency dictionaries for both lists
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)

    # Find the intersection using dictionary comprehension
    intersection = [element for element, count in (counter1 & counter2).items() for _ in range(min(count, counter1[element]))]

    return intersection


# Test Cases
print(intersect([1, 2, 2, 1], [2, 2]))  # [2, 2]
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [4, 9]
