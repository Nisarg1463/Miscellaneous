from fractions import Fraction

def inverse(mat):
    if len(mat)!=len(mat[0]):
        return 'not possible'
    try:
        if len(mat)==2:
            return [[ cofactor(mat,j,i)/determinant_2d(mat) if (i+j)%2==0 else -cofactor(mat,j,i)/determinant_2d(mat) for j in range(2)]for i in range(2)]
        return [[cofactor(mat,j,i)/determinant_3d(mat) if (i+j)%2==0 else -cofactor(mat,j,i)/determinant_3d(mat) for j in range(3)]for i in range(3)]
    except:
        pass
def determinant_3d(mat):       
    return sum([cofactor(mat,0,i) if i!=1 else cofactor(mat,0,i) for i in range(3)])

def cofactor(mat,m,n):
    if len(mat)!=len(mat[0]):
        return 'not possible'
    matr=[[ mat[i][j] for j in range(len(mat)) if i!=m and j!=n]for i in range(len(mat))]
    matr.remove([])
    if len(matr)==1:
        return matr[0][0]
    return determinant_2d(matr)

def multiply(l1,l2):
    mat=[]
    for i in range(len(l1)):
        sm=''
        total=0
        for k in range(len(l2)):
            total += l1[i][k]*l2[0][k]
        mat.append(total)
    return mat    

def determinant_2d(mat):
    return mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1]

# MAIN CODE
number = int(input("Enter number of equations : "))
mat_ls,char=[],[]
for i in range(number):    
    equation = input()
    a=''
    ls=[]
    for i in equation:
        try:
            a+=str(int(i))
        except:
            ls.append(a)
            if i not in ['+','-','=']:
                char.append(i)
            a=''
            if i in ['+','-']:
                a+=i
    ls.append(a)
    while True:
        try:
            ls.remove('')
        except:
            break
    mat_ls.append(ls)
mat_ls=[[int(mat_ls[i][j]) for j in range(len(mat_ls[0]))] for i in range(len(mat_ls))]
ls=[[mat_ls[i][j] for j in range(len(mat_ls[0])-1)]for i in range(len(mat_ls))]
b=[ mat_ls[i][len(mat_ls[0])-1] for i in range(len(mat_ls))]
b=[b]
if type(inverse(ls))!=str:
    answer=multiply(inverse(ls),b)
else:
    checker=[ int(b[i])/int(b[i+1])==int(ls[i][0])/int(ls[i+1][0]) for i in range(len(b)-1)]
    if all(checker):
        answer='infinite solutions'
    else:
        answer='no solution at all'
print(answer)