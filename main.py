from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 100
PROMISED_UP = 10

TWITTER_EMAIL = "**********************"
TWITTER_PASSWORD = "**************"
TWITTER_NUMBER = "**********"


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)

        self.down = 0
        self.up = 0
        # self.driver.quit()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(5)
        go = self.driver.find_element(By.CLASS_NAME, "start-text")
        go.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                             '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                           '3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(20)
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        time.sleep(5)
        phone = self.driver.find_element(By.NAME, "text")
        phone.send_keys(TWITTER_NUMBER)
        phone.send_keys(Keys.ENTER)

        time.sleep(5)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(20)
        message = f"Test tweet for DAY 51 of #100DaysofPython Twitter bot: Hwy Internet Provider!\nWhy is my internet speed {self.down} download and {self.up} uplaod when i pay\nwhen i pay for {PROMISED_DOWN} download and {PROMISED_UP} upload"
        compose = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        compose.send_keys(message)
        compose.send_keys(Keys.CONTROL+Keys.ENTER)




bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
