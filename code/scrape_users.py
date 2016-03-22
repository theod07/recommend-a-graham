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


def get_page(user, driver, sleeptime=1, down_scrolls=int(3e2)):
    '''
    '''
    url = 'http://instagram.com/' + user
    driver.get(url)

    # Page is not available/404
    if 'The link you followed may be broken, or the page may have been removed.' in driver.page_source:
        return

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

    saveas = ActionChains(driver).key_down(Keys.COMMAND).send_keys('s').key_up(Keys.COMMAND)
    saveas.perform()

    time.sleep(2)
    app('System Events').keystroke('\r')
    time.sleep(2)

if __name__ == '__main__':
    DEBUG = False
    SLEEPTIME = 1
    CWD = os.getcwd()
    USER_BUCKET = 'travel'
    SAVE_DIR = CWD + '/../data/{}/'.format(USER_BUCKET)

    if DEBUG:
        users = ['patricknorton', 'taylorswift']
    else:
        users = get_users('../data/{}.txt'.format(USER_BUCKET))

    # Account for users that have been scraped in previous iteration
    raw_pages = os.listdir('../data/{}/'.format(USER_BUCKET)) + os.listdir('../data/raw/')

    for user in users:
        # Check if exists
        if any(user.lower() in s.lower() for s in raw_pages):
            continue

        # Set profile, inside for loop because doesn't exist after used
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", SAVE_DIR)

        # Load driver to load page
        driver = webdriver.Firefox(firefox_profile=profile)

        get_page(user, driver, sleeptime=SLEEPTIME)

        # Write log when done
        with open('../logs/log_scrape_users.txt', 'ab') as f:
            f.write('{} saved page for {}\n'.format(time.strftime('%Y%m%d.%H:%M:%s'), user))

        # Page is not available/404
        if 'The link you followed may be broken, or the page may have been removed.' in driver.page_source:
            driver.close()
            continue

        # Check if HTML file is saved to conserve memory
        while not any(user.lower() in s.lower() and 'html' in s.lower() for s in os.listdir(SAVE_DIR)):
            print '{} Saving {} to {}'.format(time.strftime('%Y%m%d.%H:%M:%s'), user, SAVE_DIR)
            time.sleep(3)

        time.sleep(5)
        driver.close()
