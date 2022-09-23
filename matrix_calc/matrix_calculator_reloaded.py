import Matrix_and_Determinant as MD
import json

oldpermit = input('Do you want to continue with any old data? (y/n): ')
list_of_matrices = {}
if oldpermit == 'y':
    filename = input('Enter filename of previous data: ').strip()
    with open(f'{filename}.json', 'r') as f:
        old_data = json.loads(f.readline())
    
    for i in old_data.keys():
        list_of_matrices[i] = MD.matrices(old_data[i][0], old_data[i][1], old_data[i][2])

    print(list_of_matrices)

num = int(input('Enter number of starting matrices : '))

for _ in range(num):
    list_of_matrices[input('Enter name of Matrix : ')] = MD.matrix_maker()

print('Note:\n use + for addition \n use - for subtraction \n use * for multiplication \n use ^ for power')

while True:
    calculation = input('Enter calculation : ')
    calculation = calculation.replace(' ','')
    
    if calculation.lower() == 'exit':
        break

    if calculation.lower() == 'new':
        list_of_matrices[input('Enter name of Matrix : ')] = MD.matrix_maker()
        continue

    calculation = calculation.replace('+', ' + ')
    calculation = calculation.replace('-', ' - ')
    calculation = calculation.replace('^', ' ^ ')
    calculation = calculation.replace('*', ' * ')

    calculation = calculation.split()

    power = calculation.count('^')
    multiplication = calculation.count('*')
    addition = calculation.count('+')
    subtraction = calculation.count('-')

    try:
        count = 0

        for i in range(power):
            index = calculation.index('^')
            list_of_matrices[f'i{count}'] = list_of_matrices[calculation[index - 1]] ** int(calculation[index + 1])
            calculation.pop(index + 1)
            calculation.pop(index)
            calculation[index - 1] = f'i{count}'
            count += 1

        for i in range(multiplication):
            index = calculation.index('*')
            list_of_matrices[f'i{count}'] = list_of_matrices[calculation[index - 1]] * list_of_matrices[calculation[index + 1]]
            calculation.pop(index + 1)
            calculation.pop(index)
            calculation[index - 1] = f'i{count}'
            count += 1

        for i in range(addition):
            index = calculation.index('+')
            list_of_matrices[f'i{count}'] = list_of_matrices[calculation[index - 1]] + list_of_matrices[calculation[index + 1]]
            calculation.pop(index + 1)
            calculation.pop(index)
            calculation[index - 1] = f'i{count}'
            count += 1

        for i in range(subtraction):
            index = calculation.index('-')
            list_of_matrices[f'i{count}'] = list_of_matrices[calculation[index - 1]] - list_of_matrices[calculation[index + 1]]
            calculation.pop(index + 1)
            calculation.pop(index)
            calculation[index - 1] = f'i{count}'
            count += 1

    except Exception:
        pass

    finally:
        if list_of_matrices[f'i{count - 1}'] is not None:
            list_of_matrices[f'i{count - 1}'].show()
            save_info = input('Do you want to save result? (y/n): ')
            if save_info.lower() == 'y':
                name = input('Enter name for the result : ')
                list_of_matrices[name] = list_of_matrices[f'i{count - 1}']        
            for i in range(count):
                list_of_matrices.pop(f'i{i}')

boolean = input('Enter do you want to save this matrices? (y/n): ')

if boolean == 'y':
    filename = input('Enter filename to save data: ')
    dic = {}
    for i in list_of_matrices.keys():
        dic[i] = [list_of_matrices[i].matrix, list_of_matrices[i].m, list_of_matrices[i].n]
    with open(f'{filename}.json', 'w') as f:
        f.write(json.dumps(dic))