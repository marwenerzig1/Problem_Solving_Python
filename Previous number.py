#Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

print("Printing current and previous number sum in a range(10)")


for i in range(1,11):
    print("Current Number", i ,"Previous Number",  i-1  ,"Sum:" , i + (i-1) )

