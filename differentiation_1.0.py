from os import system
def inverse_trigo(func,x):
    dic={'sin^-1':f'{differ(x)}/(1-({x})^2)^1/2','cos^-1':f'-{differ(x)}/(1-({x})^2)^1/2','tan^-1':f'{differ(x)}/1+({x})^2','cot^-1':f'-{differ(x)}1/1+({x})^2','sec^-1':f'{differ(x)}/|{x}|(({x})^2-1)^1/2','cosec^-1':f'-{differ(x)}/|{x}|(({x})^2-1)^1/2'}
    return dic[func]
def div_rule(equation):
    pos=equation.index('/')
    equa1=equation[:pos]
    equa2=equation[pos+1:]
    return equa2+'*'+differ(equa1)+'-'+equa1+'*'+differ(equa2)+'/('+equa2+')^2'
def multi_rule(equation):
    ind=equation.index('*')
    eque1=equation[:ind]
    eque2=equation[ind+1:]
    return eque1+'*'+differ(eque2)+'+'+eque2+'*'+differ(eque1)
def trigo_diff(func,x,num):
    func_dict=dict(sin=num+'*'+"cos"+x,cos='-'+num+'*'+"sin"+x,tan=num+'*'+'('+"sec"+x+')^2',cot='-'+num+'*'+'('+"cosec"+x+')^2',sec=num+'*'+"sec"+x+"."+"tan"+x,cosec="-"+num+'*'+"cosec"+x+"."+"cot"+x)
    return func_dict[func]
def trigo_diff_initial(intake):   
    func=["sin","cosec","tan","cot","sec","cos"]
    intake=intake.split()
    symbols=['+','-']
    k=0
    for j in intake:
        if j in symbols:
            k+=1
            continue
        for i in func:
            if i in j:
                if i != "cosec":
                    ind=j.index(i)
                    function=j[ind:ind+3]
                    x=j[j.index(i[-1])+1:]
                    if '(' not in x:
                        num=differ(x)
                    else:
                        temp=x.replace('(','',1)
                        num=differ(temp.replace(')','',1))
                    break
                else:
                    ind=j.index(i)
                    function=j[ind:ind+5]
                    x=j[j.index("c",1)+1:]
                    if '(' not in x:
                        num=differ(x)
                    else:
                        temp=x.remove('(')
                        num=differ(temp.remove(')',-1))
                    break
        if num=='':
            num='1'
        intake[k]=trigo_diff(function,x,num)
        k+=1 
    intake=' '.join(intake)
    while True:
        if '+ -' in intake:
            intake=intake.replace('+ -','- ')
        elif '- -' in intake:
            intake=intake.replace('- -','+ ')
        else:
            break
    return intake
def differ(equation):
    if '+' in equation:    
        equation.replace('+',' + ')
    if '-' in equation:   
        equation.replace('-',' - ')
    equation_raw=equation.split(' ')
    j=0
    for i in equation_raw:
        if '*' in i or '/' in i or '(' in i:
            chain,multi,div=100,100,100
            if '*' in i:
                multi=i.index('*')
            if '/' in i:
                div=i.index('/')
            if '(' in i:
                chain=i.index('(')
            if div>multi and chain>multi:
                equation_raw[j]=multi_rule(i)
            elif chain<div:
                if chain!=0:
                    func=i[:chain]
                    operand=i[chain+1:i.index(')',-1)]
                else:
                    func=i[i.index(')')+1:]
                    operand=i[1:i.index(')')]
                if 'log' == func:
                    ans='('+differ(operand)+')'+'/'+ operand
                    if '()' in ans:
                        equation_raw[j]=ans.replace('()','1')
                    else:
                        equation_raw[j]=ans
                elif func in ['sin','cos','tan','cot','sec','cosec']:
                    equation_raw[j]=trigo_diff_initial(i)
                elif '^' in func:
                    if '^-1' in func:
                        equation_raw[j]=inverse_trigo(func,operand)
                    else:
                        x=i[chain+1:i.index(')')]
                        n=func[func.index('^')+1:]
                        equation_raw[j]=n+'('+x+')'+'^'+str(int(n)-1)+'*'+differ(x)
            else:
                equation_raw[j]=div_rule(i)   
        else:
            if i=='+' or i=='-':
                continue
            if 'log' in i:
                if '(' not in i:
                    ans_raw=i[i.index('log')+3:]
                else:    
                    ans_raw=i[i.index('(')+1:i.index(')',-1)]
                ans='('+differ(ans_raw)+')'+'/'+ ans_raw
                if '()' in ans:
                    ans=ans.replace('()','1')
                equation_raw[j]=ans
            elif 'sin' in i or 'cos' in i or 'tan' in i or 'cot' in i or 'cosec' in i or 'sec' in i:
                equation_raw[j]=trigo_diff_initial(i)
            elif '^' in i:
                if '^-1' in i:
                    equation_raw[j]=inverse_trigo(i[:i.index('^-1')+3],i[i.index('^-1')+3:])
                else:
                    indx=i.index('^')
                    x=i[:indx]
                    n=i[indx+1:]
                    if len(x)==1:
                        if int(n)==1:
                            ans=str(1)
                        elif int(n)==2:
                            ans=n+x
                        else:
                            ans=n+x+'^'+str(int(n)-1)
                    else:
                        indx=i.index('x')
                        a=int(i[:indx])
                        if int(n)==1:
                            m=str(int(n)*a)
                            ans=m+'x'+'^'+str(int(n)-1)
                        elif int(n)==2:
                            m=str(int(n)*a) 
                            ans=m+'x'
                        else:
                            m=str(int(n)*a) 
                            ans=m+'x'+'^'+str(int(n)-1)
                    equation_raw[j]=ans
            elif 'x' in i:
                equation_raw[j]=i.replace('x','1')
                if '/' in equation_raw[j]:
                    if equation_raw[j].index('/')==0:
                        equation_raw[j]='1'+equation_raw[j]
            elif 'x' not in i:
                equation_raw[j]='0'
        j+=2
    equation_ans=' '.join(equation_raw)
    equation_ans=equation_ans.replace('+ -','- ')
    equation_ans=equation_ans.replace('- -','+ ')
    if '0' in equation_ans:
        count=equation_ans.index('0')
        equation_ans=equation_ans.replace(equation_ans[count-1:count+1],'')
    return equation_ans
while True:    
    intake=input()
    if 'exit' in intake.lower():
        system('cls')
        break
    elif 'clear' in intake.lower():
        system('cls')
    else:
        print(differ(intake))