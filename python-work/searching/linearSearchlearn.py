def linearsearch(A, key):
    
    position = 0
    flag = False
    
    while position < len(A) and not flag:
        if A[position] == key:
            flag = True
            
        else:
            position = position + 1
    return flag            

A = [84,21,54,34,90,22,67,95]
found = linearsearch(A, 84)

print("Element is present : ",found)





        
    

