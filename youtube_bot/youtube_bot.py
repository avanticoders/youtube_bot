from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

from youtube_bot.constants import PATH, BINARY_PATH
from youtube_bot.constants import WEBSITE_URL as url


class YoutubeBot(webdriver.Firefox):
    def __init__(self, driver_path=PATH, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown

        service = Service(PATH)
        option = webdriver.FirefoxOptions()
        option.binary_location = BINARY_PATH

        super(YoutubeBot, self).__init__(service=service, options=option)
        self.implicitly_wait(10)

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

    def main_page(self):
        self.get(url)
