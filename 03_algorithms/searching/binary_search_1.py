import random

def binary_search_recursive(inputs, target_search, low, high):
    # check if there are values
    if low > high:
        return -1

    # get the middle index and round it off
    mid = (low + high) // 2
    print(f"The low element is {values[low]}")
    print(f"The high element is {values[high]}")
    print(f"The middle element is {values[mid]} \n")

    if inputs[mid] == target_search:
        return mid
    elif inputs[mid] < target_search:
        return binary_search_recursive(inputs, target_search, mid + 1, high)
    else:
        return binary_search_recursive(inputs, target_search, low, mid - 1)


# Generate 10 random integers between 1 and 100
values = sorted([random.randint(1, 100) for _ in range(10)])

# check the data type
print(f"{type(values)}")
print("Ordered:", values)

target = int(input("Enter number to search : "))

# start the function
result = binary_search_recursive(values, target, 0, len(values) - 1)

# result
if result != -1:
    print(f"Value {values[result]} found at index {result}")
else:
    print(f"Value {target} not found in the list")
