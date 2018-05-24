import requests
from bs4 import BeautifulSoup
import time
import datetime
from random import randint 
import numpy as np
import pandas as pd


query2Google = input("What do you want from Google News?\n")

def QGN(query2Google):
    s = '"'+query2Google+'"' #Keywords for query
    s = s.replace(" ","+")
    date = str(datetime.datetime.now().date()) #timestamp
    filename =query2Google+"_"+date+"_"+'SearchNews.csv' #csv filename
    f = open(filename,"wb")
    url = "http://www.google.co.in/search?q="+s+"&tbm=nws&tbs=qdr:y" # URL for query of news results within one year and sort by date 

    #htmlpage = urllib2.urlopen(url).read()
    time.sleep(randint(0, 2))#waiting 

    htmlpage = requests.get(url)
    print("Status code: "+ str(htmlpage.status_code))
    soup = BeautifulSoup(htmlpage.text,'lxml')

    df = []
    for result_table in soup.findAll("div", {"class": "g"}):
        a_click = result_table.find("a")
        #print ("-----Title----\n" + str(a_click.renderContents()))#Title

        #print ("----URL----\n" + str(a_click.get("href"))) #URL

        #print ("----Brief----\n" + str(result_table.find("div", {"class": "st"}).renderContents()))#Brief

        #print ("Done")
        df=np.append(df,[str(a_click.renderContents()).strip("b'"),str(a_click.get("href")).strip('/url?q='),str(result_table.find("div", {"class": "st"}).renderContents()).strip("b'")])


        df = np.reshape(df,(-1,3))
        df1 = pd.DataFrame(df,columns=['Title','URL','Brief'])
    print("Search Crawl Done!")

    df1.to_csv(filename, index=False,encoding='utf-8')
    f.close()
    return

QGN(query2Google)