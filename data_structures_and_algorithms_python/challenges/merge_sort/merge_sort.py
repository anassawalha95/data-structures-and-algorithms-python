def merge_sort(myList):

    if len(myList) > 1:
        mid = len(myList) // 2
        
        left = myList[:mid]
        right = myList[mid:]
        # print(left)
        # print(right)
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1
        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

    return myList

if __name__ == "__main__":
    arr = [8,4,23,42,16,15,1]
    print(merge_sort(arr))
