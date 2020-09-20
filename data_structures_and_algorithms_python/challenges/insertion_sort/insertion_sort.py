
def insertion_sort(lst):
    """
    Function receives a list and return it sorted.
    """
  for i in range(1,len(lst),1):
    j = i-1 
    temp = lst[i]

    while j >=0 and temp < lst[j]:
         
      lst[j+1] = lst[j]
      j = j-1

    lst[j+1] = temp

  return lst

if __name__ == "__main__":
    # lst = [8,4,23,42,16,15]
    # lst = [20,18,12,8,5,-2]
    # lst = [5,12,7,5,5,7]
    lst = [2,3,5,7,13,11]
    print(insertion_sort(lst))    