# Gestão Fácil

O Gestão Fácil é um sistema web desenvolvido em Python com Flask, SQLite e SQLAlchemy, voltado para o controle de estoque e gerenciamento de produtos.

O projeto foi desenvolvido como parte da avaliação da disciplina de Tópicos Integradores, com o objetivo de aplicar conceitos de desenvolvimento web, banco de dados, engenharia de requisitos, arquitetura de software e organização de projeto.

## Funcionalidades

- Cadastro de produtos
- Listagem de produtos no dashboard
- Edição de produtos
- Exclusão de produtos
- Controle de quantidade em estoque

## Tecnologias utilizadas

- Python
- Flask
- SQLite
- SQLAlchemy
- HTML
- CSS

## Estrutura do projeto

```text
Gestao_Facil/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── database/
│   ├── __init__.py
│   └── db.py
│
├── static/
│   └── py.css
│
└── templates/
    ├── login.html
    ├── dashboard.html
    ├── cadastro_produto.html
    ├── editar_produto.html
    ├── estoque.html
    └── relatorios.html
