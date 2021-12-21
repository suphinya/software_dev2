import time
import tweepy
import pandas as pd
import xlsxwriter
import emoji
import re
import matplotlib
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords
from spacy.lang.en.stop_words import STOP_WORDS
from datetime import date,timedelta,datetime
from textblob import TextBlob
from pandas_datareader import data
import mplfinance as fplt
import requests 
from bs4 import BeautifulSoup
import os
import threading


# search web ในปัจจุบัน โดยให้วันที่เป็นวันที่ search
def searchnews_today(name,url,linknews):

    frame = pd.DataFrame(columns = ["date","text","link"])

    nameweb = name
    print(nameweb)

    weburl = url
    print('web : ' + weburl)

    datenow = date.today()

    webdata = requests.get(weburl)
    print(webdata)

    soup = BeautifulSoup(webdata.text,'html.parser')
    listpath = []    
    news = soup.find_all('a',href=True)
    for i in news:
        headnews = i.getText()
        headnews = re.sub(r'[\!\.\?\,\:\n\t\"\(\)\[\]]', '',headnews, flags=re.MULTILINE)
        if headnews == '' :
            headnews = None
        webnews = i['href']
        checkref = re.findall(r'http',webnews)
        checkref2 = re.findall(r'www.',webnews)
        print('before : ' + webnews)
        if checkref == [] and checkref2 == [] :
            if len(webnews) >= 1 :
                if webnews[0] != '/':
                    webnews = '/'+webnews
            path = linknews + webnews
        else :
            path = webnews
        
        if path[0] == '/' and path[1] == '/' and path[2] == 'w':
            path = re.sub(r'//','https://',path, flags=re.MULTILINE)
        elif path[0] == '/' and path[1] == '/' and path[2] == 'h':
            path = re.sub(r'//','',path, flags=re.MULTILINE)

        print(path)

        checkpathfr = re.findall(linknews,path)

        if (path)[-1] not in [':',';',')'] and checkpathfr != [] and path[0] in ['h','w'] and len(listpath) <= 200 :
            listpath += path
            search2 = requests.get(path)
            print(search2)
            soup2 = BeautifulSoup(search2.text,'html.parser')
            news2 = soup2.find_all('a',href=True)
        
            for j in news2:
                headnews2 = j.getText()
                headnews2 = re.sub(r'[\!\.\?\,\:\n\t\"\(\)\[\]]', '',headnews2, flags=re.MULTILINE)
                if headnews2 == '' :
                    headnews2 = None

                webnews2 = j['href']
                seccheckref = re.findall(r'https://',webnews2)
                seccheckref2 = re.findall(r'www.',webnews2)
                if seccheckref == [] and seccheckref2 == [] :
                    path2 = linknews + webnews2
                else :
                    path2 = webnews2
                new_column = pd.Series([datenow,headnews2,path2], index=frame.columns)   
                frame = frame.append(new_column,ignore_index=True)

        new_column = pd.Series([datenow,headnews,path], index=frame.columns)   
        frame = frame.append(new_column,ignore_index=True)
    frame = frame.dropna() 
    frame = frame.drop_duplicates(subset='text',keep='first') 
    if os.path.isfile('G:/vscodework/programsearch/web file/'+nameweb+'/'+str(datenow)+'.xlsx') == True :
        concatdataweb(nameweb,frame)
    else :
        frame.to_excel('G:/vscodework/programsearch/web file/'+nameweb+'/'+str(datenow)+'.xlsx',index=False)



def concatdataweb(nameweb,dataframe):
    datenow = date.today()
    if os.path.isfile('G:/vscodework/programsearch/web file/'+nameweb+'/'+str(datenow)+'.xlsx') == True :
        olddata = pd.read_excel('G:/vscodework/programsearch/web file/'+nameweb+'/'+str(datenow)+'.xlsx')
        newdata = dataframe  
        now_data = pd.concat([olddata,newdata] , axis=0)
        now_data = now_data.drop_duplicates(subset='text',keep='first')
        now_data = now_data.sort_values(by=['date'],ascending=False)
        now_data.to_excel('G:/vscodework/programsearch/web file/'+nameweb+'/'+str(datenow)+'.xlsx',sheet_name ='data',index = False)

nameweb = []
with open('G:/vscodework/programsearch/web file/nameweb.txt','r',encoding='utf-8') as f :
    for line in f :
        nameweb.append(line.rstrip())
web =   []
with open('G:/vscodework/programsearch/web file/web.txt','r',encoding='utf-8') as f :
    for line in f :
        web.append(line.rstrip())
forlink = []
with open('G:/vscodework/programsearch/web file/link web.txt','r',encoding='utf-8') as f :
    for line in f :
        forlink.append(line.rstrip())



#searchnews_today(nameweb[0],web[0],forlink[0])

'''for i in range(len(nameweb)):
    #os.mkdir('G:/vscodework/programsearch/test wewb 555/'+nameweb[i+65])
    searchnews_today(nameweb[i],web[i],forlink[i])'''
    
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------

