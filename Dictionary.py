#Hold key and value pair
#It used to store data in form of key and value pair
#it in mutable(Changable)
#to create dictionary we uses curley braces
# We can store hetrogenius type of data
d={
    'a':"Ashwini",
    1:'Ashu'
}
print(d)

#To create empty dictionary
D={}
D1=dict()
print(type(D))
print(type(D1))

user={"Name":'Ashwini',
      "Age":20
    
     }
print(user)

#Dictionary Methods

#Retriving the data
print(user.get("Name")) #1)Get-by key access the value
print(user.keys())  #2)keys-to get all keys from dict
print(user.values()) #3)Values-To get all values from dict
print(user.items())  #4)items-To get dynamic view in tuple of dict

#Adding and Modifying data
user.update({"Age":21})  #1)Update-to update key value pair
print(user)

user.setdefault("City","Satara")  #2)setDefault-TO set by defaut value
print(user)

# user.pop("Age") #pop-removes specifies elemnt by key
# print(user)

# user.popitem() #Removes last inserted key value pair
# print(user) 

# user.clear()  #REmoves all elements from dictionary
# print(user)

#Utility Methods

clone=user.copy() #creates the shallow copy
clone["a"]=100
print(clone)
print(user)




