import pandas as pd

# Lê todos os dados da planilha 'planilha.xlsx'
df = pd.read_excel('dadosEvento.xlsx')

# Lê apenas a aba 'Dados' da planilha 'planilha.xlsx'
df = pd.read_excel('dadosEvento.xlsx', sheet_name='Planilha1')

# Imprime os dados
print(df)cos
