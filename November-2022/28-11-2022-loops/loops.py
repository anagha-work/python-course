'''for a in  range(10,0,-1):
    print(a)'''

#list
'''print(list(range(5,10,1)))
print(list(range(5,-5,-1)))'''

#tuple

'''x= ("Python","Java","Angular","React")
for i in x:
    print(i)
print("-"*50)

# string

x= "Python"
for i in x:
    print(i)
print("-"*50)'''



'''x = ["Python","Java","Angular","React"]
for  index in range(len(x)):
    value = x[index]
    print(index,value)
print("-"*50)'''


'''print("Hello world 3 times")
a = 0
while(a<3):
    a = a+1
    print("Hello world")'''

'''print("Use of break statement inside the loop")
count = 5
while(count>0):
    count = count -1
    if count == 2:
        break
    print(count)
print("loop ended")'''


'''print("Use of break statement inside the loop")
count = 5
while(count>0):
    count = count -1
    if count == 2:
        continue
    print(count)
print("loop ended")'''

'''print("Enter the from 20 to 1 :")
a = 20
while(a>=1):
    print(a,end= " ")
    a-= 1'''

#for loop using break and continue
x= "Python is high-level programming language"
for letter in x :
    if(letter == "e" or letter == "i"):
        break
    print(letter, end = "")

'''x = "Python is high-level programming language"
for letter in x :
    if(letter == "e" or letter == "i"):
        continue
    print(letter, end ="")'''