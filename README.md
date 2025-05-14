# Payflex Analytics

<p align="center">
  <img src="https://cdn2.hubspot.net/hub/7379058/hubfs/Accepting%20a%20credit%20card%20at%20a%20terminal.png" width="50%">
</p>

## Estrutura de Projeto
```plaintext
payflex-analytics/
├──  README.md
├──  pyproject.toml              # Arquivo de configuração utilizado pela biblioteca uv
├──  dashboards/
│ └── dashboard.pbi             # Arquivo PowerBI
├──  datasets/                  # Dados brutos
│ ├─  clientes.csv
│ ├─  estabelecimentos.csv
│ ├─  output.csv                # Output que alimentará o PowerBI
│ ├─  relacao_transacao_cliente.csv
│ └── transacoes.csv
├── notebook/                   # Códigos-fonte
│ └── notebook.ipynb            # Análise exploratória e perguntas do negócio
├──  utils/
│ ├─  utils.py                  # Funções auxiliares
│ └── plot_config.py            # Classe de visualização
```

## Objetivos do Projeto
Este projeto simula o desafio de uma adquirente de cartões que processa transações de crédito e débito para diversos estabelecimentos. O objetivo é realizar o tratamento, análise e visualização dos dados transacionais sobre o comportamento dos clientes e os padrões de venda dos estabelecimentos.

## Etapas do Projeto
1. Tratamento e Engenharia de Dados
2. Análise e KPIs
3. Dashboard em PowerBI


## Tecnologias e Conceitos Aplicados
Bibliotecas Principais
- pandas (tratamento e manipulação de dados)
- pylab, matplotlib e seaborn (criação de gráficos)

Programação Orientada a Objetos (POO)
- Criação de uma classe (PlotUtils) para centralizar a geração de gráficos
- Vantagens:
  - Reutilização de código (evitando duplicação)
  - Manutenção simplificada (definir parâmetros repetitivos e ajustes de estilo em um único local)
  - Legibilidade (código modular e organizado)

<br>

## Sobre o dataset
Os arquivos fornecidos (todos em formato .csv) incluem 3 tabelas dimensões e uma fato. Após o tratamento foi gerado a tabela output.
  - clientes
  - estabelecimentos
  - relação transação-cliente
  - transações (fato)
  - output

<br>

## Entregáveis
- notebook.ipynb - Jupyter Notebook com o tratamento de dados, análises exploratórias, gráficos e comentários explicativos.
- dashboard.pbix - Arquivo com o final co, report voltado para análise gerencial

<br> 

## Instruções de Setup
0. Pré-Requisitos
    - Python versão > 3.12
    - Biblioteca uv (instale usando o comando `pipx install uv` ou `pip install uv`)


<br>

1. Clone o repositório e mude o diretório
```bash
git clone https://github.com/kajinmo/payflex-analytics
cd payflex-analytics
```

<br>

2. Crie um ambiente venv e instale as dependências com `uv`
```bash
uv sync
```

<br>

3. Ative o ambiente virtual
```bash
source .venv/Scripts/activate
```

<br>

4. Abra o VSCode
```bash
code .
```

<br>

5. Configurar o VSCode para usar o ambiente virtual

- Abrir o Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS)
- Procure por "`Python: Select Interpreter`"
- Escolha o interpretador dentro da pasta `.venv` (e.g., .venv/bin/python or .venv\Scripts\python.exe)