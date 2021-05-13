# -*- coding: utf-8 -*-
"""
Zerodha Kite Connect - Streaming Data

@author: tanmayakumarsahoo
"""
#Steaming Tick level data

from kiteconnect import KiteConnect
from kiteconnect import KiteTicker#KiteTicker module is for streaming purpose  
import pandas as pd
import os

cwd = os.chdir("address of this txt file ,i.e api_key.txt")


#generate trading session
access_token = open("access_token.txt",'r').read()
key_secret = open("api_key.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])
kite.set_access_token(access_token)

#get dump of all NSE instruments
instrument_dump = kite.instruments("NSE")
instrument_df = pd.DataFrame(instrument_dump)
#instrument_df contains all the NSE instriuments which are currently trading


#to get the token_list(as output) from symbol_list from instrument_df
def tokenLookup(instrument_df,symbol_list):
    """Looks up instrument token for a given script from instrument dump"""
    token_list = []
    for symbol in symbol_list:
        token_list.append(int(instrument_df[instrument_df.tradingsymbol==symbol].instrument_token.values[0]))
    return token_list

#all the token are to be in integer because kite
#####################update ticker list######################################
tickers = ["INFY", "ACC", "ICICIBANK"]#Here I will give a list of tickers and the function(tokenLookup(instrument_df,symbol_list)) will provide me the list of tokens(token_list)
#############################################################################

#create KiteTicker object
#KiteTicker needs our api_secret and access_token
kws = KiteTicker(key_secret[0],kite.access_token)
#creating kiteticker object(kws)
#later this object(kws) will able to stream data for us
tokens = tokenLookup(instrument_df,tickers)#it will create a list of the corresponding tokens


#Web socket connection uses
def on_ticks(ws,ticks):
    # Callback to receive ticks.
    #logging.debug("Ticks: {}".format(ticks))
    print(ticks)

def on_connect(ws,response):
    # Callback on successful connect.
    # on_connect will Subscribe to a list of instrument_tokens (like RELIANCE and ACC here).
    #because u can't steam tickers unless u suscribe to them
    #logging.debug("on connect: {}".format(response))
    ws.subscribe(tokens)
    ws.set_mode(ws.MODE_FULL,tokens) # Set all token tick in `full` mode.
    #ws.set_mode(ws.MODE_FULL,[tokens[0]])  # Set one token tick in `full` mode.(here one token in the list [tokens[0]]= "INFY")
 

kws.on_ticks=on_ticks
kws.on_connect=on_connect
kws.connect()

#Once executed it will stream , it will be difficult to stop it( cannot be stoped using time module)
#ways to stop it ( sys.exit()  i,e exit from the system) or you can close the console 
