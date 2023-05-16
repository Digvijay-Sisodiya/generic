"""
- Remove the duplicates from given list.
- Case-1: Input list is integer
- Case-2 : Input list is string
"""
def remove_duplicates_from_int_list(input_list):
    """
    - Time Complexity is O(n) where n is the length of input list
    """
    return [*set(input_list)]

def remove_duplicates_from_str_list(input_list):
    """
    - Time Complexity is O(n * m)
    - Where n is the length of s1 and m is the number of unique elements in s1.
    """
    final_list=[]
    for i in input_list:
        if i not in final_list:
            final_list.append(i)
    return [*final_list]

input_1 = [1,2,4,2,1,4,7]
final_list = remove_duplicates_from_int_list(input_1)
input_2 = "digvijay"
str_final_list = remove_duplicates_from_str_list(input_2)
print(final_list)
print(str_final_list)
