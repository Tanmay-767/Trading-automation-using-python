# -*- coding: utf-8 -*-
"""
Zerodha kiteconnect automated authentication

@author: tanmayakumarsahoo
"""
#Code for the generation of request token and store it in the .txt file(in the same folder that of the web driver) 

#step 1.1: First create the request token

from kiteconnect import KiteConnect
from selenium import webdriver
import time
import os

#step 1.2:create a text file(e.g api_key.txt) and (keep API key,api_secret,uderid,password,pin line by line)
cwd = os.chdir("address of this txt file ,i.e api_key.txt")
#keep the api_key.txt and chromedriver in one folder

#step 1.3:create a Autologin function
def autologin():
    token_path = "api_key.txt"
    key_secret = open(token_path,'r').read().split()
    #key_secret[0] = Api_key
    #key_secret[1] = Api_secret
    #key_secret[2] = user id
    #key_secret[3] = password
    #key_secret[4] = pin
    kite = KiteConnect(api_key=key_secret[0])
    service = webdriver.chrome.service.Service('address of the chromedriver./chromedriver')
    #to start the web driver
    service.start()
    
    #you can use various options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    #I dont want the browser to pop out ,so headless option
    options = options.to_capabilities()# for the agreegation of all the options
    driver = webdriver.Remote(service.service_url, options)
    driver.get(kite.login_url())
    driver.implicitly_wait(10)
    
    #giving username and password path 
    username = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input')
    password = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/input')
    
    #enter to the login page(automating the process of username and password
    username.send_keys(key_secret[2])
    password.send_keys(key_secret[3])
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[4]/button').click()
    
    #go to next page for the PIN
    pin = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/div/input')
    pin.send_keys(key_secret[4])
    
    #enter to the login page
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[3]/button').click()
    time.sleep(10)#it will take some time for the rendering of the page , thus provide a suitable sleeptime
    request_token=driver.current_url.split('=')[1].split('&action')[0]#the request token will be generated between the '=' and       '&action'
    
    #generation of the request token
    with open('request_token.txt', 'w') as the_file:
        the_file.write(request_token)
    driver.quit()

    #the request token will be stored as the .txt file in the same folder(containing the chromedriver and api_key.txt)


#generating and storing access token - valid till 6 am the next day

#Step 2: Create a access token
#as soon as we get the request token we should create the access token

autologin()
request_token = open("request_token.txt",'r').read()
key_secret = open("api_key.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])#create a kite session passing the api key
data = kite.generate_session(request_token, api_secret=key_secret[1])#authenticate it by passing the request_token
#here data is the dictionary, drom this data extract access_token and store it in .txt file

with open('access_token.txt', 'w') as file:
        file.write(data["access_token"])
        
#so, by the end of program both access_token and request_token will be generated as .txt file.        
