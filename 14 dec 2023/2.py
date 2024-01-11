#largest among three
'''def sparshva(num1, num2, num3):
    return max(num1, num2, num3)
num1=int(input("Enter number 1:-"))
num2=int(input("Enter number 2:-"))
num3=int(input("Enter number 3:-"))
result = sparshva(num1, num2,num3)
print(f"{result} is the largest number among three")'''

  
#function for sum of a list
'''def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
sparshva = [1, 2, 3, 4, 5]
result = sum(sparshva)
print(result) '''


#functiom for multiples in a list
'''def multiple(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
sparshva = [59, 12, 13, 54, 75]
result = multiple(sparshva)
print(result)  '''


# ⁠Write a python function to reverse a string
'''def reverse(input_string):
    return input_string[::-1]
sparshva =input("Enter a string:-")
result = reverse(sparshva)
print(result)'''

# wap to calculate the factorial of a number
'''def fact(x):
    factorial=1
    if x>=0:
        if x==0:
            return 1
        else:
            return x * fact(x-1)
    else:
        print("invalid!")
n=int(input("enter num"))
print(fact(n*1))'''

# wap sq and cube of a number 
'''def sq(x):
    print(x**2)
def cube(x):
    print(x**3)
n=int(input("enter number "))
choos=int(input("sq or cube(1,2)"))
if choos==1:
    sq(n)
else:
    cube(n)'''

# wap list input and output distinct elements
'''def list1(x):
    b=[]
    for i in range(len(x)):
        if a[i] not in b:
            b.append(i)
    print(b)

a=[1, 2, 3, 4, 5, 3, 3,5,8,9,2,2 ]
list1(a)'''

# wap count num of upper and lower case 
'''def count(str):
    countl=0
    countc=0
    for i in range(len(str)):
        if str[i] >="a" and str[i]<="z":
            countl+=1
        elif str[i]>="A" and str[i]<="Z":
            countc+=1
        else:
            None
    print("Block=",countc)
    print("lower=",countl)
string=(input("enter string"))
count(string)'''

# WAP perfect or not
'''def perf(x):
    factors=[]
    sumf=0
    for i in range(1,x):
        if x%i==0:
            factors.append(i)
    for i in range(len(factors)):
        sumf+=factors[i]
    if sumf==x:
        print(x,"perfect number")
    else:
        print(x,"not a perfect number")
x=int(input("enter a number"))
perf(x)'''

#wapn function that checks palindrome or notdef 
    # Remove spaces and convert to lowercase for case-insensitive comparison
def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())

    # Compare the original string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage:
string_to_check = "A man, a plan, a canal, Panama"
result = is_palindrome(string_to_check)

if result:
    print(f"'{string_to_check}' is a palindrome.")
else:
    print(f"'{string_to_check}' is not a palindrome.")