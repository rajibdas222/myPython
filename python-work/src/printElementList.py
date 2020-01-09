# marks = ['Chemistry',56,98,34,76,88,52,20,48,63,76]
# name = [ 'Ashik', 'Kamal', 'Poly', 'Jahan', 'Motin', 'Mollika', 'Joni', 'Omar', 'Kader', 'Afroz']
# print(marks[0], marks[5], name[5])
# for a in range(1,11):
#     print(marks[a])
# print(name[2:6])



#Update list
marks = [ 'Chemistry', 56, 98, 34, 76, 88, 52, 20, 48, 63, 76 ]
name = [ 'Ashik', 'Kamal', 'Poly', 'Jahan', 'Motin', 'Mollika', 'Joni', 'Omar', 'Kader', 'Afroz']
print("Before Updating:")
print(marks[0:11])
print(name[0:11])
#Update marks[0] and name[7]
marks[0]="Physics"
name[7] = "Akber"
print("After Updating:")
print(marks[0:11])
print(name[0:10])




#Delete List
print("========================== Delete list Array   =========================")
MarksD = [ 'Chemistry', 56, 98, 34, 76, 88, 52, 20, 48, 63, 76 ]
NameD = [ 'Ashik', 'Kamal', 'Poly', 'Jahan', 'Motin', 'Mollika', 'Joni', 'Omar', 'Kader', 'Afroz']
print("------------Before updating :---------------")
print(MarksD[0:11])
print(NameD[0:10])
#Delete marks[2:5] and name[4]
del MarksD[2:5]
del NameD[4]
print("===========After Deleting: ==============")

print(MarksD[0:10])
print(NameD[0:9])




























