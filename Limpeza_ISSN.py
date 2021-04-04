import pandas as pd

teste = pd.read_excel('teste.xlsx')

df = pd.DataFrame(teste)

lista_ISSN = list()

for x in df.index:
    ISSN = df.loc[x,"ISSN"]      
    if ISSN not in lista_ISSN:
        lista_ISSN.append(ISSN)        
    else:
        df.drop(x, inplace = True)
    
df.to_excel (r'ISSN.xlsx',index = False)
