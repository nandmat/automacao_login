import pyautogui
import pyperclip
import time
import getpass

print("Olá, Nanderson. Seja bem vindo!")
print("Bons estudos e boas práticas")

#receber usuário e senha:
email = "nandersonmatheusmelo@gmail.com"
senha = getpass.getpass("Digite sua senha de acesso:")
    
pyautogui.PAUSE = 2

#Entrar no site do Canvas
pyautogui.press('win')
pyautogui.click(x=55, y=751)
pyautogui.write("Google Chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=671, y=429)
time.sleep(3)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://canvas.instructure.com/login/canvas")
time.sleep(0.5)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(2)

#Navegar até a caixa de login do 
pyautogui.click(x=676, y=293)
pyperclip.copy(email)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.click(x=671, y=371)

#Navegar até a caixa da senha
pyperclip.copy(senha)
pyautogui.hotkey("ctrl", "v")
time.sleep(1.5)
#Enviar os dados para validação
pyautogui.press("enter")

#Entrar no youtube no set do Breaking Beats
pyautogui.hotkey("ctrl", "t")
time.sleep(1.8)
pyperclip.copy("https://www.youtube.com/watch?v=PrczFRuLgBc&t=1236s")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.press("enter")
