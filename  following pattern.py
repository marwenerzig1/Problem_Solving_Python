#Write a Python program to print the reverse number pattern using a for loop.
#5 4 3 2 1 
#4 3 2 1 
#3 2 1 
#2 1 
#1

n = int(input("Donne N : "))
print('\n')


for i in range(n,-1,-1):
    for j in range(i,0,-1):
         print(j, end=' ')
    print('\n')