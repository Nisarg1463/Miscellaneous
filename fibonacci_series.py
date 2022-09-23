def fibonacci_series(n):
    a,b=0,1
    print("Your series is :",end=" ")
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b,end=(" "))
        for i in range (n-2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")    
intake=input("Enter the length of your fibonacci series : ")
intake=int(intake)
fibonacci_series(intake)