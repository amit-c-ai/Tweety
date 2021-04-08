import os
from twitterbot import Twitterbot
import twitterbot as tb
import secrets, sys
import xlrd
import xlwt
from xlutils.copy import copy
  
loc = 'data.xls'
print(loc)
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)
w = copy(wb)
tweetbody = []
email = []
password = []
for i in range(sheet.nrows):
    if(i!=0):
        email.append(sheet.cell_value(i, 1))

for i in range(sheet.nrows):
    if(i!=0):
        password.append(sheet.cell_value(i, 2))

for i in range(sheet.nrows):
    if(i!=0):
        tweetbody.append(sheet.cell_value(i, 3))

print("email: ", email[0], "password: ", password[0], "  ", tweetbody)

if __name__ == "__main__":
    try:
        bot = Twitterbot(email[0], password[0])
        bot.login()
        for i in range(len(tweetbody)):
            bot.post_tweets(tweetbody[i])
        bot.logout()
    except Exception as e:
        bot.logout()
        print(e)

