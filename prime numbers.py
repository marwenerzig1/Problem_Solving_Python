# A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
# 6 is not a prime number because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply to make it.


start =  25
end = 50

print("Prime numbers between", start, "and", end, "are:")

for i in range(start,end+1):
    test=True
    for j in range(2,int((i/2))+1):
        if(i % j == 0) :
            test = False
            break
    if(test == True):  
        print(i)    



