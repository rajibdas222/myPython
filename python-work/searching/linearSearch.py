def binarysearch(itemlist, item):
    first=0
    last=len(itemlist)-1
    found=False
    
    while(first<=last and not found):
        mid=(first+last)//2
        if(itemlist[mid] == item):
            found = True 
            
        else:
            if item<itemlist[mid]:
                last=mid-1
            else:
                first=mid+1
                
                
    if found ==True:
        print("Item found :" , item)
    else:
        print(" Sorry !!! item not found in list")                
                    
    return 0


dlist1 =[40,41,42,43,44,45,46,47,48,49,50]
dlist2 =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
dlist3 =[61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
dlist4 =[21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]

binarysearch(dlist3, 88)