#Check if the first and last numbers of a list are the same

def check(list):
    a = len(list) 

    if a == 0 :
        return "this list is empty"
    elif a == 1 : 
        return "the first and last numbers of a list are the same because the list is 1 item "
    else :
        if list[0] == list[a-1]:
            return "yes ! it's True the same"
        else :
            return "sory ! it's false not the same"



list = [24, 25, 245, 23, 24]
print(check(list))


