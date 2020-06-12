import time
import keyboard
import websocket


# Preferences
path = 'ws://localhost:50000/'
IS_DEBUG_MODE = False


keyboard.write('The quick brown fox jumps over the lazy dog.')

if IS_DEBUG_MODE:
    websocket.enableTrace(True)

ws = websocket.WebSocket()
ws.connect(path)
ws.send("ready")


while ws.connected:
    message = ws.recv()
    if message == 'next':
        keyboard.send('right')
        print("next")
    if message == 'prev':
        keyboard.send('left')
        print("prev")

print("Websocket disconnected!")
ws.close()
