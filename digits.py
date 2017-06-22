n=int(input("enter a number"))
    c=0
    while(n!=0):
        q=int(n/10)
        r=int(n%10)
        c=c+1
        n=q
    print(c)
