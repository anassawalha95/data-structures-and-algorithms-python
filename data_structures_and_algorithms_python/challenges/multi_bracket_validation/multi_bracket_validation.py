
def multi_bracket_validation(str_input):
    """
    function take a string as its only argument, and return a boolean representing whether or 
    not the brackets in the string are balanced.
    """
    open_list = ["[","{","("] 
    close_list = ["]","}",")"] 
    
    lst = [] 
    for i in str_input: 
        if i in open_list: 
            lst.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(lst) > 0) and
                (open_list[pos] == lst[len(lst)-1])): 
                lst.pop() 
            else: 
                return False
    if len(lst) == 0: 
        return True
    else: 
        return False