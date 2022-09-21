# binsearch.py
# Kiana Herr
# CSCI 77800 Fall 2022
# collaborators: N/A
# consulted: N/A

def binsearch_r(data, target, lo = 0, hi = None):
    '''
    binsearch_r(data, target, lo = 0, hi = None)

    Takes a sorted list 'data' and a target value 'target.'
    Returns the index of 'target' using a recursive binary search.
    If 'target' is not present, returns -1.

    If the data is not a sorted list, prints a message and returns -1.

    list data: a sorted list of values.
    int target: the value to search for.
    lo: an optional argument for the "low" index to check in the
        current iteration of the binary search. Defaults to 0.
    hi: an optional argument for the "high" index to check in the
        current iteration of the binary search. Defaults to 
        len(data) - 1.
    '''
    if not(all(data[i] <= data[i + 1] for i in range(len(data) - 1))):
        print("List is not sorted. Returning -1.")
        return -1
    else:
        if hi is None:
            hi = len(data) - 1
        if hi < lo:
            return -1
        else:
            mid = (lo + hi) // 2
            if data[mid] == target:
                return mid
            elif target > data[mid]:
                # must call with current value of hi
                return binsearch_r(data, target, lo = mid + 1, hi = hi)
            else:
                # must call with current value of lo
                return binsearch_r(data, target, lo = lo, hi = mid - 1)

def binsearch(data, target):
    '''
    binsearch_r(data, target)

    Takes a sorted list 'data' and a target value 'target.'
    Returns the index of 'target' using a binary search.
    If 'target' is not present, returns -1.

    If the data is not a sorted list, prints a message and returns -1.

    list data: a sorted list of values.
    int target: the value to search for.
    '''
    if not(all(data[i] <= data[i + 1] for i in range(len(data) - 1))):
        print("List is not sorted. Returning -1.")
        return -1 
    lo = 0
    hi = len(data) - 1
    location = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] == target:
            location = mid
            return location
        elif target > data[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

print("Testing recursive binsearch:")
test = list(range(0, 11))
print("Search a list from 0 to 10 for 3")
print(binsearch_r(test, 3))
print("Search a list from 0 to 10 for 10")
print(binsearch_r(test, 10))
print("Search a list from 0 to 10 for 20")
print(binsearch_r(test, 20))
test1 = list(range(11, 0, -1))
print("Trigger 'not sorted' message by passing a decreasing list:")
print(binsearch_r(test1, 3))

print("\nTesting iterative binsearch:")
print("Search a list from 0 to 10 for 3")
print(binsearch(test, 3))
print("Search a list from 0 to 10 for 10")
print(binsearch(test, 10))
print("Search a list from 0 to 10 for 20")
print(binsearch(test, 20))
print("Trigger 'not sorted' message by passing a decreasing list:")
print(binsearch(test1, 3))