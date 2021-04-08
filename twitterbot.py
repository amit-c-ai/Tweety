from selenium import webdriver
from selenium import common
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

'''if you are using on linux use below line also'''
# from pyvirtualdisplay import Display
import time, os
  
class Twitterbot:
  
    def __init__(self, email, password, keyword=''):
  
        self.email = email
        self.password = password
        self.hashtag = keyword
        self.is_logged_in=False
        chrome_options = Options()
        self.bot = webdriver.Chrome(
            executable_path = os.path.join(os.getcwd(), 'chromedriver'),
            options = chrome_options
        )
  
    def login(self):
  
        bot = self.bot
        bot.get('https://twitter.com/LOGIN')
        time.sleep(3)
  
        email = bot.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
        )
        password = bot.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
        )
  

        email.send_keys(self.email)

        password.send_keys(self.password)

        password.send_keys(Keys.RETURN)

        self.is_logged_in = True
  
        time.sleep(5)


    def logout(self):

        if not self.is_logged_in:
            return 

        bot = self.bot
        bot.get('https://twitter.com/home')
        time.sleep(1)
        
        bot.find_element_by_xpath("//div[@data-testid='SideNav_AccountSwitcher_Button']").click()
            
        time.sleep(1)

        bot.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div[1]/div/span').click()

        time.sleep(3)

        bot.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/span/span').click()

        time.sleep(1)

    def search(self, hashtag=''):
        if not self.is_logged_in:
            raise Exception("You must log in first!")

        bot = self.bot

        try:
            searchbox = bot.find_element_by_xpath("//input[@data-testid='SearchBox_Search_Input']")
        except common.exceptions.NoSuchElementException:
            time.sleep(2)
            searchbox = bot.find_element_by_xpath("//input[@data-testid='SearchBox_Search_Input']")

        searchbox.clear()
        searchbox.send_keys(hashtag)
        searchbox.send_keys(Keys.RETURN)
        time.sleep(5)  


    def like_tweets(self, cycles=10):
        like_buttons=[]
        if not self.is_logged_in:
            raise Exception("You must log in first!") 

        bot = self.bot   
        try:
            like_buttons = bot.find_elements_by_xpath('//div[@data-testid="like"]')
            time.sleep(1)
            for i in range(int(cycles)):
                like_buttons[i].click()
                time.sleep(2)
        except:
            like_buttons.clear()
            time.sleep(2)
            like_buttons = bot.find_elements_by_xpath('//div[@data-testid="like"]')
            time.sleep(1)
            for i in range(int(cycles)):
                like_buttons[i].click()
                time.sleep(2)            

        time.sleep(2)

      
    def post_tweets(self,tweetBody):
        if not self.is_logged_in:
            raise Exception("You must log in first!")

        bot = self.bot  

        try:
            bot.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            bot.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()

        time.sleep(4) 
        body = tweetBody

        try:
            bot.find_element_by_xpath("//div[@role='textbox']").send_keys(body)
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            bot.find_element_by_xpath("//div[@role='textbox']").send_keys(body)

        time.sleep(3)
        bot.find_element_by_xpath("//div[@data-testid='tweetButton']").click()
        time.sleep(5) 










        
        
'''
        try:
            bot.find_element_by_xpath("//div[@data-testid='confirmationSheetConfirm']").click()
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            bot.find_element_by_xpath("//div[@data-testid='confirmationSheetConfirm']").click()

        time.sleep(3)   '''

