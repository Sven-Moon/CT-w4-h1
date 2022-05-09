# Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.

# Hint: Linear Searching will require searching a list for a given number.

nums_list = [10,23,45,70,11,15]
target = 70

# If number is not present return -1
def linearSearch(arr, t):
    for i in range(len(arr)):
        if arr[i] == t:
            return i
    return -1
        
print(linearSearch(nums_list, target))

# Time Complexity: O(n), Θ(n/2)