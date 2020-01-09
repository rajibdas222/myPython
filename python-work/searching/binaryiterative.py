def binarysearch(itemlist, key):
    low = 0
    high = len(itemlist)-1
    
    while low <= high:
        mid = (low+high)//2
        if key == itemlist[mid]:
            return True
        elif key < itemlist[mid]:
            high = mid-1
        else :
            low = mid +1 
            
    return False


itemlist = []
found = binarysearch(itemlist, 26)
print('The Element is :' , found )           