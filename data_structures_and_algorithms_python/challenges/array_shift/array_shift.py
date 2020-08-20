def insertShiftArray(lst,n):
    
    if len(lst) %2 == 0:
        return lst[:len(lst)//2] + [n] + lst[len(lst)//2:]
    else:
        midpoint = (len(lst)//2) + 1
        return lst[0:midpoint] + [n] + lst[midpoint:]
