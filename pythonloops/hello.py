# for i in range(1,101):
#     print(i)

#******************************************************
# sum=0
# num=int(input("enter the number"))
# for i in range(1,num+1):
#      sum+=i
# print(sum)
#**********************************************************
# num=0
# while num<50:
#     num+=1
#     if(num%2==0):
#         print(num)

#********************************************

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(num*i)

#*******************************************************

# num=int(input("enter the number:"))
# sum=0
# while num+1>0:
#     sum+=num
#     print(num)
#     num-=1
# print(sum)

#***********************************************************
# num=(input("enter the number:"))
# while num>0:
#     print(str(len(num)))
#     break


# for i in range(1,11):
#     if(i%2==0):
#         continue
#     for j in range(1,31):
#          print(i,j)


# for i in range(1,11):
#       for j in range(1,31):
#           if(i%2!=0 and j<15):
#               continue
#           print(i,j)
          
# i=3
# print("the number is even")if(i%2==0)else print("the number is odd")


# char=input("enter the single character").lower()
# if len(char)==1:
#     if char.isalpha():
#         if char in ['a','e','i','o','u']:
#             print('is is a vowel')
#         else:
#             print('it is a consonant')
#     else:
#         print('it is a special character')
# else:
#     print('please Enter a valid character greater than 1')
        
#*************************************************************************************************

# num1=13691215222325
# temp=0
# sum=0
# count=0

# while num1>0:
#     rem=num1%10 
#     sum+=rem
#     if(rem%3==0):
#      print(rem)
#     temp=temp*10+rem
#     num1=num1//10
#     count+=1
   
      
# print(temp)
# print(sum)
# print("count=",count)

# num=0
# num1=1
# for i in range(1,20):
#     print(num)
#     num3=num+num1
#     num=num1
#     num1=num3



#user_input=input("enter the choice cube o square or exit:").lower()
# data=["square","cube","exit"]
# while True:
#     if(user_input==data[2]):
#         print("you have successfully exited")
#         break
#     elif(user_input==data[0]):
#         num=int(input("enter the number:"))
#         print(num**2)
#         user_input=input("enter the choice cube o square or exit:").lower()
#     elif(user_input==data[1]):
#         num=int(input("enter the number:"))
#         print(num**3)
#         user_input=input("enter the choice cube o square or exit:").lower()
#     else:
#         print("please enter a valid name")
#         user_input=input("enter the choice cube o square or exit:").lower()



