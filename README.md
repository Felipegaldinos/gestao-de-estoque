# Gestão de Estoque em Python

Aplicação de terminal para cadastrar e consultar produtos, atualizar quantidades e preços e remover itens. Um projeto introdutório de operações CRUD usando listas e dicionários.

## Funcionalidades

- Cadastro de nome, quantidade e preço.
- Atualização de quantidade ou preço de um produto.
- Busca e remoção por nome.
- Listagem com preços formatados em reais.
- Menu interativo com seis opções.

## Tecnologias

Python 3 e biblioteca padrão; sem dependências externas.

## Como executar

Instale Python 3 e execute na pasta do projeto:

```sh
git clone https://github.com/Felipegaldinos/gestao-de-estoque.git
cd gestao-de-estoque
python estoque.py
```

Não é necessário instalar pacotes com pip.

## Organização do código

- `estoque.py` — estrutura em memória, funções de operação e menu interativo.

## Roteiro de demonstração

Cadastre Caneta com quantidade 10 e preço 2.50, liste, busque Caneta, atualize a quantidade e remova o produto. Use ponto como separador decimal.

## Limitações atuais

Os produtos ficam apenas na lista estoque e são perdidos ao encerrar. A busca compara o nome exato. Entradas numéricas inválidas podem encerrar a execução, e não há bloqueio de valores negativos ou nomes duplicados. É um exercício de terminal, sem banco de dados ou interface web.

## Competências demonstradas

Fundamentos de Python: funções, estruturas de dados, repetição e operações CRUD.

## Autoria

Projeto disponível no perfil de [Felipe Galdino](https://github.com/Felipegaldinos). Consulte os arquivos do repositório para verificar os termos de licença aplicáveis.
