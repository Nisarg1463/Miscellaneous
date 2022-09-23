import datetime
def start():
    project="Error.py"
    current_time=datetime.datetime.now()
    f = open('user_data.txt','a')
    f1= open('user_data.txt','r')
    name=input("Enter your name : ")
    count=0
    for i in f1:
        count += 1
    f.write(f"{count+1}. {name} {current_time} {project} \n")
start()
