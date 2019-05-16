import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_gmusic_favs(uname, pw):
    browser = webdriver.Chrome('chromedriver_linux64/chromedriver')
    browser.get('https://play.google.com/music/')
    browser.find_element_by_css_selector(
        '#music-content > div > div.image-enticement.bgcolor-white.full-enticement > div > div.button-holder > '
        'paper-button').click()
    browser.find_element_by_css_selector('#identifierId').send_keys(uname)
    browser.find_element_by_css_selector('#identifierNext > content > span').click()
    time.sleep(2)
    browser.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys(pw)
    browser.find_element_by_css_selector('#passwordNext > content > span').click()

    delay = 5
    try:
        myElem = WebDriverWait(browser, delay)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, '#quickNavContainer > gpm-quick-nav > div.items.main.style-scope.gpm-quick-nav > '
                                                                    'gpm-quick-nav-item:nth-child(2) > a')))

    except TimeoutException:
        print("Loading took too much time!")
    browser.get('https://play.google.com/music/listen#/ap/auto-playlist-thumbs-up')

    input()


f = open('cred', 'r')

user, pw = f.read().split('\n')

get_gmusic_favs(user, pw)
