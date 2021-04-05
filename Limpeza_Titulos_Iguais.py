import pandas as pd

teste = pd.read_excel('ISSN.xlsx')

df = pd.DataFrame(teste)

lista_nomes = list()

for x in df.index:
    nome = df.loc[x,"Título"]      
    if nome not in lista_nomes:
        lista_nomes.append(nome)        
    else:
        df.drop(x, inplace = True)
    
df.to_excel (r'Titulos.xlsx',index = False)