
-----

# Mapeamento do Perfil de Clientes para Otimização de Campanhas de Investimento

Este projeto realiza uma análise exploratória de dados para identificar o perfil de clientes com maior propensão a adquirir um novo produto de investimento. O objetivo é fornecer insights de negócio para a equipe de Marketing, otimizando futuras campanhas de prospecção.

## 📁 Estrutura do Projeto

O projeto consiste em um único script Python e um arquivo de dados:

  * `analise_banco.py`: O script principal que carrega os dados, realiza a análise e gera gráficos.
  * `bank_marketing.xlsx`: O arquivo de dados original contendo informações dos clientes da campanha piloto.

## 🚀 Como Rodar o Projeto

Siga estes passos para executar a análise no seu ambiente local.

### 1\. Pré-requisitos

Certifique-se de que o **Python** está instalado em seu computador. Em seguida, instale as bibliotecas necessárias usando o `pip`:

```bash
pip install pandas openpyxl matplotlib
```

### 2\. Configuração

Coloque o arquivo `bank_marketing.xlsx` na mesma pasta do script `analise_banco.py`.

### 3\. Execução

Abra o terminal ou prompt de comando na pasta do projeto e execute o script:

```bash
python analise_banco.py
```

Após a execução, o script irá exibir as tabelas de porcentagens no terminal e salvar os gráficos de análise na mesma pasta. Os gráficos gerados são:

  * `distribuicao_idade.png`
  * `compra_por_profissao.png`
  * `compra_por_devedor.png`
  * `compra_por_hipoteca.png`
  * `compra_por_emprestimo.png`

## 📊 Análise e Insights de Negócio

A análise exploratória de dados permitiu extrair as seguintes conclusões sobre o perfil de clientes:

  * **Idade e Profissão:** A propensão de compra é significativamente maior em clientes mais velhos. Profissionalmente, **aposentados** (67,8% de taxa de compra) e **estudantes** (75% de taxa de compra) são os grupos com maior adesão ao produto.

  * **Saúde Financeira:** Clientes com histórico de inadimplência (`devedores`) demonstram uma baixa taxa de compra (26,15%). **Recomendação:** A equipe de marketing deve evitar este público.

  * **Relacionamento com o Banco:** A posse de **hipoteca** ou **empréstimo** não demonstrou ter um impacto significativo na decisão de compra. As taxas de adesão entre os grupos com e sem esses produtos foram muito similares. **Recomendação:** A equipe não precisa segmentar o público com base nessas características.

-----

## 📈 Conclusão

Para futuras campanhas de marketing, o perfil de cliente mais promissor é: **alguém mais velho, aposentado ou estudante, e que não tenha histórico de inadimplência.**

Ao focar a prospecção nesse perfil, a empresa pode aumentar a taxa de conversão e otimizar o retorno sobre o investimento da campanha.