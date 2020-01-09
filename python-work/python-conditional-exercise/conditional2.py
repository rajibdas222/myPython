for x in range(12):
    if (x==5 or x==9):
        continue
    print(x,end='')
print("\n") 


#Fibonacci series between 0 t0 50

x,y=0,1 

while y<50:
    print(y)
    x,y = y,x+y  