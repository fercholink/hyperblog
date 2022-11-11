# Enviar mensajes ilimitados a whatsapps

import pyautogui as spam    
import time

limite = input ('Numero para enviar mensajes: ')
mensaje = input ('Escribir mensaje?: ')

i = 0


time.sleep(5)

while i<int(limite):
    spam.typewrite(mensaje)
    spam.press('Enter')
    i+=1
    print('Enviado')

    