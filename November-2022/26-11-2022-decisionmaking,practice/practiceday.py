# data types & variable
'''print("Integer")
ab = 20+4
print("Addition is :",ab)
print("dataye of ab",type(ab))'''

#boolean
'''compare = 46>5
print("value of compare is",compare)
print("datatype is :",type(compare))'''

#print

'''print("hello python")
print("Addition is :",10+20)
print(45 + 6 * 8)'''

# user define input 
'''person =input("Enter Your Name :")
print("Welcome"+ " "+ person)
print("Welcome " + person)'''



'''print("Sequence Type : LIST , STRING , TUPLE")
it_course = ["python", "Java ", "24" ,"java", "oracle"]# syntax x=[]
print("Given statement is :",it_course)
print("Data type  is:" ,type(it_course))
graduation=("BE", "BSC","BCA","BDS")
print("Given statement is :",graduation)
print("Data type  is:" ,type(graduation))

_valUe03 ="Python is simple and powerful programming language"
print("statement is :",_valUe03)
print("Data type of _valUe03:",type(_valUe03))
print("-"*50)'''

'''l1=[]#empty list
print(type(l1))
l2=[1,2,3,4,5,6,7]
print(type(l1))'''

#type casting :
#string to integer

'''print("Enter Number :")
value = int(input())
print("Given number:", value)
print("data type in value:",type(value))

print("Enter Number :")
value_ = float(input())
print("Given number:", value_)
print("data type in value:",type(value_))'''

#creating dictionary
'''items = {1:'one','course':'python',3:'three'}
print(items)
print(type(items))
print(len(items))
print(items[1])# to access itme refer to its key name
print(items['course'])'''


'''a = {1:'Hi',3:'Anagha',2:"Babar"}
print(a)
print(type(a))
print(a[2])'''

'''a = {1:'Hi',3:'Anagha',2:"Babar",2:"Babar"}#duplicates are not allow in set
print(a)
print(type(a))
print(a[2])'''

#set

'''s1 = {1,2,3.3,"python",4,"python"}#duplicates are not allow in set
print(s1)
print(type(s1))
print(len(s1))'''


'''s1 = {"Anagha","babar", "Python" }
print(s1[2])#In set Index is not allow'''

#string

'''line1 = 'python is a programming language.'
line2 = "Python is designed by Guido Van Rossum and released in 1991."
line_3 = python syntax is easy as compared to other languages.
Python supports OOPS concept
print("About Python :", line1,line2,line_3)
print("Data type :", type(line1))'''

'''l1 = "Anagha"
l2 ="Be"
l3 =Positive
print("Anagha :",l2,l3)
print("data type :",type(l2))'''

#index & slicing

'''line = "it's 7.30pm"
print(len(line))
print(line[0])
print(line[2])
print(line[3])
print(line[4])
print(line[-3])
print(line[5:])'''

'''_s1 = 'Today is funday'
print(len(_s1))
print(_s1[9:])
print(_s1[0:])
print(_s1[-1:-4])'''


#same quote in same statement
#backslash \ is used as an escape character
'''print("print(\"hello world\")")
line = 'it\'s 7.30pm'
print(line)
print("length of line:",len(line))'''

'''a1 ='Anagha\'s \t Shrawasti'
print(a1)'''

#string concatenation
'''Name = "Mona"
Surname = "Ganvir"
Full_Name = Name +" " +Surname
print(Full_Name)'''

'''ab = "Anagha"
cd ="Babar"
Full_name = ab +" " +cd
print(Full_name)'''

# creating tuple -----> using parentheses()

'''t1 = (1,"hello",True,"hello")  #heterogenous/allow duplicate
print("Given tuple :",t1)
print(type(t1))'''

'''a1 = ("Anagha",)#tuple
print(type(a1))'''

'''t2 = (1,"hello",3.45,False)
print(len(t2))
print(t2[0])#positive index
print(t2[1])
print(t2[2])
print(t2[3])'''

'''t1 = (1,"Anagha" ,24,False,24)
t2 = (1,"hello",3.45,False)
t2 = (1,"hello",3.45,False)
print(t1)

#t1[0]= "python"
#print(t1)
print(t1[-1])
print(t1[-3])
print(t1[1:])'''

#packing and unpacking in tuple
'''a =('kasturi','26','10000','trainer')#packing 
#to extract the values back into variables "unpacking"
(name,age,salary,job)=a
print(name)
print(age)
print(salary)
print(job)'''

a1 = ("Anagha",24,"Python")
(Name,age,course)=a1
print(Name)




















