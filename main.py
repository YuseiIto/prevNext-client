import time
import keyboard
import websocket

# Preferences
path = 'ws://localhost:50000/'
IS_DEBUG_MODE = False


print("Remote-presentation-support")
print("Created by Yusei Ito")
print("- - - - - - - - - - ")
print("Target server: " + path)

if IS_DEBUG_MODE:
    websocket.enableTrace(True)

ws = websocket.WebSocket()
ws.connect(path)
ws.send("ready")

print("\033[32mConnection established! Ready.\033[0m")

# Main outine. continues fowever if conneced
while ws.connected:
    message = ws.recv()
    if message == 'next':
        keyboard.send('right')
        print("next")
    if message == 'prev':
        keyboard.send('left')
        print("prev")

print("\033[92mWebsocket disconnected!\033[0m")
ws.close()
