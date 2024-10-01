#https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md
import websocket,json,os
import cursor
cursor.hide()

def on_message(ws, message):
    """ convert string to dictionary"""
    message = json.loads(message)
    clear = lambda: os.system('cls')
    clear()
    print(message)
    print(" ",message['data'][0]['p'],flush=True,end="\r")


def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"method":"SUBSCRIBE","params":["btcusdt@aggTrade",""]}')


if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(f"wss://stream.binance.com:9443/ws/bnbbtcopen@depth",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
#https://www.youtube.com/watch?v=d-2GoqQbagI