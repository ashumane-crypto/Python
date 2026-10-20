 #Task on string
# 1) To check the given string is anagram or not 


# # 2) To reverse a given string
# string=input("Enter a string:")
# rev_text=""
# for ch in string:
#     rev_text=ch+rev_text
# print(rev_text)

# # method-2
# # str1=string[::-1]
# # print(str1)


# # 3) (How are you) reverse string

# str2="How are you"
# str3=str2[::3]
# print(str3)

name = input("Enter a string: ")

word = ""
result = ""

for ch in name:
    if ch != " ":
        word=word+ch
    else:
        result=word+" "+result
        word=""
result=word+" "+result
print(result)


# # 4) krishna o/p--k|r|i|s|h|n|a
# name=input("Enter a name:")
# for i in range(len(name)):
#     if i<(len(name))-1:
#         print(name[i],end="|")
#     else:
#         print(name[i])


# # 5) count a frequency of given string p=1,r-2,g-1
# name1=input("Enter a string:")
# frequency={}
# for ch in name1:
#     if ch in frequency:
#         frequency[ch]=frequency[ch]+1
#     else:
#         frequency[ch]=1
# print(frequency)

# 6) take input from user (input=python) and  o/p should be print its positive and neagative  use loop

# name3=input("Enter a string:")
# print("Character","Positive index","Negative index")
# for i in range(len(name3)):
#     positive_index=i
#     negative_index=i-len(name3)
#     print(name3[i],positive_index,negative_index)

# 7) Check the given string is pallindrome or not 
# string=input("Enter a string:")
# string1=string
# rev_text=""
# for ch in string:
#     rev_text=ch+rev_text
# print(rev_text)
# if string1==rev_text:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# 8) input-> Hello output->HELLO without using upper method
# string=input("enter a string:")
# result=""
# for ch in string:
#     if 'a'<=ch<='z':
#         result=result+chr(ord(ch)-32)
#     else:
#         result=result+ch
# print(result)


# 9) input->HELLO output->hello without using inbuilt method
# string=input("Enter a string:")
# result=""
# for ch in string:
#     if 'A'<=ch<="Z":
#         result=result+chr(ord(ch)+32)
#     else:
#         result=result+ch
# print(result)



# s4="MOM"
# s5=s4[::-1]
# if s5==s4:
#     print("is palindrome")
# else:
#     print("not palindrome")