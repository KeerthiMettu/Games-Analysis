# -*- coding: utf-8 -*-
"""PS display apps.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A-wSsmSeorm1iRPy1QdXvrEZjzjhwR2n
"""

pip install google-play-scraper

import requests
from bs4 import BeautifulSoup

import pandas as pd

from google_play_scraper import app

action_url='https://play.google.com/store/apps/category/GAME_TRIVIA'

# 'https://play.google.com/store/apps/category/GAME_STRATEGY'
# 'https://play.google.com/store/apps/category/GAME_SPORTS'
# 'https://play.google.com/store/apps/category/GAME_SIMULATION'
# 'https://play.google.com/store/apps/category/GAME_ROLE_PLAYING'
# 'https://play.google.com/store/apps/category/GAME_RACING'
# 'https://play.google.com/store/apps/category/GAME_PUZZLE'
# 'https://play.google.com/store/apps/category/GAME_MUSIC'
# 'https://play.google.com/store/apps/category/GAME_EDUCATIONAL'
# 'https://play.google.com/store/apps/category/GAME_CASUAL'
# 'https://play.google.com/store/apps/category/GAME_CASINO'
# 'https://play.google.com/store/apps/category/GAME_CARD'
# 'https://play.google.com/store/apps/category/GAME_BOARD'
# 'https://play.google.com/store/apps/category/GAME_ARCADE'
# 'https://play.google.com/store/apps/category/GAME_ADVENTURE'
# 'https://play.google.com/store/apps/category/GAME_ACTION?hl=en-GB'

app_page = requests.get(action_url)

# Provide the app page content to BeautifulSoup parser
soup = BeautifulSoup(app_page.content, 'html.parser')

tag='div'
attribute='b8cIId ReQCgd Q9MA7b'
gameurls = soup.findAll(tag, class_=attribute)

# for i in gameurls:
#     print(i)

# to get only game names
# for x in gameurls:
#    print(x.text)

print(type(gameurls))
print(len(gameurls))

rec=[]

Id = []

print(type(rec))
print(type(Id))

for x in gameurls:
   aa=x.findAll('a')
   rec.append(str(aa))
  #  print(rec)

print(type(aa))
print(type(rec))

for href in rec:
    ele=href.split("id=")
    subele=ele[1].split("\"><div")
    Id.append(subele[0])
    # subele[0]
    #print(Id)

print(Id[0:5])

for game in Id[0:5]:
    t=app(game)
    print(t,"\n")
    print(type(t),type(t['title']))
    print(t['title'])

features=[' title ' ,' appId ' ,' url ' ,' description ' ,' summary ' ,' installs ' ,
' minInstalls ' ,' score ' ,' ratings ' ,' reviews ' ,' price ' ,' free ' ,' currency ' ,
' offersIAP ' ,' size ' ,' androidVersion ' ,' developer ' ,' developerId ' ,' developerEmail ' ,
' developerWebsite ' ,' privacyPolicy ' ,' developerInternalID ' ,' genre ' ,' genreId ' ,
' icon ' ,' headerImage ' ,
# ' screenshots ' ,' video ' ,' videoImage ' ,
' contentRating ' ,
' contentRatingDescription ' ,' adSupported ' ,' containsAds ' ,' released ' ,' updated ' ,
' version ' ,' recentChanges ' ,' comments '
]

records=pd.DataFrame()
print(records)

def add_details_as_row(game_result):
    row=[]
    row.append(game_result['title'])
    row.append(game_result['appId'])
    row.append(game_result['url'])
    row.append(game_result['description'])
    row.append(game_result['summary'])
    row.append(game_result['installs'])
    row.append(game_result['minInstalls'])
    row.append(game_result['score'])
    row.append(game_result['ratings'])
    row.append(game_result['reviews'])
    row.append(game_result['price'])
    row.append(game_result['free'])
    row.append(game_result['currency'])
    row.append(game_result['offersIAP'])
    row.append(game_result['size'])
    row.append(game_result['androidVersion'])
    row.append(game_result['developer'])
    row.append(game_result['developerId'])
    row.append(game_result['developerEmail'])
    row.append(game_result['developerWebsite'])
    row.append(game_result['privacyPolicy'])
    row.append(game_result['developerInternalID'])
    row.append(game_result['genre'])
    row.append(game_result['genreId'])
    row.append(game_result['icon'])
    row.append(game_result['headerImage'])
    row.append(game_result['contentRating'])
    row.append(game_result['contentRatingDescription'])
    row.append(game_result['adSupported'])
    row.append(game_result['containsAds'])
    row.append(game_result['released'])
    row.append(game_result['updated'])
    row.append(game_result['version'])
    row.append(game_result['recentChanges'])
    row.append(game_result['comments'])
    return row;

for game in Id:
    each_game_result=app (game)
    eachrow=add_details_as_row(each_game_result)
    #print(eachrow)
    records = records.append([eachrow])

# appending rows 
# for key,value in game_result.items(): 
#         row.append(value)

print(records)

records.to_csv('Gaming.csv',index = False, header=True)

new_record=pd.read_csv('/content/Gaming.csv',sep=',')
print(new_record)

#/content/Gaming.csv

