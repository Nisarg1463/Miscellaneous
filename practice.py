class Matrix:
    def __init__(self,m,n,mat):
        self.m=m
        self.n=n
        self.matrix=mat

    def show(self):
        print(self.matrix)

    def __add__(self,other):
        if self.m==other.m and self.n==other.n:
            return [[self.matrix[i][j]+other.matrix[i][j] for j in range(self.n)] for i in range(self.m)]

    def __sub__(self,other):
        if self.m==other.m and self.n==other.n:
            return [[self.matrix[i][j]-other.matrix[i][j] for j in range(self.n)] for i in range(self.m)]

    def __mul__(self,other):
        if self.n==other.m:
            return [[sum([self.matrix[i][k]*other.matrix[k][j] for k in range(self.n)]) for j in range(other.n)] for i in range(self.m)]

    def scalar_multiply(self,num):
        return [[self.matrix[i][j]*num for j in range(self.n)] for i in range(self.m)]

    def __pow__(self,num):
        a=Matrix(self.m,self.n,self.matrix)
        for i in range(num-1):
            a.matrix = a*self
        return a.matrix

    def adjoint(self):
        if self.m==2 and self.n==2:
            pass

num=int(input('Enter number of matrices :'))
mat_list=[]
for i in range(num):
    m,n=input(f'Enter order of {i+1} matrix : ').split('x')
    m,n=int(m),int(n)
    matrix=[]
    for i in range(m):
        a=input().split(' ')
        for j in range(len(a)):
            a[j]=int(a[j])
        matrix.append(a)
    mat_list.append(Matrix(m,n,matrix))
# print(mat_list[0]+mat_list[1])
# print(mat_list[0]-mat_list[1])
# print(mat_list[0]*mat_list[1])
# print(mat_list[0]**3)
# print(mat_list[0].scalar_multiply(3))