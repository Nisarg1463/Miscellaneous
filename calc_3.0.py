from os import system

while True:
    intake = input()
    if 'exit' in intake.lower():
        system('cls')
        break
    if 'clear' in intake.lower():
        system('cls')
        continue
    symbols = ['/', '*', '+', '-']
    k = ''
    counter = sum([intake.count(i) for i in symbols])
    if '/' not in intake and counter != 1:
        counter += 1
    intake_raw = ''
    try:
        for j in range(counter):
            ls = []
            for i in symbols:
                ls.append(i)
                while True:
                    if type(ls[-1]) != int:
                        if i in intake:
                            ls.append(intake.index(i))
                        else:
                            break
                    else:
                        if i in intake[ls[-1]+1:]:
                            ls.append(intake.index(i, ls[-1]+1))
                        else:
                            break
                ls.remove(i)
                ls.sort()
            if len(ls) > 1:
                if k == '':
                    k = '/'
                else:
                    k = symbols[symbols.index(k)+1]
                if k in intake:
                    k_index = intake.index(k)
                    k_index_position = ls.index(k_index)
                    if k_index_position == len(ls)-1:
                        num1 = intake[ls[k_index_position-1]+1:k_index]
                        num2 = intake[k_index+1:]
                    elif k_index_position == 0:
                        num1 = intake[:k_index]
                        num2 = intake[k_index+1:ls[k_index_position+1]]
                    else:
                        num1 = intake[ls[k_index_position-1]+1:k_index]
                        num2 = intake[k_index+1:ls[k_index_position+1]]
                    if k == '/':
                        ans = float(num1)/float(num2)
                    elif k == '*':
                        ans = float(num1)*float(num2)
                    elif k == '+':
                        ans = float(num1)+float(num2)
                    else:
                        ans = float(num1)-float(num2)
                    intake = intake.replace(str(num1)+k+str(num2), str(ans))
            else:
                num1 = intake[:ls[0]]
                num2 = intake[ls[0]+1:]
                if '/' in intake:
                    ans = float(num1)/float(num2)
                    k = '/'
                elif '*' in intake:
                    ans = float(num1)*float(num2)
                    k = '*'
                elif '+' in intake:
                    ans = float(num1)+float(num2)
                    k = '+'
                else:
                    ans = float(num1)-float(num2)
                    k = '-'
                intake = intake.replace(str(num1)+k+str(num2), str(ans))
    except Exception as e:
        print(e)
    finally:
        print(intake)
