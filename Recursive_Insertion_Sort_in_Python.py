# Idea of Insertion Sort

# We divide the given array into two parts i.e Sorted sub-list and Unsorted sub-list.
# Initially in the sorted sub-list single element is kept and then,
# from the unsorted sub-list we pick every element and insert it at the
# correct position in the sorted sub-list.
# This way we achieve our sorted sub-list.

# Recursion Idea
# 1) BASE CASE : If array size is less than or equal to 1, return None.
# 2) Sorting recursively the first n-1 elements.
# 3) Inserting the last element at its correct position in sorted array.


# Creating the recursive function for Insertion Sort.

def RecursiveInsertionSort(array, n):
    # Base Case
    # If the size of array is less than or equal to 1, we return None.
    if n<=1:
        return None
    # Sorting the first n-1 elements recursively.
    RecursiveInsertionSort(array, n-1)

    # Inserting the last element at its correct position in sorted array.

    # Storing the last element in a temporary variable.
    temp = array[n-1]

    # Assigning the index of the element previous to the element stored in temporary variable.
    j = n-2

    # Now, moving the elements of array[0,1,......i-1], that are greater
    # than the element stored in temporary variable to one position ahead of their
    # current position.

    while j>=0 and array[j] > temp:
        array[j+1] = array[j]
        j -= 1

    array[j+1] = temp

# Creating a utility function to print the elements of array of size n.

def Arrayprint(array, n):
    for i in range(n):
        print(array[i], end = " ")

# Taking the list(array) of elements as input from the user.
Array = list(map(int, input("Enter the unsorted array elements : ").split()))

# Finding the length of the input array.
length = len(Array)

# Calling the Recursive Insertion Sort Function
# and passing the input array and its length as parameters.

RecursiveInsertionSort(Array,length)

# Calling the Array print function for printing the elements of sorted elements
print("Sorted Elements : ")
Arrayprint(Array, length)
