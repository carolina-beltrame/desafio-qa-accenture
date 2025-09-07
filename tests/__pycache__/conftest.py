# importando as bibliotecas 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

# definindo função de configuração do ambiente
@pytest.fixture(scope="function")
def driver():
    # instalando o driver do chrome e maximizando a janela
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # controle retorne para a função do teste
    yield driver
    # fechar o navegador
    driver.quit()
