#https://pypi.org/project/websocket_client/
import websocket,json,os
import cursor
cursor.hide()


sandbox_api = 'sandbox_c2sjvm2ad3ic1qis2cr0'
apikey = 'c2sjvm2ad3ic1qis2cqg'
key = apikey
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
    #ws.send('{"type":"subscribe","symbol":"AAPL"}')
    #ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:ETHUSDT"}')
    #ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')


if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={key}",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
