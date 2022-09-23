from os import system, name 
from time import sleep
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
def factorial(a):
    total=1
    for i in range(1,a+1):
        total*=i
    return total
choice=1
while choice!=3:
    print("1.Combination")
    print("2.Permitution")
    print("3.Exit")
    choice=int(input("Enter your choice: "))
    if choice==3:
        clear()
        continue
    n,r=input("Enter n and r for your choice saperated by comma: ").split(",")
    n,r=int(n),int(r)
    if choice == 1:
        answer=factorial(n)/(factorial(n-r)*factorial(r))
    elif choice==2:
        answer=factorial(n)/factorial(r)
    else:
        print("Enter valid answer")
    print(f"your answer is {answer}")
    sleep(2)
    clear()