import pandas as pd

teste = pd.read_excel('Questao.xlsx')

s = pd.Series(teste['Qualise_Novo'])

s.dropna()

s.to_excel (r'Qualis_Novo.xlsx',index = False)

teste = pd.read_excel('Qualis_Novo.xlsx')

s = pd.Series(teste['Qualise_Novo'])

lista_nomes = list()

for x in s.index:
    nome = s.loc[x]
    nome_split = nome.split('(')
    s.loc[x] = nome_sem_parenteses = nome_split[0].strip()      
    if nome_sem_parenteses not in lista_nomes:
        lista_nomes.append(nome_sem_parenteses)        
    else:
        s.drop(x, inplace = True)

s.to_excel (r'Qualis_Novo.xlsx',index = False)