import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Carregando o arquivo, pulando a linha bagunçada
df = pd.read_excel('bank_marketing.xlsx', header=1)

# Remove os espaços em branco extras dos nomes das colunas
df.columns = df.columns.str.strip()

# Agora o nome da coluna deve estar correto
comprou = df[df['Cliente_Comprou_o_Titulo?'] == 'Sim']
nao_comprou = df[df['Cliente_Comprou_o_Titulo?'] == 'Não']

# Criando o histograma para cada grupo
plt.figure(figsize=(10, 6))
plt.hist(comprou['Idade'], bins=20, edgecolor='black', alpha=0.6, label='Comprou')
plt.hist(nao_comprou['Idade'], bins=20, edgecolor='black', alpha=0.6, label='Não Comprou')
plt.title('Distribuição de Idade por Resultado de Compra')
plt.xlabel('Idade')
plt.ylabel('Número de Clientes')
plt.legend()
plt.savefig('distribuicao_idade.png')

# Seu código para carregar os dados aqui

# Crie uma tabela de contingência para ver a relação entre Profissão e Compra
contingencia = pd.crosstab(df['Profissão'], df['Cliente_Comprou_o_Titulo?'], normalize='index') * 100
print(contingencia)

# Opcional: crie um gráfico para visualizar
contingencia.plot(kind='bar', figsize=(12, 7))
plt.title('Taxa de Compra por Profissão')
plt.ylabel('Porcentagem de Compra')
plt.xlabel('Profissão')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Comprou o Título?')
plt.tight_layout()
plt.savefig('compra_por_profissao.png') # Salva o gráfico


# Cria uma tabela de contingência para ver a relação entre Ser Devedor e a Compra do Produto
contingencia_devedor = pd.crosstab(df['Cliente_Devedor?'], df['Cliente_Comprou_o_Titulo?'], normalize='index') * 100
print(contingencia_devedor)

# Opcional: crie um gráfico para visualizar
contingencia_devedor.plot(kind='bar', figsize=(8, 6))
plt.title('Taxa de Compra por Histórico de Inadimplência')
plt.ylabel('Porcentagem de Compra')
plt.xlabel('Cliente Devedor?')
plt.xticks(rotation=0)
plt.legend(title='Comprou o Título?')
plt.tight_layout()
plt.savefig('compra_por_devedor.png')

# Cria uma tabela de contingência para ver a relação entre ter Hipoteca e a Compra do Produto
contingencia_hipoteca = pd.crosstab(df['Tem_Hipoteca?'], df['Cliente_Comprou_o_Titulo?'], normalize='index') * 100
print(contingencia_hipoteca)

# Opcional: crie um gráfico para visualizar
contingencia_hipoteca.plot(kind='bar', figsize=(8, 6))
plt.title('Taxa de Compra por Posse de Hipoteca')
plt.ylabel('Porcentagem de Compra')
plt.xlabel('Tem Hipoteca?')
plt.xticks(rotation=0)
plt.legend(title='Comprou o Título?')
plt.tight_layout()
plt.savefig('compra_por_hipoteca.png')

# Cria uma tabela de contingência para ver a relação entre ter Empréstimo e a Compra do Produto
contingencia_emprestimo = pd.crosstab(df['Tem_Emprestimo?'], df['Cliente_Comprou_o_Titulo?'], normalize='index') * 100
print(contingencia_emprestimo)

# Opcional: crie um gráfico para visualizar
contingencia_emprestimo.plot(kind='bar', figsize=(8, 6))
plt.title('Taxa de Compra por Posse de Empréstimo')
plt.ylabel('Porcentagem de Compra')
plt.xlabel('Tem Empréstimo?')
plt.xticks(rotation=0)
plt.legend(title='Comprou o Título?')
plt.tight_layout()
plt.savefig('compra_por_emprestimo.png')