import time
import keyboard
import websocket
import sys

# Preferences
path = 'ws://server.nextprev.yuseiito.com/'
IS_DEBUG_MODE = False

spaceId = str(sys.argv[1])

print("Remote-presentation-support")
print("Created by Yusei Ito")
print("- - - - - - - - - - ")
print("Target server: " + path)

if IS_DEBUG_MODE:
    websocket.enableTrace(True)

ws = websocket.WebSocket()


# Main outine. continues fowever if conneced
while True:
    ws.connect(path)
    ws.send('ready#' + spaceId)
    print("\033[32mConnection established! Ready.\033[0m")
    while ws.connected:
        ws.settimeout(20)
        try:
            message = ws.recv()
            if message == 'next':
                keyboard.send('right')
                print("next")
            if message == 'prev':
                keyboard.send('left')
                print("prev")
            if message == 'check':
                ws.send('ready#' + spaceId)
                print("Check")
            message = ''
        except Exception as e:
            message = ''
            if str(e) != 'timed out':
                print(e)
            else:
                print('.')
                ws.send('ready#' + spaceId)
            continue
    print("\033[92mWebsocket disconnected!\033[0m")
ws.close()
