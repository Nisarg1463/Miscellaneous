from time import sleep
from os import system
from fractions import Fraction
import datetime
def start():
    project="Matrix_and_determinant_calc.py"
    current_time=datetime.datetime.now()
    f = open('user_data.txt','a')
    f1= open('user_data.txt','r')
    name=input("Enter your name : ")
    count=0
    for i in f1:
        count += 1
    f.write(f"{count+1}. {name} {current_time} {project} \n")
def mat_power(mat,power):
    if power==2:
        return mat_square(mat,mat)
    else:
        return mat_square(mat_power(mat,power-1),mat)
def mat_square(mat1,mat2):
    m1=len(mat1)
    n1=len(mat1[0])
    s=[]
    for i in range(m1):
        sm=''
        for j in range(n1):    
            total=0
            for k in range(m1):
                total=total+(mat1[i][k]*mat2[k][j])
            if j==0:
                sm=sm+str(total)
                continue
            sm=sm+','+str(total)
        s.append(sm.split(','))   
    for i in range(m1):
        for j in range(n1):
            s[i][j]=int(s[i][j])
    return s
def co_factor_3d(matrix,n):
    cofactor=0
    for i in matrix:
        if n in i:
            j=i.index(n)
            i=matrix.index(i)
            if i==0 and j==0:
                cofactor=matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1]
            if i==0 and j==1:
                cofactor=matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0]
            if i==0 and j==2:
                cofactor=matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0]
            if i==1 and j==0:
                cofactor=matrix[0][1]*matrix[2][2]-matrix[0][2]*matrix[2][1]
            if i==1 and j==1:
                cofactor=matrix[0][0]*matrix[2][2]-matrix[0][2]*matrix[2][0]
            if i==1 and j==2:
                cofactor=matrix[0][0]*matrix[2][1]-matrix[0][1]*matrix[2][0]
            if i==2 and j==0:
                cofactor=matrix[0][1]*matrix[1][2]-matrix[0][2]*matrix[1][1]
            if i==2 and j==1:
                cofactor=matrix[0][0]*matrix[1][2]-matrix[0][2]*matrix[1][0]
            if i==2 and j==2:
                cofactor=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    return cofactor
def determinant_3d(mat):       
    total=0
    for i in range(3):
        if i==0:
            add=mat[0][i]*(mat[1][1]*mat[2][2]-mat[1][2]*mat[2][1])
        elif i==1:
            add=-mat[0][i]*(mat[1][0]*mat[2][2]-mat[1][2]*mat[2][0])
        else:
            add=mat[0][i]*(mat[1][0]*mat[2][1]-mat[1][1]*mat[2][0])
        total=total+add
    return total
def determinant_2d(mat):
    total=mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1]
    return total
def inverse_matrix_3d():
    global matr,m,n
    if len(matr)==1:
        choice=1
    else:
        choice=int(input("Enter number of matrix of which you want to find inverse : "))
    mat=matr[choice-1]
    if m[choice-1]==3 and n[choice-1]==3:
        final_matrix=[]
        range_matrix=""
        trial1_matrix=[]
        l=determinant_3d(mat)
        if l!=0:
            for i in range(3):
                for j in range(3):
                    if j==0:
                        range_matrix=range_matrix+str(co_factor_3d(mat,mat[i][j]))
                    else:
                        range_matrix=range_matrix+","+str(co_factor_3d(mat,mat[i][j]))
                range_matrix=range_matrix+" "
            trial1_matrix=range_matrix.split()
            for i in range(3):
                final_matrix.append(trial1_matrix[i].split(","))
            for i in range(3):
                for j in range(3):
                    final_matrix[i][j]=int(final_matrix[i][j])
                    x=final_matrix[i][j]/l
                    final_matrix[i][j]=str(Fraction(x).limit_denominator)
            return final_matrix
        else:
            print("Determinant is 0 . Therefor inverse is not possible")
            sleep(5)
    else:
        print("It is not a 3x3 matrix")
        sleep(5)
def inverse_matrix_2d():
    global matr,m,n
    if len(matr)==1:
        choice=1
    else:    
        choice=int(input("Enter the number of matrix of which you want to find inverse : "))
    matrix=matr[choice-1]
    final_matrix=[]
    trial_matrix=[]
    range_matrix=""
    det=determinant_2d(matrix)
    if m[choice-1]==2 and n[choice-1]==2:
        if det!=0:
            for i in range(2):
                for j in range(2):
                    if i==0 and j==0:
                        range_matrix=str(matrix[1][1])
                    if i==0 and j==1:
                        range_matrix=range_matrix+","+str(-matrix[0][1])
                    if i==1 and j==0:
                        range_matrix=range_matrix+str(-matrix[1][0])
                    if i==1 and j==1:
                        range_matrix=range_matrix+","+str(matrix[0][0])
                range_matrix=range_matrix+" "
            trial_matrix=range_matrix.split()
            for i in range(2):
                final_matrix.append(trial_matrix[i].split(","))
            for i in range(2):
                for j in range(2):
                    x=int(final_matrix[i][j])/det
                    final_matrix[i][j]=str(Fraction(x).limit_denominator())
            return final_matrix
        else:
            print("Determinant is 0.So inverse not possible")
            sleep(5)
    else:
        print("It is not 2x2 matrix")   
        sleep(5)     
def add():
    global matr,m,n
    if len(matr)==2:
        choice1=1
        choice2=2
    else:
        choice1,choice2=input("Enter the number of matrices you want to add : ").split(",")
        choice1,choice2=int(choice1),int(choice2)
    order1,order2=[],[]
    order1.append(m[choice1-1])
    order1.append(n[choice1-1])
    order2.append(m[choice2-1])
    order2.append(n[choice2-1])
    mat1=matr[choice1-1]
    mat2=matr[choice2-1]
    mat3=[]
    mat5=''
    if order1==order2:
        for i in range(order1[0]):
            mat5=''
            for j in range (order1[1]):
                mat4=mat1[i][j]+mat2[i][j]
                mat5=mat5+' '+str(mat4)
            mat3.append(mat5.split())
        for i in range(order2[0]):
            for j in range(order2[1]):
                mat3[i][j]=int(mat3[i][j])
        system('cls')
        return mat3
    else:
        print("Sum not possible")
    sleep(3)
def sub():
    global matr,m,n
    if len(matr)==2:
        choice1=1
        choice2=2
    else:
        choice1,choice2=input("Enter the number of matrices you want to subtract : ").split(",")
        choice1,choice2=int(choice1),int(choice2)
    order1,order2=[],[]
    order1.append(m[choice1-1])
    order1.append(n[choice1-1])
    order2.append(m[choice2-1])
    order2.append(n[choice2-1])
    mat1=matr[choice1-1]
    mat2=matr[choice2-1]
    mat3=[]
    mat5=''
    if order1==order2:
        for i in range(order1[0]):
            mat5=''
            for j in range (order1[1]):
                mat4=mat1[i][j]-mat2[i][j]
                mat5=mat5+' '+str(mat4)
            mat3.append(mat5.split())
        for i in range(order2[0]):
            for j in range(order2[1]):
                mat3[i][j]=int(mat3[i][j])
        return mat3
    else:
        print("Subtraction not possible")
        sleep(3)
def multi():
    global matr,m,n,result
    if len(matr)==2:
        choice1=1
        choice2=2
    else:
        choice1,choice2=input("Enter the number of matrices you want to multiply : ").split(",")
        choice1,choice2=int(choice1),int(choice2)
    order1,order2=[],[]
    order1.append(m[choice1-1])
    order1.append(n[choice1-1])
    order2.append(m[choice2-1])
    order2.append(n[choice2-1])
    mat1=matr[choice1-1]
    mat2=matr[choice2-1]
    s=[]
    if order1[1]==order2[0]:
        m1=order1[0]
        n1=order2[1]
        for i in range(m1):
            sm=''
            for j in range(n1):    
                total=0
                for k in range(order1[1]):
                    total=total+(mat1[i][k]*mat2[k][j])
                if j==0:
                    sm=sm+str(total)
                    continue
                sm=sm+','+str(total)
            s.append(sm.split(',')) 
        for i in range(m1):
            for j in range(n1):
                s[i][j]=int(s[i][j])  
        return s
    else:
        print("Multiplication not possible")
        sleep(3)
def matrix(m,n):
    mat=[]
    for i in range(m):
        b=""
        for j in range(n):
            a=input(f"Enter element A{i+1}{j+1} of your matrix : ")
            b=b+" "+a
        mat.append(b.split())
    for i in range(m):
        for j in range(n):
            mat[i][j]=int(mat[i][j])
    return mat
start()
number=int(input("Enter the number of matrices : "))
matr=[]
m=[]
n=[]
result=[]
for i in range(number):
    c,d=input(f"Enter the order of your {i+1} matrix : ").split("x")
    c,d=int(c),int(d)
    m.append(c)
    n.append(d)
    matr.append(matrix(m[i],n[i]))
system('cls')
while True:
    print("Note : Temperarily fractions are not available")
    print("Options are as follow : ")
    print("0.Add a matrix in list of matrix")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Inverse of 2x2 matrix")
    print("5.Inverse of 3x3 matrix")
    print("6.2D determinant")
    print("7.3D determinant")
    print("8.matrix power")
    print("9.Exit")
    choice=int(input("Enter your choice : "))
    if choice==0:
        c,d=input("Enter the order of your matrix : ").split("x")
        c,d=int(c),int(d)
        m.append(c)
        n.append(d)
        matr.append(matrix(m[-1],n[-1]))
        system('cls')
    elif choice==1:
        ans=add()
        print(f"Answer is {ans}")
        null=input("Press enter to continue")
    elif choice==2:
        ans=sub()
        print(f"Answer is {ans}")
        null=input("Press enter to continue")
    elif choice==3:
        ans=multi()
        print(f"Answer is {ans}")
        null=input("Press enter to continue")
    elif choice==4:
        ans=inverse_matrix_2d()
        print(f"Answer is {ans}")
        null=input("Press enter to continue")
    elif choice==5:
        ans=inverse_matrix_3d()
        print(f"Answer is {ans}")
        null=input("Press enter to continue")
    elif choice==6:
        if len(matr)==1:
            intake=1
        else:    
            intake=int(input("Enter number of matrix which you want to find determinant"))
        ans=determinant_2d(matr[intake-1])
        print(f"Answer is {ans}")
        null=input("Press enter to continue")
    elif choice==7:
        if len(matr)==1:
            intake=1
        else:
            intake=int(input("Enter number of matrix which you want to find determinant"))
        ans=determinant_3d(matr[intake-1])
        print(f"Answer is {ans}")
        null=input("Press enter to continue")
    elif choice==8:
        if len(matr)==1:
            mat=matr[0]
        else:
            take=int(input("Enter position of matrix : "))
            mat=matr[take-1]
        power=int(input("Enter the power : "))
        print(f"Answer is {mat_power(mat,power)}")
        null=input("Press enter to continue")
    elif choice==9:
        break
    else:    
        print("Enter valid option.")
        sleep(2)
    system('cls')
system('cls')