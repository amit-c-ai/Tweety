import os
from twitterbot import Twitterbot
import twitterbot as tb
import secrets, sys
import xlrd
import xlwt
from xlutils.copy import copy

loc='data.xls'
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

keywords=[]
email=[]
password=[]
likes=[]

for i in range(sheet.nrows):
    if(i!=0):
        keywords.append(sheet.cell_value(i, 0))

for i in range(sheet.nrows):
    if(i!=0):
        email.append(sheet.cell_value(i, 1))

for i in range(sheet.nrows):
    if(i!=0):
        password.append(sheet.cell_value(i, 2))

for i in range(sheet.nrows):
    if(i!=0):
        likes.append(sheet.cell_value(i, 4))
print(int(email[0]), password[0], "likes : ", likes)

bot = Twitterbot(int(email[0]), password[0])

bot.login()
bot.search(keywords[0])
bot.like_tweets(likes[0])
bot.logout()
