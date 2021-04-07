import pandas as pd   

base = pd.read_excel('output.xlsx')

df = pd.DataFrame(base)

for x in df.index:
    issn_novo = df.loc[x,'ISSN_Novo']
    issn_novo = issn_novo.split('‐')    
    issn_antigo = df.loc[x,'ISSN_Antigo'] 
    issn_antigo = issn_antigo.split('-') 
    if issn_antigo == issn_novo:
        df.drop(x, inplace = True)   

df.to_excel (r'output_limpeza_iguais.xlsx',index = False)             