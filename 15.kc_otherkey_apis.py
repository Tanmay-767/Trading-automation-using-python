# -*- coding: utf-8 -*-
"""
Zerodha Kite Connect Intro

@author: tanmayakumarsahoo
"""
from kiteconnect import KiteConnect
import os


cwd = os.chdir("address of this txt file ,i.e api_key.txt")

#generate trading session
access_token = open("access_token.txt",'r').read()
key_secret = open("api_key.txt",'r').read().split()
#key_secret[0] = Api_key
#key_secret[1] = Api_secret
#key_secret[2] = user id
#key_secret[3] = password
#key_secret[4] = pin
kite = KiteConnect(api_key=key_secret[0])
kite.set_access_token(access_token)


# Fetch quote details(details about an instument(like volume , last traded price, ohlc))
quote = kite.quote("NSE:INFY")

# Fetch last trading price of an instrument
ltp = kite.ltp("NSE:INFY")

# Fetch all the order details(like order id,order quantity etc)#it will give all the orders placed in a given period
orders = kite.orders()

# Fetch position details
positions = kite.positions()

# Fetch holding details(current holdings in your account)
holdings = kite.holdings()
