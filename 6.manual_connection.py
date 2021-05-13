# -*- coding: utf-8 -*-
"""
Connecting to KiteConnect API

@author: tanmayakumarsahoo
"""

#Establishing Connection and Creating a Trading Object
from kiteconnect import KiteConnect
import pandas as pd

api_key = "Your API Key"
api_secret = "Your API Secret"
kite = KiteConnect(api_key=api_key)
print(kite.login_url()) #use this url to manually login and authorize yourself
#login url will be there in the output
#login into zerodha by entering url and then the password and PIN


#get the request token from the url in the chrome(or safari)
#generate trading session
request_token = "Your Request Token" #Extract request token from the redirect url obtained after you authorize yourself by loggin in
data = kite.generate_session(request_token, api_secret=api_secret)
#here data is a dictionary that contains(access_token,api_key,avatar_url,brocker,
#email,exchange,login_time,meta,order_types,products,public_token,refresh_token,
#user_id,user_name,user_shortname)

#create kite trading object
kite.set_access_token(data["access_token"])


#get dump of all NSE instruments
instrument_dump = kite.instruments("NSE")
instrument_df = pd.DataFrame(instrument_dump)
instrument_df.to_csv("instruments.csv",index=False)