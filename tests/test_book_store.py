# importando pytest, classe definida e uuid para gerar usuários únicos
import pytest
from api_client.book_store_api import BookStoreAPI
import uuid

# dados para teste. senha deve seguir o formato abaixo
PASSWORD = "Testeaccenture123!@#$%"
BASE_URL = "https://demoqa.com"

# criando o cliente da API
@pytest.fixture(scope="session")
def api_client():
    return BookStoreAPI(BASE_URL)

# executando a criação de usuário e geração de token
@pytest.fixture(scope="session")
def user_data(api_client):
    # gerando um nome de usuário único
    unique_username = f"teste_accenture_{uuid.uuid4()}"

    # cria um usuário e verifica se o status retornado é 201 (Created)
    user_response = api_client.create_user(unique_username, PASSWORD)
    assert user_response.status_code == 201
    user_id = user_response.json().get("userID")
    assert user_id is not None

    # gera um token e verifica se foi criado
    token_response = api_client.generate_token(unique_username, PASSWORD)
    token = token_response.json().get("token")
    assert token is not None

    # retorna os dados que o teste principal vai precisar
    return {"user_id": user_id, "token": token, "username": unique_username}

# função do teste - fixtures são os argumentos
def test_full_api_flow(api_client, user_data):
    # pega os dados retornados pela fixture 'user_data'
    user_id = user_data["user_id"]
    token = user_data["token"]
    username = user_data["username"]

    # confirma se o usuário está autorizado
    authorized_response = api_client.is_authorized(username, PASSWORD)
    assert authorized_response.status_code == 200
    assert authorized_response.text == "true"
    print("\n autorização do usuário validada com sucesso.")

    # lista os livros e valida se existem livros cadastrados
    books_response = api_client.get_all_books()
    assert books_response.status_code == 200
    all_books = books_response.json()["books"]
    assert len(all_books) >= 2
    print("\n lista de livros obtida com sucesso.")

    # seleciona e adiciona dois livros
    books_to_add = all_books[:2]
    books_isbns = [book["isbn"] for book in books_to_add]
    add_books_response = api_client.add_books_to_user(user_id, token, books_isbns)
    # valida se os livros foram adicionados com sucesso
    assert add_books_response.status_code == 201
    print("\n livros adicionados à conta do usuário com sucesso.")

    # lista os detalhes do usuário para validação final
    user_info_response = api_client.get_user_info(user_id, token)
    assert user_info_response.status_code == 200
    user_books = user_info_response.json()["books"]

    # valida se os livros adicionados estão no perfil do usuário
    added_isbns = {book["isbn"] for book in user_books}
    for isbn in books_isbns:
        assert isbn in added_isbns
        print("\n validação final de que os livros estão no perfil do usuário.")

    print("\n desafio de API concluído com sucesso!")