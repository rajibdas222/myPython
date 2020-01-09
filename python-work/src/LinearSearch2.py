def linear_search(values, item):
    Loc = 0
    search_result = False

    while Loc < len(values) and search_result is False:
        if values[Loc] == item:
            search_result = True
        else:
            Loc = Loc + 1
    if search_result == True:
        print("Item found at Location No is : ",Loc)
    else:
        print ("Item Not Found")
    return 0
        
        
data1 = [64, 34, 25, 12, 22, 11, 90]
linear_search(data1, 12)
linear_search(data1, 92)

