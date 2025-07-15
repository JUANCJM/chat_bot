import pyautogui, webbrowser
from time import sleep
import schedule
import time

grupo_id = "FMa4NL1gRuaL3oExFH6K3l"
mensaje_enviado = False

def enviar_mensaje():
    global mensaje_enviado
    print("Enviando mensaje al grupo...")
    webbrowser.open(f"https://web.whatsapp.com/accept?code={grupo_id}")
    sleep(10)  # Espera a que cargue WhatsApp Web y el grupo
    pyautogui.typewrite("hola grupo, este es un mensaje de xXJUANCJMXx")  # Cambia el texto aquí
    pyautogui.press("enter")
    sleep(2)
    pyautogui.hotkey('ctrl', 'w')
    print("Mensaje enviado y cliente cerrado.")
    mensaje_enviado = True

hora_envio = "09:02"  # Cambia la hora aquí
print(f"Esperando para enviar mensaje al grupo a las {hora_envio}...")
schedule.every().day.at(hora_envio).do(enviar_mensaje)

while not mensaje_enviado:
    schedule.run_pending()
    time.sleep(1)

print("Script finalizado.")