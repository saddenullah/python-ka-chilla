# # type of conversion
x=10          #integer
y=10.5         #float
z="saddin"      #String 

# IMPLICIT TYPE OF CONVERSION
x=x*y
# print(type(x))
print(x,type(x))

# EXPLICIT TYPE OF CONVERSION

age=input("how old is you? ")
print(type(age))  #herte type of age is string 
print(age)

# change above string into integer

age=input("how old is you? ")
age=int(age)    #here change to integer
# OR
print(type(int(age)))  #herte type of age change into  integer
print(age)
# OR 
print(age,type(int(age))) #here all in one , print of age and also cnvert the type of age 