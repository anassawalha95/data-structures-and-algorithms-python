def reverse_array(arr):
    """Reverses a list

    Args:
        arr (list): python list

    Returns:
        [list]: list in reversed form
    """
    # put your function implementation here
    lst = [] #1
    for i in range(len(arr)-1,-1,-1): #n
        lst.append(arr[i]) #n-1
    
    return lst #1

print(reverse_array([1, 2, 3, 4, 5, 6]))

def reverse_array_2(arr):
    newLst = arr[::-1]
    return newLst

print(reverse_array_2([89, 2354, 3546, 23, 10, -923, 823, -12]))