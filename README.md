# Gestor Financeiro Pessoal

Aplicação de gestão financeira pessoal desenvolvida em Python, com interface interativa em Streamlit e armazenamento de dados em SQLite.

O projeto foi criado com o objetivo de praticar desenvolvimento Python, manipulação de dados, persistência em banco de dados, visualização de informações e testes automatizados.

## Funcionalidades

- Cadastro de receitas e despesas.
- Edição e exclusão de transações.
- Cálculo automático do saldo financeiro.
- Histórico de transações.
- Filtros por tipo e categoria.
- Gráfico de receitas versus despesas.
- Gráfico de despesas por categoria.
- Testes automatizados da lógica de cálculo do saldo.

## Tecnologias utilizadas

- **Python** — lógica e processamento dos dados.
- **Streamlit** — interface web interativa.
- **SQLite** — armazenamento local das transações.
- **unittest** — testes automatizados.
- **Git e GitHub** — controle de versão e hospedagem do código.

## Como executar o projeto

### 1. Pré-requisitos

- Python instalado.
- Git instalado.
- Terminal ou editor de código, como o PyCharm.

### 2. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
cd gestor-financeiro
```

Substitua `URL_DO_SEU_REPOSITORIO` pela URL real do repositório no GitHub.

### 3. Crie um ambiente virtual

No Windows:

```powershell
python -m venv .venv
```

Ative o ambiente virtual:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Instale a dependência

```bash
python -m pip install streamlit
```

### 5. Execute a aplicação

```bash
streamlit run app.py
```

O Streamlit disponibilizará um endereço local para acessar a aplicação pelo navegador.

## Como executar os testes

Com o ambiente configurado, execute:

```bash
python -m unittest test_financeiro.py
```

Os testes verificam diferentes cenários da função de cálculo do saldo financeiro.

## Armazenamento dos dados

O projeto utiliza SQLite e cria o banco de dados localmente durante a inicialização da aplicação.

O arquivo `financeiro.db` não é versionado no Git, pois contém dados locais do usuário.

## Aprendizados

Este projeto permitiu praticar:

- Organização de código em módulos.
- Operações CRUD (criar, consultar, atualizar e excluir registros).
- Consultas SQL parametrizadas.
- Construção de interfaces com Streamlit.
- Agregação e visualização de dados.
- Testes automatizados.
- Controle de versão com Git.

## Próximas melhorias

- Adicionar filtros por período.
- Criar testes para outras funcionalidades.
- Melhorar a validação dos dados.
- Implementar relatórios financeiros.
- Disponibilizar uma demonstração online.

---

**Projeto de portfólio em desenvolvimento.**
