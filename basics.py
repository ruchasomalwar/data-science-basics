a=10  #assigning the value of 'a' as 10
b=20  #assigning the value of 'b' as 20
a=5;b=10   #again assigning the values of 'a'&'b'
b,c=3.2,"Hello" #value of 'c' is assiginined as 3.2
x=y=z="WOrld"
print(c)
print()
print("Value of a=\n",a)  #\n is used for next line
print("Value of b=\n",b)
print(b,c)
print(b,c,sep=",")
c
print(a)
#%%

##division operartion in python 
print(1/3)

print(1//3)  ##floored division (gives the quotient)
print(7%3)   # % is used for modulus
print(round(1/3,2))  # here '2' indicates the how may places after the decimal point
#%%
a=5
b=3.2
print(type(b))  #is used to see the type of the variable
print(a+b)
a="5"
b="3.2"
print(type(b))
#%%

##user input
name=input("enter your name")
print("hello",name)
#%%
#if-elif-else statment
x=10
y=5
if x<y:
    print("this is firest block")
    print('x is less than y')
elif x>y:
    print('x is greater than y')
else:
    print('x & y are equal')
print("done")
#%%
##nasted if else 
if x==y:
    print('x and y are equal')
else:
    if x<y:
        print('x is less than y')
    else:
        print('x is greater than y')
print("done")

#%%
x=5;y=8
if( x>7 and y>7):
    print('x is single digit positive number.')

#%%
x=5;y=8
if( x>7 and y>7) or x!=y:   # != indicates not equal to
    print('x is single digit positive number.')
 #%%
##user defiened function 
def cube(a):
    print("value is =",a)
    return a*a*a

##square 10
value=float(input("enter a number:"))
cube(value)
#%%
def hi():
    print("hello user!")
hi()
#%%
##conditional loop (while)
##a) initiaalizing of itr variable b) condiation evaluation c)increamemtation\decreatation 
count=100
while(count>=70):
    print(count)
    #count +1
    count=count-1
else:
    print("count value reached", count)
#%%
##iterative loop(for loop)
friends=['a','b','c',3.6]
for i in friends:
    print('happy diwali,',i)
#%%%
friends=['a','b','c',3.6]
for i in friends:
    print('happy diwali,',i)

#%%
##python numbers
a=5
print(type(a))

b=30.6
print(type(b))

c=3+2j  #real number
print(type(c))
#%%
##change of data type
print(int(-2.8))
print(float(5))
#%% library
import math
print(math.sqrt(4))
print(math.floor(10.7))
print(math.pow(2,3))    
print(round(math.pi,2))  
print(math.pi)
print(math.factorial(4))    
#%% library randonm number genration 
import random as rn
#rn.seed(10)
print(rn.random())
print(rn.randrange(50,100))
print(rn.uniform(50.5,100))
x=[1,2,3,4,5]
print(rn.choice(x))    
#%% string
my_string='hello'
print(my_string)
print()
my_string="""hi.hello."""
print(my_string)

my_string="""hello.\n hii."""
print(my_string)
#%% accesing data structure
#slicing
my_string=('pyhton is a programming language. python is intresting.')
print(my_string[0])
print(my_string[-3])
#[inclusive:exclusive]
print(my_string[3:10])
print(my_string[:10])  
print(my_string[3:])  
print(my_string[:]) 
##print(my_string[100]) 
print(len(my_string))
del my_string
print(my_string)
#%% list [data structures]
##del- deleting
##list are mutable or can be modified, tuples are not mutable or cannot be modified
##python list
mylist1=[1,3,5,4,2]

mylist2=[1,4.2,'python',4.2]
print(mylist1)
print(mylist2)
print(type(mylist2))
#%% use of sliccing operator
a=[10,20,30,40,50,60,70,80]
print(a[2])
print(a[0:3])
print(a[5:])
##mutable example [modification in the given list]
a[3]=55.0
print(a)
#%%creating range
x=list(range(0,15))
print(x)
## numpy library have function of listing numbers in ascending or descending order
#%%nasted list
b=['spam',2.0,5,[10,"raj"]] ##nasted list
print(b[3][1])
#%%appending multiple elements
my_list=[1,3,6,9]
my_new_list=[4,5,6,7,8]
my_list.extend(my_new_list)
my_list.append("shreyas")
print(my_list)
#%% tuples immutable{cannot be modified} 
##tuples have () bracket list have [] bracket
a=(5,'python',10+2j,6)
print(a)
print(type(a))
print(a[0])
#%% nasted tuples
n_tuples=('mouse',[8,4,6],(1,2,3),8)
print(n_tuples)
##n_tuples[2][3]=0 immutable
del n_tuples
#%%sets {}
my_set={1,2,3,4,5,6,1,5,3,5,4,8}
print(my_set)
my_set=(1,1.0,"hello","shreyas",(1,2,4))
print(my_set)
#%%##union and intersection 
A=[1,5,4,17,9,4,4,6,2]
B=[15,22,56,2,4,7,88,9,5]
setA=set(A)
setB=set(B)

print(setA | setB) # setA or setB
print(setA.union(setB))
print(setA & setB)
print(setA.intersection(setB))
print(setA-setB)
print(setB.difference(setA))

#%% Dictionaries ##dicttionarie objects are mutable
##creating  dictionary
my_d1={1:'a',2:'b'}
print(my_d1)

my_d2={'name':['shreays','nikita','alex'],"ID":[2,4,3]}
print(my_d2)
print(my_d2['name'])
#%%
##modification of values
my_d={"name":"shereyas","age":27}
print(my_d)

my_d['address']='mumbai'
print(my_d)
my_d.values()
#%% 'zip' allows you to merge data
##data merging 
a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=dict(zip(a,b))
print(c)
#%%
##numpy library{arrays}
import numpy as np
np.__version__


a=np.array([1,2,3])
print(a)
print(type(a))
#%%2d array
a=np.array([(1,2,3),(5,5,6)])
print(a)
print(a.ndim)  #ndim tells if the data is 1d or 2d
print(a.shape)
#%%accessing the array
##indexing and slicing
a=np.array([(1,2,3,4),(3,4,5,6),(1,2,3,4)])
print(a)
print(a[0,2])
print(a[:,2])
print()
print(a[0:2,])
#%%
#aggreagate functions
a=np.array([(8,9),(10,11),(12,13)])
print(np.min(a))
print(np.max(a))
print(np.sum(a))
print(np.mean(a))
print(np.sqrt(a))
print(np.std(a))
print(np.log(a))
b=np.sqrt(a)
print(np.round(2))
#%%
import numpy as np
x=np.array([(1,2),(3,4)])
y=np.array([(5,6),(3,4)])
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x@y)
#print(np.dot(x,y))
#print(np.add(x,y))
#np.add(),np.subtract(),np.multiply,np.divide(),np.remainder()







