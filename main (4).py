#Function to check if a number is present in the list or not
def linearSearch(num,list1):
 for i in range(0,len(list1)):
  if list1[i] == num: #num is present
    return i #return the position
 return None #num is not present in the list
#end of function
list1 = [] #Create an empty list
print("How many numbers do you want to enter in the list: ")
maximum = int(input())
print("Enter a list of numbers: ")
for i in range(0,maximum):
 n = int(input())
 list1.append(n) #append numbers to the list
num = int(input("Enter the number to be searched: "))
result = linearSearch(num,list1)
if result is None:
 print("Number",num,"is not present in the list")
else:
 print("Number",num,"is present at",result + 1, "position")