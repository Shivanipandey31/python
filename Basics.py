# # x=10100
# # y=100
# # z=215
# # u=0x12d
# # float_1=100.5
# # float_2=1.5e2
# # a=5+3.14j
# # print(x,y,z,u)
# # print (float_1,float_2)
# # print(a,a.imag,a.real)

# # x=(1==True)
# # y=(2==False)
# # z=(3==True)
# # a=True+10
# # b= False+10
# # print("x is",x)
# # print("y is",y)
# # print("z is",z)
# # print("a:",a)
# # print("b:",b)

# # a=32
# # b=6
# # print('Addition',a+b)
# # print('Subtraction',a-b)
# # print('Multiplication',a*b)
# # print('Division',a/b)
# # print('Reminder',a%b)
# # print('exponent of',a**b)
# # print('Floor division of',a//b)

# #Simple Interest

# # 
# # a,b=32,6
# # print(a==b)
# # print(a!=b)
# # print(a<=b)
# # print(a>=b)
# # print(a>b)
# # print(a<b)

# # a,b=5,1
# # print("And:"a&b)
# # print("OR",a|b)
# # print('XOR:',a^b)
# # print('NOT:'~a)
# # print('Left Shift',a<<b)
# # print('Right',a<<b)

# # a=5
# # print(a>3 and a<5)
# # print(a>3 or a)
# # a=["Rose","Lotus"]
# # b=["Rose","Lotus"]
# # c=a
# # print(a is c)
# # print(a is not c)
# # print(a is b)
# # print(a is not b)
# # print(a==b)
# # print(a!=c)

# # a=int(input("Enter a Value"))
# # b=int(input("enter value"))
# # print(a+b)
# # print(a-b)


# # age=32
# # while age>18:
# #     print('You can vote')

# # counter=0
# # while(counter<3):
# #     print('inside loop')
# #     counter=counter+1
# # else:
# #     print('inside else')

# # my_str="python"
# # for char in my_str:
# #     if char=='o':
# #         break
# #     print (char)


# num=0
# while (num<10):
#     num+=1
#     if(num%3)==0: 
#         continue
#     print (num )


# sequence=["Python","Ram","statement"]
# for value in sequence:
#     if value=="Ram":
#         pass
#     else:
#         print("not reached pass keyword:",value)

# armstrong
# num=int(input("enter a no."))
# sum=0
# temp=num
# while temp>0:
#      digit =temp%10
#      sum=sum+digit**3
#      temp=temp//10
# if sum==num:
#      print("armstrong")
# else :
#      print("not armstrong")


# #palindrome using while loop
# num=int(input("enter no."))
# sum=0
# temp=num
# while(temp>0):
#     r=temp%10
#     sum=(sum*10)+r
#     temp=temp//10
# if(sum==num):
#     print("palindrome")
# else:
#     print("not palindrome")


# mystr='Hello123'
# print(mystr.isalnum())

# mystr='12345'
# print(mystr.isalnum())

# str1='abcd'
# str2='xyz'
# #print str 3=azbycxd
# for i in range (len(str1)):  
#  str3=str1[i]+str2[len(str2)-1]
# print(str3)


#reverse the tuple
# tup=(1,2)
# for i in range(len(tup),0,-1):
#     print(i,end=" ")


#access value 20 from the tuple
# tuple1=("orange",[10,20,30],(5,15,25))
# print(tuple1[1][1])



# dict={"one":"1","two":2,"three":"3"}
# for key,value in dict.items():
#     print(key,":",value)
# dict.pop("two")
# print(dict)


#pretty printing in a dictionary

#convert two lists into dictionary
# list1=[1,2,3]
# list2=["one","two","three"]
# dict={}
# for i in range(len(list1)):
#     dict[list2[i]]=list1[i]
# print(dict)


#merge two python dictionaries into
# dict={"one":"1","two":2,"three":"3"}
# dict1={"four":"4","five":5,"six":"6"}
# for key,value in dict1.items():
#     if key not in dict:
#         dict[key]=value
# print(dict)        


# dict={}
# dict1={}
# k=int(input("enter no. of key,value pairs"))
# for i in range(k):
#     key=str(input("Enter key"))
#     value=int(input("Enter value"))
#     dict[key]=value
# print(dict)




#write a program that generate a set of prime numbers and a set of odd number perform union and intersection


# s1={1,2,3,4,5}
# s2={9,8,7,6,5}
# s1.union(s2)
# print(s1)
# s1.intersection(s2)
# print(s1)

#A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is input through the keyboard in hundreds, find the total number of currency notes of each denomination the cashier will have to give to the withdrawer.
# def isprime(n):
#     if n<=1:
#         return False

# for i in range(1,51):
# 	if(i%5==0 and i%3==0):
# 		print("FizzBuzz")
# 	if(i%3==0 and i%5!=0):
# 		print ("Fizz")
# 	elif(i%5==0 and i%3!=0):
# 		print("Buzz")
#     else:
#         print(i)

# amount=int(input("Enter amount="))
# ten=0
# fifty=0
# hundred=0
# while(amount>=10):
# 	hundred=amount//100
# 	amount=amount%100
# 	fifty=amount//50
# 	amount=amount%50
# 	ten=amount//10
# 	amount=amount%10
# print("Ten= ",ten)
# print("Fifty= ",fifty)
# print("Hundred= ",hundred)




# l=[1,2,3,4,5,6,7,8,9]
 #return a list that reverse all the element starting from index 0 to middle index only

# s='simran'
# print(s[0:len(s):-1])

s="this is python that is training"
s.startswith("t")
s.startswith("th")
s.startswith("py",8)
s="python302"

s.isalnum