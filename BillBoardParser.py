from bs4 import BeautifulSoup
from time import localtime, strftime
import os
import json
import datetime
import urllib.request
'''
// 최근 10주 동안의 데이터가 필요할 시
ParsingDataListbyDate=[]
for i in range(0,10):
    time = datetime.datetime.now() - datetime.timedelta(days = i*7)
    date = time.strftime("%Y-%m-%d")
    url="http://www.billboard.com/charts/hot-100/{0}".format(date)
    BillBoardData=urllib.request.urlopen(url).read().decode("utf8")
    soup = BeautifulSoup(BillBoardData, 'html.parser')
    ParsingDataListbyRank=[]
    index = 1
'''
time = datetime.datetime.now() - datetime.timedelta(days = 0*7)
date = time.strftime("%Y-%m-%d")
url="http://www.billboard.com/charts/hot-100/{0}".format(date)
BillBoardData=urllib.request.urlopen(url).read().decode("utf8")
soup = BeautifulSoup(BillBoardData, 'html.parser')
ParsingDataListbyRank=[]
index = 1
for s in range(0,100):
        singer = soup.find(
        "article",{"class":"chart-row chart-row--{0} js-chart-row".format(index)}).find_all(
        "span", {"class":"chart-row__artist"})
        song = soup.find(
        "article",{"class":"chart-row chart-row--{0} js-chart-row".format(index)}).find_all(
        "h2", {"class":"chart-row__song"})
        rank = soup.find(
        "article",{"class":"chart-row chart-row--{0} js-chart-row".format(index)}).find_all(
        "span", {"class":"chart-row__current-week"})
        DataDitionary={}
        try:
            DataDitionary['artist']=singer[0].get_text(" ", strip=True)
        except:
            singer = soup.find("article",class_="chart-row chart-row--{0} js-chart-row".format(index)).find_all("a", {"class":"chart-row__artist"})
            DataDitionary['artist']=singer[0].get_text(" ", strip=True)
        
        DataDitionary['song'] = song[0].get_text(" ", strip=True)
        DataDitionary['rank'] = rank[0].get_text(" ", strip=True)
        DataDitionary['date'] = date
        ParsingDataListbyRank.append(DataDitionary)
        print("{0} : {1}".format(index,ParsingDataListbyRank[s]))  # Look A Parsed Aata
        index=index+1
jsonData = json.dumps(ParsingDataListbyRank) # 데이터를 json 형식으로 변환한다.
#print(jsonData)