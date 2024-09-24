

n = int(input("give n : "))

for i in range(1,n+1):
    for i in range(1,i+1):
        print("* ", end=' ')
    print("\n")

for i in range(n-1,0,-1):
    for i in range(1,i+1):
        print("* ", end=' ')
    print("\n")
