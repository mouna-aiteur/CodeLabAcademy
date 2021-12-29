#1- writting function that checks whether a passed string is palindrome or not
def checkingPolindrome(s):
    # reverse the string s gives us list , so we join it in a string
   reversedWord= "".join(list(reversed(s)))
   # get rid of all spaces , so we compare only the letters
   reversedWord= reversedWord.replace(" ","")
   s2 = s.replace(" ","")
   if reversedWord == s2:
       print(s, "is polindrome")
   else:
       print(s, "is not polindrome")

word= input("enter string :")
checkingPolindrome(word)

#2- writting function that checks if the number is prime or not
def primeNumberChecking(n):
    #initialize remainder
    remainder = n % 2
    i = 2
    while remainder != 0 :
        if  n ==2 or n== 1:
            break
        
        remainder = n%i
        if i == n-1 :
            break
        i=+1        
    if remainder != 0 or n ==2:
        print(n , " is prime number")
    else:
        print(n , " is not prime number")
#input a number and convert it to integer
number = int(input(" enter a number greater than 1 :"))  
primeNumberChecking(number)   

#3-checking if number is in a giving range
def checkingFunction(n,l):
    # initializing variable that is true if n exists in the range and false if it does not
    nExists = False
    for i in l:
        if i == n :
            nExixts = True
            break
    if nExists == True :
        print(n , " is in the range ")
    else:
        print(n , " is not in the range ")
# asking for the range lenght
rangeLen = int(input(" enter the lenght of the range : "))
myRange = []
for i in range(0 , rangeLen):
    number = float(input("enter number : "))
    myRange.append(number)
#asking for the number that the user want to check
checkedNumber = float(input(" enter the number that you want to check if it is in the range : "))
checkingFunction(checkedNumber, myRange)
        
            
    
    

#4-function that calculates the factorial of a number
def factorial(n):
    if n== 0 or n == 1:
        return 1
    return n* factorial(n-1)
#input a number and convert it to integer
number = int(input("enter positive integer : "))
print("the factorial : " ,factorial(number))

#5-Python program to reverse a string.
def reverse(s):
    lenght = len(s)
    Mylist=[]
    for i in range(lenght-1,-1,-1):
        Mylist.append(s[i])
    return "".join(Mylist)
    print(Mylist)
# input the string
word = input("enter string :")
#printing the reversed string wiyhout extra space
print(reverse(word).strip())

#6- writing fumction that sums all the numbers in a list.
def fuctionSum(l):
    sum = 0
    for i in l :
        sum = sum + i
    print("the sum is : ",sum)
# asking the user to input the lenght of the list
lenght = int(input("enter the lenght of the list : "))
list = []
#putting the numbers in list
for i in range(0,lenght):
    number = float(input("enter a number :"))
    list.append(number)
fuctionSum(list)

#7- writting function to find the Max of three numbers
def maxFunction(l):
    # initialazing a avriable called max
    max = 0.00
    for i in range(0,len(l)-1):
        if l[i]>l[i+1]:
            max = l[i]
            l[i+1] = l[i]
        else:
            max = l[i+1]
    print("the maximum number is : ", max)
# defining list of 3 numbers only
numberList = []
for i in range(0, 3):
    number = float(input(" enter number : "))
    numberList.append(number)
maxFunction(numberList)