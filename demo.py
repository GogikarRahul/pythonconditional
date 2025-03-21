num=int(input("enter the number:"))
if(num>0):
    print("number is positive")
elif(num==0):
    print("number is zero")
else:
    print("number is negative")


num=int(input("enter the number:"))
if(num%2==0):
    print(num,"is even number")
else:
    print(num,"is odd number")

age=int(input("enter the number:"))
if(age>=18):
    print("hey you can vote")
else:
    print("you cannot vote")


num1=int(input("enter the first number:"))
num2=int (input("enter the second number:"))
if(num1>num2):
    print( num1,"number is greatest ")
else:
    print(num2,"is greater")

marks=int(input("enter the marks:"))
if(marks>=40):
    print("pass")
else:
    print("fail")

day=int(input("enter the day:"))
if(day==1):
    print("monday")
elif(day==2):
    print("tuesady")
elif(day==3):
    print("wednesday")
elif(day==4):
    print("thursday")
elif(day==5):
    print("friday")
elif(day==6):
    print("saturday")
elif(day==7):
    print("sunday")
elif(day>7):
    print("enter the correct number which is less than 7")
else:
    print("nothing")


# calculator
num1=int(input("enter the number:"))
operator=input("enter the operator:")
num2=int(input("enter the second number:"))

if(operator== '+'):
    print(num1+num2)
elif(operator== '-'):
    print(num1-num2)
elif(operator== '/'):
    print(num1/num2)
elif(operator=='*'):
    print(num1*num2)
elif(operator=='//'):
    print(num1//num2)
elif(operator=='%'):
    print(num1%num2)
elif(operator != '+','-','/','*' ,'//','%' ):
    print("enter the valid operator!!")
else:
    print(" enter valid operator")


#printing the month

month=int(input("enter the month number:"))
if(month==1):
    print("january")
elif(month==2):
    print("Febraury")
elif(month==3):
    print("March")
elif(month==4):
    print("April")
elif(month==5):
    print("May")
elif(month==6):
    print("june")
elif(month==7):
    print("july")
elif(month==8):
    print("August")
elif(month==9):
    print("September")
elif(month==10):
    print("October")
elif(month==11):
    print("november")
elif(month==12):
    print("December")
elif(month>12):
    print("enter the valid month number!!")
else:
    print("hey there you go")


num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the number three:"))
if(num1>num2>num3):
    print(num1," first is greatest")
elif(num2>num1>num3):
    print(num2," second is greatest")
elif(num3>num1>num2):
    print( num3,"third is greatest")
else:
    print("enter the valid number")

year=int(input("enter the year:"))
if(year%400==0):
    print(year,"it is a leap year")
elif(year%4 ==0 and year% 100 !=0):
    print(year,"it is  a leap year")
else:
    print("It is not a leap year")

char=input("Enter the character:")
if(char=='a'):
    print(char,"it is a vowel")
elif(char=='A'):
    print(char,"it is a vowel")
elif(char=='e'):
    print(char,"it is a vowel")
elif(char=='E'):
    print(char,"it is a vowel")
elif(char=='i'):
    print(char,"it is a vowel")
elif(char=='I'):
    print(char,"it is a vowel")
   
elif(char=='o'):
    print(char,"it is a vowel")
   
elif(char=='O'):
   print(char,"it is a vowel")
   
elif(char != 'a','A','e','E','i','I','o','O','e','E'):
    print(char,"it is  a consonent")
else:
    print("enter the correct character")
   
grade=int(input("Enter the number:"))
if(grade>=90 and grade<=100):
    print("Grade A")
elif(grade>=80 and grade<90):
    print("Grade B")
elif(grade>=70 and grade<80):
    print("Grade C")
else:
    print("Fail")

   