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

print(len(string))

string5="Java is Programming Language"
string6=string5.replace("Java","Python")
print(string6)

str5=""
list=["H","E","L","L","O"]

string7=str5.join(list)
print(string7)

string8="communication"
string9=string8.index("c")  #Starts from forward to backward indexing if there is no chanaracter found then return error message
print(string9)

string8="communication"
string10=string8.rfind("c") #Start from backward to forward indexing
print(string10)

str14=string8.find("z")   #If we use a find method it reurns the index but iftheir is no found then returns -1
print(str14)

string11="Welcome to the python"
string12=string11.index("p",6,18)
print(string12)

string13="Python is a programming language"
string14=string13.partition("is")  #Partition returns a tuple
print(string14)

string15=string13.split()  #split returns a list
print(string15)

string16=string13.count("a")
print("Occurence",string16)

string17="This are my favourite fruits and they are tasty" 
string18=string17.count("are",3,41)
print(string18)


#More string functions
string19=string17.endswith("ty")
print(string19)

string20=string17.startswith("")
print(string20)

string22="123num"
string23=string22.isalnum()  #letter+digit then return true
print(string23)

string24=string22.isdigit() #only digit then return true
print(string24)

string25=string22.isalpha()  #only alphabets then return true
print(string25)



s="Programming"
count=0
for ch in s:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        count=count+1
print("Count of vowels is:-",count)


#Find seprate Letter,number and symbol from mixed string
mixed_string="User_12345!"
letter=""
number=""
symbol=""
for char in mixed_string:
    if char.isalpha():
        letter=letter+char
    elif char.isdigit():
        number=number+char
    else:
        symbol=symbol+char
print(f"Letters:{letter}")
print(f"Number:{number}")
print(f"Symbol:{symbol}")





