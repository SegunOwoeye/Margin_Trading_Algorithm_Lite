#!/usr/bin/python3.6.5

import websocket
import rel

from datetime import datetime
from os import path
import sqlite3
from time import time
from json import loads
from functools import partial

"""
1. CODE FOR GETTING LIVE MARKET DATA
"""
def on_message(ws, message, exchange_pair, exchange_name, interval):
    raw_data_string = message
    json_data_string = raw_data_string.replace("++Rcv raw:", "").strip()
    data_list = loads(json_data_string)
    
    ohlcv_list = data_list['k']
    time = data_list["E"] 
    open_price = float(ohlcv_list['o'])
    close_price = float(ohlcv_list['c'])
    high_price = float(ohlcv_list['h'])
    low_price = float(ohlcv_list['l'])
    volume_traded = float(ohlcv_list['v'])
    
    



"""
2. CODE FOR CONNECTING TO WEBSOCKET 
"""
def on_error(ws, error):
    print(error)
def on_close(ws, close_status_code, close_msg):
    print("### closed ###")
def on_open(ws,interval):
    print(f"Opened connection: Live Data for Interval={interval}")

"""
4. RUNS THE PROGRAM
"""
def run(exchange_pair, exchange_name, interval):
    ws = websocket.WebSocketApp(f"wss://stream.binance.com:9443/ws/{exchange_pair.lower()}@kline_{interval}",
                              on_open=partial(on_open, interval=interval),
                              on_message=partial(on_message, exchange_pair=exchange_pair, exchange_name=exchange_name, interval=interval),
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()






#starts the program
#run("BTCUSDT","Binance", "5m")

#check("BTCUSDT", "Binance", "5m")
