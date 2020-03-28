import requests
import time
import os
# import smtplib

TICKER_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'

# Get the location for our price alerts config.
CONFIG = os.path.join(os.path.dirname(os.path.realpath(__file__)),
    'price-alert-rules.txt',)

# The name of our IFTTT web request event.
IFTTT_EVENT = 'btc_price_current'

# Our IFTTT secret key. Protect this if you don't want attackers to send
# you notifications.
IFTTT_KEY = 'qZ5DgJ5QYWEgPNvYPhILk'

# The endpoint we'll use to send trigger price alert notifications.
IFTTT_URL = (
    'https://maker.ifttt.com/use/qZ5DgJ5QYWEgPNvYPhILk'
    .format(IFTTT_EVENT, IFTTT_KEY)
)

# def sendTelegramNotification():
#   requests.post(IFTTT_URL)

# def fetchBitcoinPrice():
#   while True:
#     url = "https://api.coindesk.com/v1/bpi/currentprice.json"
#     response = requests.get(
#       url, 
#       headers={"Accept": "application/json"},
#     )
#     data = response.json()
#     bpi = data['bpi']
#     USD = bpi['USD']
#     bitcoin_rate = int(USD['rate_float'])
#     if bitcoin_rate < int(alert_amount):
#       sendTelegramNotification()
#       print('Will check again in every second. Ctrl + C to quit.')
      
#       time.sleep(3)
#     else:
#       time.sleep(1)
#       print('Price is ' + str(bitcoin_rate) + '. Will check again in 3 seconds. Ctrl + C to quit.')



alert_amount = input('Alert if Bitcoin drops below: ')
# def Telegram_Notification():
#   requests.post(IFTTT_URL)

while True:
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(
    url, 
    headers={"Accept": "application/json"},
  )
    data = response.json()
    bpi = data['bpi']
    USD = bpi['USD']
    bitcoin_rate = int(USD['rate_float'])
    if bitcoin_rate < int(alert_amount):
      # Telegram_Notification()
      print('Price is ' + str(bitcoin_rate) + '.Will check again every second. Ctrl + C to quit.')
    
      time.sleep(1)
    else:
      time.sleep(3)
    print('Price is ' + str(bitcoin_rate) + '. Will check every three second. Ctrl + C to quit.')
# if __name__ == "__main__":
#     Telegram_Notification()