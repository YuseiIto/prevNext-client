import time
# import keyboard
# import websocket
import sys


# Preferences
path = 'ws://server.prevnext.yuseiito.com/'
IS_DEBUG_MODE = False

try:
    spaceId = str(sys.argv[1])
except IndexError as e:
    print(
        "\033[31mError: The space id is not provided. Please run command like `prevNext 1234`\033[m")
    sys.exit()


if spaceId == "-v":
    print("0.1.0")
    sys.exit()
else:
    print("\033[Space ID: " + spaceId + "\033[m")


print("\033[32m\033[1m prevNext \033[m")
print("\033[32m Remote presentation application. \033[m")
print("\033[32mCreated by Yusei Ito\033[m")
print("\033[32m- - - - - - - - - - \033[m")
print("\033[32mTarget server: " + path + "\033[m")

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
