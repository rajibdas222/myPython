
def quick_sort(collection):
    length = len(collection)
    if length <= 1:
        return collection
    else:
        #use the last element as the first pivot
        
        pivot = collection.pop()
        
        greater, lesser = [],[]
        
        for element in collection:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)
                
        return quick_sort(lesser) + [pivot] + quick_sort(greater)   
    
    
if __name__ == "__main__":
    
    user_input = input("Enter numbers separated by a comm:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(quick_sort(unsorted))              