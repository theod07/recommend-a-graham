import selenium.webdriver as webdriver
import time
import random
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from appscript import app

def get_users(filename):
    '''
    INPUT: file of users, separated by newline
    OUTPUT: list of users
    '''
    with open(filename) as f:
        users = f.readlines()
    users = [name.split('\n')[0] for name in users if not name.startswith('#')]
    return set(users)


def get_page(user, driver, sleeptime=1, down_scrolls=1e6):
    '''
    '''
    url = 'http://instagram.com/' + user
    driver.get(url)
    try:
        driver.find_element_by_link_text('LOAD MORE').click()
    except NoSuchElementException:
        print "Sorry, can't click LOAD MORE for {}".format(user)

    page = driver.page_source

    for i in xrange(down_scrolls):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(sleeptime + random.random())
        if driver.page_source == page:
            break
        page = driver.page_source

    saveas.perform()
    time.sleep(sleeptime)
    app('System Events').keystroke('\r')

if __name__ == '__main__':
    SLEEPTIME = 1
    SAVE_DIR = '/Users/wonder/galvanize/project/recommend-a-graham/data'
    DEBUG = False


    if DEBUG:
        users = ['patricknorton', 'taylorswift']
    else:
        users = get_users('../data/most_popular.txt')

    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", SAVE_DIR)
    driver = webdriver.Firefox(firefox_profile=profile)

    saveas = ActionChains(driver).key_down(Keys.COMMAND).send_keys('s').key_up(Keys.COMMAND)

    rawPages = os.listdir('data/')
    for user in users:
        if any("@" + user in s for s in rawPages):
            continue
        get_page(user, driver, sleeptime=SLEEPTIME)
        with open('logs/log_scrape_users.txt', 'ab') as f:
            f.write('{} saved page for {}'.format(time.strftime('%Y%m%d.%H:%M:%s'), user))

    driver.close()
