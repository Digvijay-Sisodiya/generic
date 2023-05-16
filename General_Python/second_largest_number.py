"""
- Find second largest number in an input
- Time Complexity: O(n), where n is the length of the input list.
"""
def second_largest_number(input_list):
    largest = None
    second_largest = None
    for i in input_list:
        if largest is None or i > largest:
            second_largest = largest
            largest = i
        elif second_largest is None or i > second_largest:
            second_largest = i
    return second_largest
n = [1,2,4,2,1,4,7]
numbers = second_largest_number(n)
print(numbers)