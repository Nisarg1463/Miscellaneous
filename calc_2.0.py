from os import system, name 
from time import sleep
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
while True:
    intake_raw=input("Enter an equation : ")
    intake=intake_raw.replace(" ","")
    try:
        if "+" in intake:
            counter=intake.count('+')
            if counter==1:
                a=int(intake[:intake.index('+')])
                b=int(intake[intake.index('+')+1:])
                summation=a+b
            else:
                for i in range(counter):
                    if i == 0:
                        plus_count=intake.find("+")
                        plus_count_raw=intake.find("+",plus_count+1)
                        a=int(intake[:plus_count])
                        b=int(intake[plus_count+1:plus_count_raw])
                        summation=a+b
                    else:
                        plus_count=intake.find("+",plus_count+1)
                        plus_count_raw=intake.find("+",plus_count+1)
                        if plus_count_raw>0:
                            a=int(intake[plus_count+1:plus_count_raw])
                        else:
                            a=int(intake[plus_count+1:])
                        summation += a
            print(summation)
        elif "-" in intake:
            counter=intake.count('-')
            if counter==1:
                a=int(intake[:intake.index('-')])
                b=int(intake[intake.index('-')+1:])
                summation=a-b
            else:
                for i in range(counter):
                    if i == 0:
                        plus_count=intake.find("-")
                        plus_count_raw=intake.find("-",plus_count+1)
                        a=int(intake[:plus_count])
                        b=int(intake[plus_count+1:plus_count_raw])
                        summation=a-b
                    else:
                        plus_count=intake.find("-",plus_count+1)
                        plus_count_raw=intake.find("-",plus_count+1)
                        if plus_count_raw>0:
                            a=int(intake[plus_count+1:plus_count_raw])
                        else:
                            a=int(intake[plus_count+1:])
                        summation -= a
            print(summation)
        elif "*" in intake:
            counter=intake.count('*')
            if counter==1:
                a=int(intake[:intake.index('*')])
                b=int(intake[intake.index('*')+1:])
                summation=a*b
            else:
                for i in range(counter):
                    if i == 0:
                        plus_count=intake.find("*")
                        plus_count_raw=intake.find("*",plus_count+1)
                        a=int(intake[:plus_count])
                        b=int(intake[plus_count+1:plus_count_raw])
                        summation=a*b
                    else:
                        plus_count=intake.find("*",plus_count+1)
                        plus_count_raw=intake.find("*",plus_count+1)
                        if plus_count_raw>0:
                            a=int(intake[plus_count+1:plus_count_raw])
                        else:
                            a=int(intake[plus_count+1:])
                        summation *= a
            print(summation)
        elif "/" in intake:
            counter=intake.count('/')
            if counter==1:
                a=int(intake[:intake.index('/')])
                b=int(intake[intake.index('/')+1:])
                summation=a/b
            else:
                for i in range(counter):
                    if i == 0:
                        plus_count=intake.find("/")
                        plus_count_raw=intake.find("/",plus_count+1)
                        a=int(intake[:plus_count])
                        b=int(intake[plus_count+1:plus_count_raw])
                        summation=a/b
                    else:
                        plus_count=intake.find("/",plus_count+1)
                        plus_count_raw=intake.find("/",plus_count+1)
                        if plus_count_raw>0:
                            a=int(intake[plus_count+1:plus_count_raw])
                        else:
                            a=int(intake[plus_count+1:])
                        summation /= a
            print(summation)
        elif "exit" in intake:
            break
    except Exception as e:
        print(e)
    finally:
        p=input("Press enter to continue")
        clear()