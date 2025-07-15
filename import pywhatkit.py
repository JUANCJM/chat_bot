import pywhatkit
numero = "+529931744349"
msg = "Hola, este es un mensaje de prueba enviado desde un script de Python."
pywhatkit.sendwhatmsg_instantly(numero, msg, tab_close=True)
