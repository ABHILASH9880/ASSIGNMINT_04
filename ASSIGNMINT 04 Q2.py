triple = lambda x : x * 3
length= int(input("enter the list  :"))
list1 = []

for _ in range (length):
    temp = int(input("enter list item:"))
    list1.append(temp)

list2= list(map(triple,list1))

print("original list is :", list1)
print("triple of given list is :", list2)
