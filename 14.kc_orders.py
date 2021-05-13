# -*- coding: utf-8 -*-
"""
Zerodha Kite Connect Intro - Placing orders

@author: tanmayakumarsahoo
"""
from kiteconnect import KiteConnect
import logging
import os

#Create the kite object and generate the sessions
cwd = os.chdir("D:\\Udemy\\Zerodha KiteConnect API\\1_account_authorization")

#generate trading session
access_token = open("access_token.txt",'r').read()
key_secret = open("api_key.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])
kite.set_access_token(access_token)

#function to create the market order
def placeMarketOrder(symbol,buy_sell,quantity):    
    # Place an intraday market order on NSE
    if buy_sell == "buy":
        t_type=kite.TRANSACTION_TYPE_BUY
    elif buy_sell == "sell":
        t_type=kite.TRANSACTION_TYPE_SELL
    kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NSE,
                    transaction_type=t_type,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_MARKET,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR)
    
#for example(all exchanges = NSE orders )   
#placeMarketOrder("ACC","buy",100)  
#placeMarketOrder("RELIANCE","sell",100) 
  
    
#function to create the bracket order    
def placeBracketOrder(symbol,buy_sell,quantity,atr,price): #price = trade entry price
    #this price may be above or below the market value(the price  at which you r willing to buy
    # Place an intraday market order on NSE
    if buy_sell == "buy":
        t_type=kite.TRANSACTION_TYPE_BUY
    elif buy_sell == "sell":
        t_type=kite.TRANSACTION_TYPE_SELL
    kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NSE,
                    transaction_type=t_type,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_LIMIT,
                    price=price, #BO has to be a limit order, set a low price threshold or stop-loss
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_BO,
                    squareoff=int(6*atr), 
                    stoploss=int(3*atr), 
                    trailing_stoploss=2)

#for example(all exchanges = NSE orders)
#placeBracketOrder("ACC","buy",100,10,price)
#suppose atr=10 for RELIANCE(let :spot price= 2000) 
#then, squareoff(2000+6*atr = 2060) and stoploss(2000-3*atr = 1970)     
#for example(all exchanges = NSE orders )   
#placeMarketOrder("ACC","buy",100)  
#placeMarketOrder("RELIANCE","sell",100) 





#tradingsymbol	Tradingsymbol of the instrument
#exchange	Name of the exchange
#transaction_type	BUY or SELL
#order_type	Order type (MARKET, LIMIT etc.)
#quantity	Quantity to transact
#Product	Margin product to use for the order (margins are blocked based on this) ?
#price	The min or max price to execute the order at (for LIMIT orders)
#trigger_price	The price at which an order should be triggered (SL, SL-M)
#disclosed_quantity	Quantity to disclose publicly (for equity trades)
#validity	Order validity
#tag	An optional tag to apply to an order to identify it (alphanumeric, max 20 chars)
    