# importando biblioteca para as requisições HTTP
import requests
# importando base64 para codificar autenticação
import base64

# definindo classe do cliente
class BookStoreAPI:
    def __init__(self, base_url):
        # construtor da classe 
        self.base_url = base_url
        # cabeçalho padrão
        self.headers = {"accept": "application/json"}

    def create_user(self, username, password):
        # requisição POST para criação de novo usuário
        endpoint = "/Account/v1/User"
        # dados a serem enviados
        payload = {
            "userName": username,
            "password": password
        }
        response = requests.post(f"{self.base_url}{endpoint}", json=payload)
        return response
    
    def generate_token(self, username, password):
        # requisição POST para geração de token para autorização
        endpoint = "/Account/v1/GenerateToken"
        # dados a serem enviados
        payload = {
            "userName": username,
            "password": password
        }

        response = requests.post(f"{self.base_url}{endpoint}", json=payload)
        return response

    def is_authorized(self, username, password):
        # verificando se o usuário é autorizado
        endpoint = "/Account/v1/Authorized"
        # codificando usuário e senha para o formato 'base64'
        auth_string = f"{username}:{password}".encode("utf-8")
        auth_base64 = base64.b64encode(auth_string).decode("utf-8")
        
        # cabeçalho usado para autenticar a requisição
        headers = {"Authorization": f"Basic {auth_base64}"}
        # dados a serem enviados
        payload = {
            "userName": username,
            "password": password
        }
        
        response = requests.post(f"{self.base_url}{endpoint}", headers=headers, json=payload)
        return response 
    
    def get_all_books(self):
        # requisição GET para obter lista de todos os livros cadastrados
        endpoint = "/BookStore/v1/Books"
        response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers)
        return response
    
    def add_books_to_user(self, user_id, token, books_isbns):
        # requisição POST para adicionar livros para o perfil do usuário
        endpoint = "/BookStore/v1/Books"
        # cabeçalho utiliza o token gerado para autenticação
        headers = {**self.headers, "Authorization": f"Bearer {token}"}
        payload = {
            "userId": user_id,
            # lista com os ISBNs dos livrso
            "collectionOfIsbns": [{"isbn": isbn} for isbn in books_isbns]
        }
        response = requests.post(f"{self.base_url}{endpoint}", json=payload, headers=headers)
        return response
    
    def get_user_info(self, user_id, token):
        # requisição GET para pegar informações dos usuários e seus livrso
        endpoint = f"/Account/v1/User/{user_id}"
        headers = {**self.headers, "Authorization": f"Bearer {token}"}
        response = requests.get(f"{self.base_url}{endpoint}", headers=headers)
        return response