#Modes in file Handling
# 1)"r"=read-opens the file for reading,error if file does not exists
# 2)"a"=append-opens the file and write the new data,creates the file if not exixting
# 3)"w"=write-Opens the file for writing and previous data is deleted and new entered data is stored
# 4)"x"=creates-creates the specifies file and returns an error if it still exists

# f=open("demo.txt",'w')
# f.write("Hello My Name is Ashwini")
# f.close()

# #read mode operation
# file=open("demo.txt",'r')
# print("file_name",file.name)
# print("readable_mode: ",file.readable())  #to find data is readable or not
# print("writable_mode: ",file.writable())  #to find we can write the new data or not 
# print("file_close",file.closed)
# print(file.read())  #To see(read) the data in terminal
# print(file.readline())  #read only one line
# print(file.readlines())  #read multiple lines give o/p in list


# #to read data using for loop
# for x in file:
#     print(x)
# file.close()


# #write the data using file mode write 'w'
# #but previous data is gone we only here can add new data
# f=open("demo.txt",'w')
# f.write("Hey Guys How are you??\n")
# f.write("What you doing??\n")
# f.close()


# #write the data using file in append 'a' mode
# #but existing data is still their we can add new data
# f=open("demo.txt",'a')
# f.write("My name is Ashwini\n")
# f.write("I am from Satara")

# f=open("demo1.txt",'x')
# f=open("demo1.txt",'w')
# f.write("Good Morning!!!")

# f.close()

file=open("demo1.txt",'r')
print(file.read())
file.close()






