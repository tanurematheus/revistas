import pandas as pd

teste = pd.read_excel('Titulos.xlsx')

df = pd.DataFrame(teste)

lista_nomes = list()

for x in df.index:
    nome = df.loc[x,"Título"]
    nome_split = nome.split('(')
    df.loc[x,"Título"] = nome_sem_parenteses = nome_split[0].strip()      
    if nome_sem_parenteses not in lista_nomes:
        lista_nomes.append(nome_sem_parenteses)        
    else:
        df.drop(x, inplace = True)
    
df.to_excel (r'Titulos_Sem_Parentesis.xlsx',index = False)