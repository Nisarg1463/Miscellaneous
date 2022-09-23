from fractions import Fraction
from os import system
from time import sleep
def differ(a,b):
    if a>=0:
        a=int(a)
        i=b*(a-1)
    else:
        a=int(a)
        i=b*(-a+1)
    i=i.count("x")
    j=len(b)
    num=""
    if j>1:
        for k in range(j-1):
            num=num+b[k]
        num=int(num)
        if i!=0:
            return str(num*a)+"x"+"^"+str(i)            
    if i==0:
        return str(a)
    return str(a)+b+"^"+str(i)    
def integrat(a,b):
    if "x" not in b:
        if a != 0:
            return str(pow(int(b),a))+"x"
        return b+"x"
    if a>=0:
        a=int(a)
        i="x"*(a+1)
        i=i.count("x")
    else:
        a=int(a)
        i="x"*(-a-1)
        i=i.count("x")
        i=-i
    j=len(b)
    num=""
    if j>1:
        for k in range(j-1):
            num=num+b[k]
        if num != "":
            num=int(num)
        if i==0:
            return str(num)+"ln(x)"
        else:
            if num != "":
                num=num/i
                return "("+str(Fraction(num).limit_denominator())+')'+"x"+"^"+str(i)
    if i==0:
        return "ln(x)"
    if a<0:
        return b+"^"+str(-i)+"/"+str(i)    
    return b+"^"+str(i)+"/"+str(i)
print("1.differention")
print("2.integration")
choice=int(input("Enter your choice : "))
total=""
no_input=int(input("Enter the number of inputs of your equation : "))
for a in range(no_input):
    x,n=input(f"Enter element {a+1} of your formula : ").split("^")
    n=int(n)
    sign=""    
    if a!=no_input-1:
        sign=input("Enter sign between elements:")
    if choice==1:
        take=differ(n,x)
        if a==0:
            total=total+take
        elif sign=="+":
            if take[0]=="-":
                total=total+"-"+take[1:]
            else:
                total=total+"+"+take
        else:
            if take[0]=="-":
                total=total+"+"+take[1:]
            else:
                total=total+"-"+take
    else:
        take=integrat(n,x)
        if a==0:
            total=total+take
        elif sign=="+":
            if take[0]=="-":
                total=total+"-"+take[1:]
            else:
                total=total+"+"+take
        else:
            if take[0]=="-":
                total=total+"+"+take[1:]
            else:
                total=total+"-"+take
print(total)
# sleep(5)
# system('cls')