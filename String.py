# string is collection of characters. It is a sequence of characters.
str1='Hello Python'
print(str1)

str2="Helloo World!!"
print(str2)

str3=''' Hii this is a mutli line string
this is second line 
this is third line '''
print(str3)

str="Hello World"
print(str)
#Positive Indexing
print(str[1])
print(str[4])
print(str[7])
print(str[10])

#Negative Indexing
print(str[-3])
print(str[-4])
print(str[-10])
print(str[-5])
print(str[-11])

#Slicing
print(str[:])
print(str[1:4])
print(str[4:8])
print(str[7:11])
print(str[3:7])

print(str[0:7:3]) 
print(str[6:11:4])
print(str[6:10:3])
print(str[7:10:2])

string="WELCOME"
string1=string.capitalize()
print(string1)
print(id(string))
print(id(string1))

string2=string.isupper() #Return Value true or false
print(string2)

string4="wel"
string5=string4.islower()
print(string5)

string3=string.lower() #Convert String
print(string3)