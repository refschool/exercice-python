import yfinance as yf
import  textwrap


msft = yf.Ticker("PLTR")
print(msft)


for cle,value in msft.info.items():
    print(cle,value)
#print(textwrap.fill(str(msft.info),width=80))