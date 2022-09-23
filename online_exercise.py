import numpy as np
intake=int(input('Enter number of list you want to add : '))
mat_ls=[]
for i in range(intake):
    order=input(f'Enter order of your {i+1} matrix : ').split('x')
    order[0],order[1]=int(order[0]),int(order[1])
    mat=[[int(input(f"Enter the element {i+1}{j+1} of your matrix: ")) for j in range(order[0])]for i in range(order[1])]
    mat_ls.append(np.array([mat]))
# intake=input()
print()  