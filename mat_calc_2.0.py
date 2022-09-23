from os import system
from fractions import Fraction
import datetime
def scalar_multiply(mat,scalar):
    return [[ j*scalar for j in i]for i in mat]
def adjoint(mat):
    return [[ cofactor(mat,j,i) if (i+j)%2==0 else -int(cofactor(mat,j,i)) for j in range(len(mat))]for i in range(len(mat))]
def add(mat1,mat2):
    global ls,mat_ls
    if (ls[mat_ls.index(mat1)]==ls[mat_ls.index(mat2)]):
        return [[mat1[i][j]+mat2[i][j] for j in range(ls[mat_ls.index(mat1)][0])]for i in range(ls[mat_ls.index(mat1)][0])]
def sub(mat1,mat2):
    global ls,mat_ls
    if (ls[mat_ls.index(mat1)]==ls[mat_ls.index(mat2)]):
        return [[mat1[i][j]-mat2[i][j] for j in range(ls[mat_ls.index(mat1)][0])]for i in range(ls[mat_ls.index(mat1)][0])]
    return "Not possible"
def determinant_2d(mat):
    return mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1]
def mat_power(mat,power):
    if power==2:
        return multiply(mat,mat)
    return multiply(mat_power(mat,power-1),mat)
def multiply(l1,l2):
    if len(l1)==len(l2[0]):
        mat=[]
        for i in range(len(l1)):
            sm=''
            for j in range(len(l2[0])):
                total=0
                for k in range(len(l2)):
                    total += l1[i][k]*l2[k][j]
                sm+=str(total)
                if j!=len(l2[0])-1:
                    sm+=','
            mat.append(sm)
        mat1=[i.split(',') for i in mat]
        mat=[[int(j) for j in i]for i in mat1]
        return mat
    return 'not possible'
def cofactor(mat,m,n):
    if len(mat)!=len(mat[0]):
        return 'not possible'
    matr=[[ mat[i][j] for j in range(len(mat)) if i!=m and j!=n]for i in range(len(mat))]
    matr.remove([])
    if len(matr)==1:
        return matr[0][0]
    return determinant_2d(matr)
def determinant_3d(mat):       
    return sum([cofactor(mat,0,i) if i!=1 else cofactor(mat,0,i) for i in range(3)])
def inverse(mat):
    if len(mat)!=len(mat[0]):
        return 'not possible'
    try:
        if len(mat)==2:
            return [[ Fraction(cofactor(mat,j,i)/determinant_2d(mat)) if (i+j)%2==0 else -Fraction(cofactor(mat,j,i)/determinant_2d(mat)) for j in range(2)]for i in range(2)]
        return [[ Fraction(cofactor(mat,j,i)/determinant_3d(mat)) if (i+j)%2==0 else -Fraction(cofactor(mat,j,i)/determinant_3d(mat)) for j in range(3)]for i in range(3)]
    except Exception as e:
        print(e)
number=int(input("Enter number of matrices you want to add in list : "))
ls=[input(f"Enter order of your {i+1} matrix : ").split("x") for i in range(number)]
for i in range(len(ls)):
    for j in range(len(ls[i])):
        ls[i][j]=int(ls[i][j])
mat_ls=[[[int(input(f"Enter the element {i+1}{j+1} of your matrix: ")) for j in range(k[1])]for i in range(k[0])] for k in ls]
while True:
    operation=input("Write operation you want to perform : ")
    if "+" in operation:
        k=operation.index("+")
        num1=int(operation[:k])
        num2=int(operation[k+1:])
        print(add(mat_ls[num1-1],mat_ls[num2-1]))
    elif '^-1' in operation:
        num1=int(operation[:operation.index("^-1")])
        print(inverse(mat_ls[num1-1]))
    elif '-' in operation:
        k=operation.index("-")
        num1=int(operation[:k])
        num2=int(operation[k+1:])
        print(sub(mat_ls[num1-1],mat_ls[num2-1]))
    elif '*' in operation:
        k=operation.index("*")
        num1=int(operation[:k])
        num2=int(operation[k+1:])
        print(multiply(mat_ls[num1-1],mat_ls[num2-1]))
    elif operation.count('|')==2:
        k=operation.index('|')
        l=operation.find('|',k+1)
        num=int(operation[k+1:l])
        if len(mat_ls[num-1])==2:
            print(determinant_2d(mat_ls[num-1]))
        else :
            print(determinant_3d(mat_ls[num-1]))
    elif '^' in operation:
        k=operation.index('^')
        print(mat_power(mat_ls[int(operation[:k])-1],int(operation[k+1:])))
    elif '[' in operation and ']' in operation:
        number=int(operation[operation.index('[')+1:operation.index(']')])
        scalar=int(operation[:operation.index('[')])
        print(scalar_multiply(mat_ls[number-1],scalar))
    elif 'adj' in operation:
        k=operation.index('(')
        l=operation.index(')')
        print(adjoint(mat_ls[int(operation[k+1:l])-1]))
    elif 'new' in operation.lower():
        ls.append(input('Enter order of your matrix : ').split('x'))
        ls[-1][0],ls[-1][1]=int(ls[-1][0]),int(ls[-1][1])
        mat=[ [ int(input(f"Enter the element {i+1} {j+1} : ")) for j in range(ls[-1][1])] for i in range(ls[-1][0])]
        mat_ls.append(mat)
    elif 'exit' in operation.lower():
        system('cls')
        break
    elif 'clear' in operation.lower():
        system('cls')
    else:
        print("Enter valid operation")