Desafio de Automação de API

Este projeto automatiza e valida o fluxo de gerenciamento de livros de uma API. 
Ele utiliza o padrão Page Object Model (adaptado para a API) e dados dinâmicos para garantir que os testes sejam robustos e confiáveis.

Tecnologias Utilizadas
  - Python: Linguagem principal.
  - Pytest: Framework de testes.
  - Requests: Biblioteca para testes de API.
  - Faker: Geração de dados de teste.

Requisitos Alcançados
  - Criação de Usuário e Autenticação: O teste cria um novo usuário, gera um token de acesso e valida que o usuário está autorizado a usar a API.
  - Gestão de Livros: O teste lista os livros disponíveis, adiciona dois livros ao perfil do usuário e valida se a adição foi bem-sucedida.
  - Detalhes do Usuário: A automação lista os detalhes do usuário, incluindo os livros que foram alugados, e valida a resposta da API.

Para Rodar
- Instale as dependências:
    pip install -r requirements.txt
  
- Rode os testes:
  pytest -s tests/test_book_store.py

