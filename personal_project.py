from os import system
from fractions import Fraction
import datetime
def scalar_multiply(mat,scalar):
    return [[ j*scalar for j in i]for i in mat]
def adjoint(mat):
    return [[ cofactor(mat,j,i) if (i+j)%2==0 else -int(cofactor(mat,j,i)) for j in range(len(mat))]for i in range(len(mat))]
def add(mat1,mat2):
    return [[mat1[i][j]+mat2[i][j] for j in range(len(mat1))]for i in range(len(mat1[0]))]
def sub(mat1,mat2):
    return [[mat1[i][j]-mat2[i][j] for j in range(len(mat1))]for i in range(len(mat1[0]))]
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
    equation=input()
    if 'exit' in equation.lower():
        system('cls')
        break
    if 'clear' in equation.lower():
        system('cls')
        continue
    if 'new' in equation:
        ls.append(input('Enter order of your matrix : ').split('x'))
        ls[-1][0],ls[-1][1]=int(ls[-1][0]),int(ls[-1][1])
        mat=[ [ int(input(f"Enter the element {i+1}{j+1} : ")) for j in range(ls[-1][1])] for i in range(ls[-1][0])]
        mat_ls.append(mat)
        continue
    if 'mat clean' in equation:
        mat_ls=[]
        continue
    symbol=['adj','^-1','^','*','+','-']
    symbols=[]
    for i in symbol:
        if i in equation:
            symbols.append(i)
    if '^-1' in equation:
        counter=sum([ equation.count(i) for i in symbol])-2*equation.count('^-1')
    else:    
        counter=sum([ equation.count(i) for i in symbol])
    k=''
    for i in range(counter):
        ls=[]
        for i in symbol:
            ls.append(i)
            while True:   
                if type(ls[-1])!= int:
                    if i in equation:
                        ls.append(equation.index(i))
                    else: 
                        break
                else:
                    if i in equation[ls[-1]+1:]:
                        ls.append(equation.index(i,ls[-1]+1))
                    else: 
                        break
            ls.remove(i)
            ls.sort()
        ls=list(set(ls))
        ls.sort()
        for j in ls:
            if ls.index(j)!=len(ls)-1:    
                if j+1==ls[ls.index(j)+1]:
                    ls.remove(j+1) 
        if k=='':
            k=symbols[0]
        if k not in equation:
            k=symbols[symbols.index(k)+1]
        if k=='adj':
            if len(ls)==1:
                num=equation[4:-1]
            else:
                num=equation[equation.index('adj(')+4:equation.index(')')]
            mat_ls.append(adjoint(mat_ls[int(num)-1]))
            equation=equation.replace(f'adj({num})',str(len(mat_ls)))
        elif k=='^-1':
            if len(ls)==1:
                num=equation[:equation.index('^')]
            else:
                num=equation[ls[ls.index(equation.index(k))-1]+1:equation.index(k)]
            mat_ls.append(inverse(mat_ls[int(num)-1]))
            equation=equation.replace(f'{num}^-1',str(len(mat_ls)))
        else:
            if len(ls)==1:
                num1=equation[:equation.index(k)]
                num2=equation[equation.index(k)+1:]
            elif ls.index(equation.index(k))==0:
                num1=equation[:equation.index(k)]
                num2=equation[equation.index(k)+1:ls[ls.index(equation.index(k))+1]]
            elif ls.index(equation.index(k))==len(ls)-1:
                num2=equation[equation.index(k)+1:]
                num1=equation[ls[ls.index(equation.index(k))-1]+1:equation.index(k)]
            else:
                num1=equation[ls[ls.index(equation.index(k))-1]+1:equation.index(k)]
                num2=equation[equation.index(k)+1:ls[ls.index(equation.index(k))+1]]
            if k=='^':
                ans=mat_power(mat_ls[int(num1)-1],int(num2))
            elif k=='+':
                ans=add(mat_ls[int(num1)-1],mat_ls[int(num2)-1])
            elif k=='-':
                ans=sub(mat_ls[int(num1)-1],mat_ls[int(num2)-1])
            elif k=='*':
                ans=multiply(mat_ls[int(num1)-1],mat_ls[int(num2)-1])
            mat_ls.append(ans)
            equation=equation.replace(f'{num1}{k}{num2}',str(len(mat_ls)),1)
    for i in mat_ls[int(equation)-1]:
        print(i)