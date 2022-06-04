from bs4 import BeautifulSoup
import requests
import pyautogui
import time

def bot_bomdia(url, tag):
    time.sleep(5)
    req = requests.get(url)
    parse = BeautifulSoup(req.text, 'html.parser')
    html = parse.find_all(tag)
    for mensagem in html:
        pyautogui.typewrite(mensagem.get_text())
        pyautogui.press("enter")

def bot_oi(msg, qtd):
    time.sleep(5)
    pyautogui.typewrite(f'Sequência de {qtd} {msg}')
    pyautogui.press("enter")
    for i in range(qtd):
        pyautogui.typewrite(f'{i+1} - {msg} ')
        pyautogui.press("enter")


#bot_bomdia('https://www.mensagens10.com.br/mensagens-de-bom-dia', 'p')
msg = input("Digite a mensagem\n")
qtd = int(input("Digite a quantidade\n"))
bot_oi(msg, qtd)
