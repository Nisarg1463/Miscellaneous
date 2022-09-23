from os import system, name 
from time import sleep
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')
i=1
while i!=0:
    print("Select process which you want to do from below options :")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Remainder")
    print("0.Exit")
    i=int(input("Enter your option : "))
    if i==0:
        clear()
        continue
    a=int(input("Enter first number :"))
    b=int(input("Enter second number :"))
    if i==1:
        t=a+b
    elif i==2:
        t=a-b
    elif i==3:
        t=a*b
    elif i==4:
        t=a/b
    elif i==5:
        t=a%b
    else:
        print("Invalid option")
        continue
    print(f"Your answer is {t}")
    sleep(5)
    clear()