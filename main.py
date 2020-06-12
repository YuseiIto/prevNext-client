import time
import keyboard
import websocket


# Preferences
path = 'ws://localhost:50000/'
IS_DEBUG_MODE = False


keyboard.press_and_release('shift+s, space')
keyboard.write('The quick brown fox jumps over the lazy dog.')

if IS_DEBUG_MODE:
    websocket.enableTrace(True)

ws = websocket.WebSocket()
ws.connect(path)
print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")
print("Receiving...")
result = ws.recv()
print("Received '%s'" % result)
ws.close()

""" 
while True:
    keyboard.send('enter')
    print("Change LIne!")
    time.sleep(0.8) """
