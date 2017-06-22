a=str(input("enter a character"))
if(a.isupper()):
    a1=a.lower()
    if(a1=="a" or a1=="e" or a1=="i" or a1=="o" or a1=="u"):
        print("vowel")
    else:
        print("consonant")
else:
    if(a=="a" or a=="e" or a=="i" or a=="o" or a=="u"):
        print("vowel")
    else:
        print("consonant")
