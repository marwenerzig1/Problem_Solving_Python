# Display Fibonacci series up to 10 terms
# Have you ever wondered about the Fibonacci Sequence? It’s a series of numbers in which the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.


num1 , num2 = 0 , 1


print(num1)
print(num2)

for i in range(10):
    res = num1 + num2

    print(res)

    num1=num2
    num2=res 






