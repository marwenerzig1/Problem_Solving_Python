#Write a Python program to use for loop to find the factorial of a given number.
#The factorial (symbol: !) means multiplying all numbers from the chosen number down to 1.
               
n = int(input("write number"))
res = 1

for i in range(n,1,-1):
    res = res * i 

print(n,"! = ",res)