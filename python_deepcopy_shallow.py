# python deep copy and shallow copy 



# shallow copy changes booth the values  
# where deep copy only changes to the original value not others 

import copy

# Example list
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Shallow copy
shallow_copied_list = copy.copy(original_list)

# Deep copy
deep_copied_list = copy.deepcopy(original_list)

# Modifying the copied lists
shallow_copied_list[0][0] = 'a'  # Modifying a shallow copy
deep_copied_list[0][0] = 'b'     # Modifying a deep copy

# Printing original and copied lists
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)
print("Deep Copied List:", deep_copied_list)
