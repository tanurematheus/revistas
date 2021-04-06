import pandas as pd   

base = pd.read_excel('Qualis_Antigo_ISSN.xlsx')
base2 = pd.read_excel('Qualis_Novo_ISSN.xlsx')

Qualis_Antigo = pd.DataFrame(base)
Qualis_Novo = pd.DataFrame(base2)

resultado = pd.merge(left = Qualis_Antigo, right = Qualis_Novo,how ='inner',suffixes=('_Antigo','_Novo'), on = 'Título') 

resultado.rename(columns={'Unnamed: 0' : 'ID_ISSN_Antigo'}, inplace = True)

resultado = resultado[['ID_ISSN_Antigo', 'Título', 'ISSN_Antigo', 'ISSN_Novo']]

resultado.to_excel (r'output.xlsx',index = False)             