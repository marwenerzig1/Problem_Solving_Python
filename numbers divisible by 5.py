#Write a Python code to display numbers from a list divisible by 5

def div_5(list):
    print("The numbers divisible by 5 are : ")
    for i in list:
        if (i % 5 == 0):
            print(i)


list = [10, 15, 14, 12]
div_5(list)