import copy


def matrix_maker():
    m, n = input('Enter number of rows and columns respectively: ').split('x')
    # taking matrix input

    m, n = int(m), int(n)

    matrix = []

    for i in range(m):
        matrix.append(input().split())
        
    #To remove human error while entering values
        
    for i in range(m):
        while(len(matrix[i]) > n):
            matrix[i].pop()
        while(len(matrix[i]) < n):
            matrix[i].append(int(input(f'Enter value for position {i+1} {len(matrix[i])+1} : ')))

        #converting them into integers

    for i in range(m):
        for j in range(n):
            matrix[i][j] = int(matrix[i][j]) 

    return matrices(matrix, m, n)

class matrices:

    def show(self):
        for i in range(self.m):
            print(self.matrix[i])

    def __init__(self, lst, m, n):
        self.matrix = lst
        self.m = m
        self.n = n
    
    def __add__(self, other):
        if self.m == other.m and self.n == other.n:
            answer = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.n)] for i in range(self.m)]
            return matrices(answer, self.m, self.n) 
        print('not possible')
    
    def __sub__(self, other):
        if self.m == other.m and self.n == other.n:
            answer = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.n)] for i in range(self.m)]
            return matrices(answer, self.m, self.n) 
        print('not possible')
    
    def __mul__(self, other):
        if self.n == other.m:
            answer = []
            for i in range(self.m):
                row = []
                for j in range(other.n):
                    sum = 0
                    for k in range(self.m):
                        sum += self.matrix[i][k] * other.matrix[k][j]
                    row.append(sum)
                answer.append(row)
            return matrices(answer, self.m, other.n)
        print('not possible')

    def __pow__(self, power):
        answer = copy.deepcopy(self)
        if self.n == self.m:
            for _ in range(power-1):
                answer = answer * self
            return answer
        print('not possible')
    
    def __imul__(self, other):
        return self * other

    def __iadd__(self, other):
        return self + other

    def __ipow__(self, power):
        return self ** power

    def __isub__(self, other):
        return self - other    

    def transpose(self):
        answer = []
        for i in range(self.m):
            intermediate = []
            for j in range(self.n):
                intermediate.append(self.matrix[j][i])
            answer.append(intermediate)
        return matrices(answer, self.n ,self.m)
    
    def scalar_multiply(self, number):
        return matrices([[number * self.matrix[i][j] for j in range(self.n)] for i in range(self.m)], self.m, self.n)
    
    def inverse(self):
        det = determinant(self.matrix, self.n)
        if det.determinant() == 0:
            print('not possible')
        else:
            value = 1/det.determinant()
            adjoin_matrix = det.adjoin()
            return adjoin_matrix.scalar_multiply(value)


class determinant:

    def __init__(self, matrix, size):
        self.matrix = matrix
        self.size = size

    def determinant(self):
        order = self.size
        lst = self.matrix
        if self.size == 1:
            return self.matrix[0][0]
        if order == 2:
            return lst[0][0]*lst[1][1] - lst[0][1]*lst[1][0]
        else:
            answer = 0
            for i in range(self.size):
                minor_det = determinant(self.minor((0, i)), self.size - 1)
                if i % 2 == 0:
                    answer += lst[0][i]*minor_det.determinant()
                else:
                    answer -= lst[0][i]*minor_det.determinant()
            return answer

    def minor(self, position):
        answer = []
        for i in range(self.size):
            intermediate = []
            for j in range(self.size):
                if position[0] != i and position[1] != j:
                    intermediate.append(self.matrix[i][j])
            answer.append(intermediate)
        answer.remove([])
        return answer
    
    def cofactor(self, position):
        minor_mat = determinant(self.minor(position), self.size - 1)
        if (position[0] + position[1]) % 2 == 0:
            return minor_mat.determinant()
        return -minor_mat.determinant()
    
    def adjoin(self):
        answer = []
        for i in range(self.size):
            intermediate = []
            for j in range(self.size):
                intermediate.append(self.cofactor((i, j)))
            answer.append(intermediate)
        return matrices(answer, self.size, self.size).transpose()

# m1 = matrix_maker()
# m2 = matrix_maker()
if __name__ == '__main__':
    m1 = matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3)
    m2 = matrices([[13, 5, 9], [9, 8, 15], [5, 11, 5]], 3, 3)
    m3 = matrices([[21, 22], [23, 24]], 2, 2)
    I = matrices([[1, 0, 0], [0, 1, 0], [0, 0, 1]],3, 3)

    # print(determinant([[1, 2, 3], [5, 4, 6], [8, 9, 7]], 3).determinant())

    # if m2.inverse() is not None:
    #     m2.inverse().show()
    matrices([[3 ,2 ,-2], [-1 ,-1 ,2], [0, -1, 2]], 3, 3).inverse().show()