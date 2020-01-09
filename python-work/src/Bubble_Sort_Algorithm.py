def bubbleSort(nList):
    for passnum in range(len(nList)-1,0,-1):
        for i in range(passnum):
            if nList[i]>nList[i+1]:
                temp = nList[i]
                nList[i] = nList[i+1]
                nList[i+1] = temp
                
                
nList = [14, 46, 27,18,53,67,10,78,23,89]
bubbleSort(nList)
print(nList)                