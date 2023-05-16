# Remove the duplicates from given list
def remove_duplicates_from_int_list(input_list):
    # Case-1
    # Input list is integer
    # Time Complexity is O(n) where n is the length of input list
    return [*set(input_list)]

def remove_duplicates_from_str_list(input_list):
    # Case-2
    # input list is string
    # Time Complexity is O(n * m), where n is the length of s1 and m is the number of unique elements in s1.
    final_list=[]
    for i in input_list:
        if i not in final_list:
            final_list.append(i)
    return [*final_list] # D i g v j a y

s = [1,2,4,2,1,4,7]
final_list = remove_duplicates_from_int_list(s)
# s1 = ['D','I','G','V','I','J','A','Y']
s1 = "Digvijay"
str_final_list = remove_duplicates_from_str_list(s1)
print(final_list)
print(str_final_list)
