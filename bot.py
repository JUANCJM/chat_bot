import irc.client
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox

# Configura estos valores
server = "irc.chat.twitch.tv"
port = 6667
nickname = "xxjuancjmxx"
token = "oauth:j1ikoit1zvcdool9iocxhz9uyhi5vh"
canal = ""  # Se configurará desde la GUI

# Variables globales para el control del bot
reactor = None
connection = None
bot_running = False

def enviar_mensaje(conn):
    global bot_running
    while bot_running:
        mensaje = "hola, soy xXJUANCJMXx ya llegue para apoyarte!"
        conn.privmsg(canal, mensaje)
        print(f"Mensaje enviado a {canal}: {mensaje}")
        if not bot_running:
            break
        time.sleep(400)  # 50 segundos
        
        if not bot_running:
            break
        msj1 = "que anime es?"
        conn.privmsg(canal, msj1)
        print(f"Mensaje enviado a {canal}: {msj1}")
        if not bot_running:
            break
        time.sleep(400)
        
        if not bot_running:
            break
        msj2 = "Esta interesante, es la primaera vez que lo veo!!"
        conn.privmsg(canal, msj2)
        print(f"Mensaje enviado a {canal}: {msj2}")
        if not bot_running:
            break
        time.sleep(400)
        
        if not bot_running:
            break
        msj3 = "buen anime!, GG"
        conn.privmsg(canal, msj3)
        print(f"Mensaje enviado a {canal}: {msj3}")
        if not bot_running:
            break
        time.sleep(400)
        
        if not bot_running:
            break
        msj4 = "la estas flipando tio, sigue así"
        conn.privmsg(canal, msj4)
        print(f"Mensaje enviado a {canal}: {msj4}")
        if not bot_running:
            break
        time.sleep(1800)  # 1800 segundos = 30 minutos

def on_connect(connection, event):
    global bot_running
    connection.join(canal)
    print(f"Conectado al canal: {canal}")
    # Inicia el hilo para enviar mensajes periódicos
    bot_running = True
    threading.Thread(target=enviar_mensaje, args=(connection,), daemon=True).start()

def iniciar_bot(canal_destino):
    global reactor, connection, canal, bot_running
    
    try:
        canal = canal_destino
        reactor = irc.client.Reactor()
        connection = reactor.server().connect(server, port, nickname, password=token)
        connection.add_global_handler("welcome", on_connect)
        
        # Ejecutar en un hilo separado para no bloquear la GUI
        def run_bot():
            try:
                reactor.process_forever()
            except Exception as e:
                print(f"Error en el bot: {e}")
                
        threading.Thread(target=run_bot, daemon=True).start()
        return True
        
    except irc.client.ServerConnectionError as e:
        print(f"Error de conexión: {e}")
        return False

def detener_bot():
    global bot_running, connection, reactor
    bot_running = False
    if connection:
        try:
            connection.disconnect()
        except:
            pass
    if reactor:
        try:
            reactor.disconnect_all()
        except:
            pass

class ChatBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Bot - Configuración de Canal")
        self.root.geometry("450x300")
        self.root.resizable(False, False)
        
        # Variables
        self.canal_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Desconectado")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        titulo = ttk.Label(main_frame, text="Configuración del Chat Bot", 
                          font=("Arial", 14, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Campo de canal
        ttk.Label(main_frame, text="Canal de destino:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        canal_frame = ttk.Frame(main_frame)
        canal_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(canal_frame, text="#").grid(row=0, column=0)
        self.canal_entry = ttk.Entry(canal_frame, textvariable=self.canal_var, width=30)
        self.canal_entry.grid(row=0, column=1, padx=(0, 5))
        
        # Información
        info_text = "Ingresa el nombre del canal sin el símbolo #\nEjemplo: para #elcrissenpaii, escribe: elcrissenpaii"
        ttk.Label(main_frame, text=info_text, font=("Arial", 9), 
                 foreground="gray").grid(row=3, column=0, columnspan=2, pady=10)
        
        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)
        
        self.start_button = ttk.Button(button_frame, text="Iniciar Bot", 
                                      command=self.iniciar_bot)
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.stop_button = ttk.Button(button_frame, text="Detener Bot", 
                                     command=self.detener_bot, state="disabled")
        self.stop_button.grid(row=0, column=1, padx=5)
        
        # Estado
        status_frame = ttk.LabelFrame(main_frame, text="Estado", padding="10")
        status_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        self.status_label = ttk.Label(status_frame, textvariable=self.status_var)
        self.status_label.grid(row=0, column=0)
        
        # Configurar peso de columnas
        main_frame.columnconfigure(1, weight=1)
        canal_frame.columnconfigure(1, weight=1)
        
        # Foco inicial en el campo de entrada
        self.canal_entry.focus()
        
    def validar_canal(self, canal):
        if not canal.strip():
            return False, "El nombre del canal no puede estar vacío"
        
        canal = canal.strip()
        
        # Validar caracteres permitidos (letras, números, guiones bajos)
        import re
        if not re.match(r'^[a-zA-Z0-9_]+$', canal):
            return False, "El canal solo puede contener letras, números y guiones bajos"
        
        return True, ""
        
    def iniciar_bot(self):
        canal_nombre = self.canal_var.get().strip()
        
        # Validar entrada
        valido, mensaje = self.validar_canal(canal_nombre)
        if not valido:
            messagebox.showerror("Error", mensaje)
            return
            
        canal_completo = f"#{canal_nombre}"
        
        # Confirmar inicio
        if messagebox.askyesno("Confirmar", 
                              f"¿Iniciar el bot en el canal {canal_completo}?"):
            
            self.status_var.set("Conectando...")
            self.root.update()
            
            if iniciar_bot(canal_completo):
                self.status_var.set(f"Conectado a {canal_completo}")
                self.start_button.config(state="disabled")
                self.stop_button.config(state="normal")
                self.canal_entry.config(state="disabled")
                messagebox.showinfo("Éxito", f"Bot iniciado en {canal_completo}")
            else:
                self.status_var.set("Error de conexión")
                messagebox.showerror("Error", "No se pudo conectar al canal")
    
    def detener_bot(self):
        if messagebox.askyesno("Confirmar", "¿Detener el bot?"):
            detener_bot()
            self.status_var.set("Desconectado")
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
            self.canal_entry.config(state="normal")
            messagebox.showinfo("Información", "Bot detenido")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotGUI(root)
    root.mainloop()
