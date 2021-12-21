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


import unittest
from newapp3 import Ui_MainWindow
import pandas as pd
import xlsxwriter

class testcase(unittest.TestCase):

    def testcheck_day(self):
        result1 = Ui_MainWindow.check_day(self)
        act1 = '2021-04-29'
        self.assertEqual(str(result1),act1)

    def testcleantext(self):
        word = 'covid'
        text = 'today covid is more infected in thailand'
        result2 = Ui_MainWindow.cleantext(self,word,text)
        act2 = 'infected,thailand'
        self.assertEqual(result2,act2)

    def testtokenize(self):
        wordtoken = 'infected,thailand'
        result3 = Ui_MainWindow.tokenize(self,wordtoken)
        act3 = ['infected','thailand']
        self.assertEqual(result3,act3)

    def testcheckdata(self):
        result4 = Ui_MainWindow.checkdata(self,'covid')
        act4 = 'yes'
        self.assertEqual(result4,act4)

    def testsearch_stock(self):
        result5 = Ui_MainWindow.search_stock(self,'SCB.BK','2021-03-19','2021-04-19')
        act5 = None
        self.assertEqual(result5,act5)

    def testsearch_web(self):
        result6 = Ui_MainWindow.search_web(self,'test unittest','https://www.thairath.co.th/news','https://www.thairath.co.th')
        act6 = None
        self.assertEqual(result6,act6)

    def testcrawler_tw(self):      
        word = 'covid'
        sinceday = '2021-04-27'
        untilday = '2021-04-29' # วันที่ 28 แต่การ crawler ต้องบวก until เพิ่ม 1 วัน
        result7 = len(Ui_MainWindow.crawler_tw(self, word, sinceday, untilday))
        act7 = len(pd.read_excel('G:/vscodework/programsearch/twitter file/new_'+word+'.xlsx'))
        self.assertEqual(result7, act7)

    def testdaytwitt(self):
        word = 'covid'
        datafile = pd.read_excel('G:/vscodework/programsearch/twitter file/new_'+word+'.xlsx')
        result8 = Ui_MainWindow.daytwitt(self,datafile)
        self.assertIsNotNone(result8)
    
    def testanalyze_sentiment(self):
        word = 'covid'
        dayt = '2021-04-28'
        datafilet = pd.read_excel('G:/vscodework/programsearch/twitter file/new_'+word+'.xlsx')
        result9 = Ui_MainWindow.analyze_sentiment(self,dayt,dayt,datafilet)
        self.assertIsNotNone(result9)


if __name__ == '__main__':
    unittest.main()
    