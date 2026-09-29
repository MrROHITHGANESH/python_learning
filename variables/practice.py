#    variable assignmemnt= Giving a value to a variable for the first time.
#    variable Reassignment=changing the value of an existing variable.


# 1. variable assignmemnt,Reassignment  

x=10
y=x        #   y=10
x=20
print(x)      
print(y)    # output: x=20 ,y=10



#  2.variable assignmemnt,Reassignment  

a=5          #assignment
b=2
a=b          #reassignment a=2
b=10
print(a)
print(b)    # output: a=2, b=10


#  3.  Assiging a different datatype to a variable + type()

name="ganesh"
age=20
name = age      #name =20
print(name)
print(type(name))     # output: 20, <class 'int'>


#  4.  Dynamic typing + variable reassignment + type()

x=10                 
x="python"              
x=25.5 
print(x)
print(type(x))        # output: 25.5, <class 'float'>    


#

my_name="ganesh"
print(my_name)