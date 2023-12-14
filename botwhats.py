from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import keyboard
import time

def enviar_mensagem_whatsapp(contato, mensagem):
    # Configurando o ChromeDriver
    servico = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()  # Ativa o modo headless (sem interface gráfica)

    # Inicializando o navegador
    navegador = webdriver.Chrome(service=servico, options=options)

    # URL do WhatsApp Web
    whatsapp_url = 'https://web.whatsapp.com/'

    # Abre o WhatsApp Web
    navegador.get(whatsapp_url)

    # Aguarde o usuário fazer o login manualmente
    input("Faça o login manualmente e pressione Enter quando estiver pronto...")

    # Monta a URL com o número do contato
    url_contato = f'https://web.whatsapp.com/send?phone={contato}&text={mensagem}'

    # Abre a URL
    navegador.get(url_contato)

    # Aguarda o tempo necessário para a página carregar completamente
    time.sleep(15)

    keyboard.press_and_release('tab')
    keyboard.press_and_release('enter')

    # Fecha o navegador
    navegador.quit()

# Exemplo de uso
contato_whatsapp = '+5511'  # Substitua pelo número de telefone desejado
mensagem_whatsapp = 'Olá, isso é um teste!'
enviar_mensagem_whatsapp(contato_whatsapp, mensagem_whatsapp)
