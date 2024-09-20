#Write a Python code to accept a string from the user and display characters present at an even index number.
#For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.


str = input("write a chaine : ")


for i in range(0,len(str)):
    #print(i)
    if (i % 2 == 0):
        print("'",str[i],"'")



    



