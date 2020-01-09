def max_of_two(x, y):
    if x > y:
        return x
    return y


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))   


print("The max of three :" , max_of_three(3, 6, -5))


def sumtot(numbers):
    total = 0
    for x in numbers:
        total += x
    return  total


print(sumtot((8, 2, 3, 0, 7)))  

# #Tuple
x = ()
print(x)
tuplex = tuple()
print(tuplex)

# create tuple with numbers
tuplex = 5, 10, 12, 23, 45
print(tuplex)
tuplex = 5,
print(tuplex)

  
