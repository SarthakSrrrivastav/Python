# Check if the first and last number of a list is the same

print("Size of list : ")
size=int(input("size"))
li=[]
for i in range(size):
    li.append(input("Input: "))

    
    
print(li)

if(li[0]==li[size-1]):
    print("First and last element is Same")
else:
    print("First and last element is not Same")
