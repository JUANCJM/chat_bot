import irc.client
import time
import threading

# Configura estos valores
server = "irc.chat.twitch.tv"
port = 6667
nickname = "xxjuancjmxx"
token = "oauth:j1ikoit1zvcdool9iocxhz9uyhi5vh"
canal = "#elcrissenpaii"  # Siempre con #

# Crear conexión IRC
reactor = irc.client.Reactor()

def enviar_mensaje(conn):
    while True:
        mensaje = "hola, soy xXJUANCJMXx ya llegue para apoyarte!"
        conn.privmsg(canal, mensaje)
        print(f"Mensaje enviado: {mensaje}")
        time.sleep(400)  # 50 segundos
        msj1 = "que anime es?"
        conn.privmsg(canal, msj1)
        print(f"Mensaje enviado: {msj1}")
        time.sleep(400)
        msj2 = "Esta interesante, es la primaera vez que lo veo!!"
        conn.privmsg(canal, msj2)
        print(f"Mensaje enviado: {msj2}")
        time.sleep(400)
        msj3 = "buen anime!, GG"
        conn.privmsg(canal, msj3)
        print(f"Mensaje enviado: {msj3}")
        time.sleep(400)
        msj3 = "la estas flipando tio, sigue así"
        conn.privmsg(canal, msj3)
        print(f"Mensaje enviado: {msj3}")
        time.sleep(1800)  # 1800 segundos = 30 minutos

def on_connect(connection, event):
    connection.join(canal)
    # Inicia el hilo para enviar mensajes periódicos
    threading.Thread(target=enviar_mensaje, args=(connection,), daemon=True).start()

try:
    conn = reactor.server().connect(server, port, nickname, password=token)
    conn.add_global_handler("welcome", on_connect)
    reactor.process_forever()
except irc.client.ServerConnectionError as e:
    print(f"Error de conexión: {e}")
