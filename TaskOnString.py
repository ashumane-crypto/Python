 #Task on string
# # 1) To check the given string is anagram or not 
str1=input("Enter a string1:")
str2=input("Enter a string2:")
if len(str1)!=len(str2):
    print("Not Anagram")
else:
    for ch in str1:
        found=0
    for i in range(len(str2)):
        if ch ==str2[i]:
            found=1
            str2=str2[:i]+str2[i+1:]
            break
    if found==0:
        print("Not Anagram")
    else:
        print("Anagram")


a="silent"
b="listen"
if(sorted(a)==sorted(b)):  #eilnst==eilnst
    print("Given string is Anagram")
else:
    print("Given string is not Anagram")





 # 2) To reverse a given string
# string=input("Enter a string:")
# rev_text=""
# for ch in string:
#     rev_text=ch+rev_text
# print(rev_text)




# # 3) (How are you) reverse string
# name="How are You"
# word=""
# result=""
# for ch in name:
#     if ch!=" ":
#         word=word+ch
#     else:
#         result=word+" "+result
#         word=""
# result=word+" "+result
# print(result)


# str2="How are you"
# str3=str2[::3]
# print(str3)




# # 4) krishna o/p--k|r|i|s|h|n|a
# name="Krishna"
# for i in range(len(name)):
#     if i<(len(name))-1:
#         print(name[i],end="|")
#     else:
#         print(name[i])



# # 5) count a frequency of given string p=1,r-2,g-1

# string=input("Enter a String:")
# frequency={}
# for ch in string:
#     if ch in frequency:
#         frequency[ch]+=1
#     else:
#         frequency[ch]=1
# print(frequency)



# # 6) take input from user (input=python) and  o/p should be print its positive and neagative  use loop
# string=input("Enter a string:")
# print("Character","positive_index","negative_index")
# for i in range(len(string)):
#     positive_index=i
#     negative_index=i-len(string)
#     print(string[i],positive_index,negative_index)




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

# s4="MOM"
# s5=s4[::-1]
# if s5==s4:
#     print("is palindrome")
# else:
#     print("not palindrome")


# # 8) input-> Hello output->HELLO without using upper method
# string=input("Enter a string:")
# result=""
# for ch in string:
#     if 'a'<ch<'z':
#         result=result+chr(ord(ch)-32)
#     else:
#         result=result+ch
# print(result)




# # 9) input->HELLO output->hello without using inbuilt method
# string=input("Enter a String:")
# result=""
# for ch in string:
#     if "A"<ch<"Z":
#         result=result+chr(ord(ch)+32)
#     else:
#         result=result+ch
# print(result)







