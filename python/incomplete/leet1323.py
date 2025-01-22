def maximum69Number(num: int) -> int:
        str_num = str(num)
        max_num = num  # Initialize with the original number

        # Iterate through each digit (index)
        for i in range(len(str_num)):
            # Create a temporary string with the digit at index 'i' swapped
            temp_num = str_num[:i] + ("9" if str_num[i] == "6" else "6") + str_num[i+1:]
            # Convert the temporary string back to integer
            temp_num = int(temp_num)
            # Update max_num if the temporary number is greater
            max_num = max(max_num, temp_num)

        return max_num


# Test Cases
print(maximum69Number(9669))
