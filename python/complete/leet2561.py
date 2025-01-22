def findDelayedArrivalTime(arrivalTime: int, delayedTime: int) -> int:
    # combine arrival and delayed time
    total_time = arrivalTime + delayedTime
    # check if total time is greater or equal to 24
    if total_time >= 24:
        # if true, subtract 24 to adhere to 24 hour time
        total_time -= 24
    return total_time


# Test Cases
print(findDelayedArrivalTime(15, 5))  # 20
print(findDelayedArrivalTime(13, 11))  # 0
print(findDelayedArrivalTime(1, 24))  # 1
