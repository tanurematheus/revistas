import pandas as pd   

base = pd.read_excel('output_limpeza_iguais.xlsx')

df = pd.DataFrame(base)

x=0

z = len(df.index)-1

while x < z: 
    
    titulo = df.loc[x,'Título']
    titulo2 = df.loc[x+1,'Título']
    
    if titulo == titulo2:
        issn_novo = df.loc[x,'ISSN_Novo']
        issn_novo = issn_novo.split('‐')    
        issn_antigo = df.loc[x,'ISSN_Antigo'] 
        issn_antigo = issn_antigo.split('-')

        issn_novo2 = df.loc[x+1,'ISSN_Novo']
        issn_novo2 = issn_novo2.split('‐')    
        issn_antigo2 = df.loc[x+1,'ISSN_Antigo'] 
        issn_antigo2 = issn_antigo2.split('-')  

        if ((issn_antigo == issn_novo2) and (issn_antigo2 == issn_novo)):
            df.drop(x, inplace = True)
            df.drop(x+1, inplace = True)
            x+=1 
    x+=1          

df.to_excel (r'Base_Final.xlsx',index = False)  