# this exercice make you know this string is missing letter or not 
# for example : xyz : No Missing Letter In Sequence !
# or cdeg : Missing Letter In Sequence is f ! 


# abcdefghijklmnopqrstuvwxyz
# xyz  


alphabet = "abcdefghijklmnopqrstuvwxyz"
n = len(alphabet)

ch = input("taper une suite d'alphabet : ")
n_ch = len(ch)

for i in range(n):
    if ch[0] == alphabet[i]:
        if ch == alphabet[i:(i+n_ch)] : 
            print("No Missing Letter In Sequence !")
            break;
        else:
            ch2 = alphabet[i:(i+n_ch)]
            for j in range(n_ch):
                if (ch[j] != ch2[j]):
                    print("Missing Letter In Sequence is " , ch2[j])
                    break;

