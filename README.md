# Chat Bot con Interfaz Gráfica

Bot de chat para Twitch IRC con interfaz gráfica para configurar el canal de destino.

## Características

- Interfaz gráfica para configurar el canal de destino
- Validación de nombres de canal
- Envío automático de mensajes programados
- Control de inicio/detención del bot

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
python bot.py
```

La aplicación abrirá una ventana donde podrás:

1. **Ingresar el canal de destino**: Escribe el nombre del canal sin el símbolo `#` (ejemplo: `elcrissenpaii`)
2. **Iniciar el bot**: Haz clic en "Iniciar Bot" para comenzar a enviar mensajes
3. **Detener el bot**: Haz clic en "Detener Bot" para parar el envío de mensajes

## Configuración

Antes de usar el bot, asegúrate de configurar:

- `nickname`: Tu nombre de usuario de Twitch
- `token`: Tu token OAuth de Twitch
- `server` y `port`: Configuración del servidor IRC (predeterminado: irc.chat.twitch.tv:6667)
