import pyautogui, webbrowser
from time import sleep
import schedule
import time

numero = "+529931058957"
mensaje_enviado = False

def enviar_mensaje():
    global mensaje_enviado
    print("Enviando mensaje...")
    webbrowser.open("https://web.whatsapp.com/send?phone=" + numero)
    sleep(10)  # Espera a que cargue WhatsApp Web
    pyautogui.typewrite("hola thefirewolfplay estes es un msj")  # Cambia el texto aquí
    pyautogui.press("enter")
    sleep(2)  # Espera a que se envíe el mensaje
    pyautogui.hotkey('ctrl', 'w')  # Cierra la pestaña del navegador
    print("Mensaje enviado y cliente cerrado.")
    mensaje_enviado = True

# Programa el envío a la hora deseada
hora_envio = "08:35"  # Cambia la hora aquí
print(f"Esperando para enviar mensaje a las {hora_envio}...")
schedule.every().day.at(hora_envio).do(enviar_mensaje)

while not mensaje_enviado:
    schedule.run_pending()
    time.sleep(1)

print("Script finalizado.")