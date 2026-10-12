#Unordered collection of unique elements
#it is mutable
# there is no indexing and slicing beacuse set deos not retirn as it is index present in input
#i,e indexing is not fix in set
#it created by built in function set
#We did not maintain order

s1={1,2,2,4,7,9,4,3,1}
print(s1)

#empty set
s=set()
print(type(s))

# Methods of set
s2={"apple",1,2,4,2,"Banana","Hello",9,8}
print(s2)
s2.add(99) #1)Add-to at one element in set
print(s2)
s2.update([55,47]) #update-to add multiple element in set
print(s2)
s2.remove(2) #remove-to remove the particular element from list
print(s2)
s2.pop() #pop-REmoves the random lement from set
print(s2)
s2.clear() #clear-Removes all elemnt from set
print(s2)


set1={1,3,9,8,5,3,2,2,5,6}
set2={9,3,1,1,5,6}
print(set1.union (set2)) #Union(|)-Returns uniques lement from both set
print(set1.intersection (set2)) #Intersection(&)-retirns the commmon Elemnts from both set
print(set1.difference (set2))  #Difference(-)-Elements in set1 that are not in set2
print(set1.symmetric_difference (set2)) 


set_X={1,2,3,4,5}
set_Y={1,8,2,3}
set_Z={1,3}
print(set_Y.issubset(set_X))
print(set_X.issuperset(set_Z))
# set_X.insertion_update(set_Y,set_Z)
# print(set_X)
