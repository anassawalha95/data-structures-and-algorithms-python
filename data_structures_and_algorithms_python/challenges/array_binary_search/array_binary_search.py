# def BinarySearch(lst,num):
#     idx = len(lst)// 2 # 2
#     match = -1
#     if num < lst[idx]:
#         for i in range(idx,-1,-1):
#             # print('this iiiiiiii',i)
#             if lst[i] == num:
#                 # print(lst[i])
#                 match = i
            
#     if num > lst[idx]:
#         for i in range(idx,len(lst),1):
#             if lst[i] == num:
#                 match = i
#     if num == lst[idx]:
#         match = idx
#     return match

# print(BinarySearch([1,2,3,4,5],4))

# Python3 Program for recursive binary search. 
  
# Returns index of x in arr if present, else -1 

def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
result = binarySearch(arr, 0, len(arr)-1, x) 
  