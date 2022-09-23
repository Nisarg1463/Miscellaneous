def matrix(m):
    matrices=[]
    mat=[]
    for i in range(m):
        b=""
        for j in range(m):
            a=input(f"Enter element A{i+1}{j+1} of your matrix : ")
            b=b+" "+a
        mat.append(b.split())
    for i in range(m):
        for j in range(m):
            mat[i][j]=int(mat[i][j])
    return mat
def determinant_3d(mat)       
    total=0
    for i in range(3):
        if i==0:
            add=mat[0][i]*(mat[1][1]*mat[2][2]-mat[1][2]*mat[2][1])
        elif i==1:
            add=-mat[0][i]*(mat[1][0]*mat[2][2]-mat[1][2]*mat[2][0])
        else:
            add=mat[0][i]*(mat[1][0]*mat[2][1]-mat[1][1]*mat[2][0])
        total=total+add
    print(f"Your answer is {total}")
def determinant_2d(mat):
    total=mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1]
    print(f"Your answer is {total}")
while True:
    print("1.2D determinant")
    print("2.3D determinant")
    print("3.Exit")
    choise=int(input("Enter your choice : "))
    if choise==1:
        matr=matrix(2)
        determinant_2d(matr)
    elif choise==2:
        matr=matr(3)
        determinant_3d(matr)
    elif choise==3:
        break
    else:
        print("Enter a valid choise")