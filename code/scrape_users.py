from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import selenium.webdriver as webdriver
from pykeyboard import PyKeyboard
# from appscript import app
import random
import time
import os

def get_users(filename):
    """
    load list of usernames from file

    INPUT:  file of users, separated by newline
    OUTPUT: list of users
    """
    with open(filename) as f:
        users = f.readlines()
    users = [name.split('\n')[0] for name in users if not name.startswith('#')]
    return set(users)


def get_page(user, driver, sleeptime=1, down_scrolls=int(3e2)):
    """
    collect data for a given username
    save webpage locally

    INPUT:  user, string name of user
            driver, Selenium driver object 
            sleeptime, integer number of seconds to pause between scrolls
            down_scrolls, integer number of times to scroll down user's page
    OUTPUT: None; raw page is saved to local drive
    """
    url = 'http://instagram.com/' + user
    driver.get(url)

    # Page is not available/404
    message_404 = 'The link you followed may be broken, or the page may have been removed.'
    if message_404 in driver.page_source:
        return
    # Must click 'Load More' button to see more content
    try:
        driver.find_element_by_link_text('LOAD MORE').click()
    # Content is not available for whatever reason
    except NoSuchElementException:
        print "Sorry, can't click LOAD MORE for {}".format(user)

    page = driver.page_source
    # Continue scrolling to load more content
    for i in xrange(down_scrolls):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        # Pause to update page
        time.sleep(sleeptime + random.random())
        # Stop early if the page hasn't changed since the last iteration
        if driver.page_source == page:
            break
        page = driver.page_source
    # Execute keyboard shortcuts to save entire page
    saveas = ActionChains(driver).key_down(Keys.CONTROL).send_keys('s').key_up(Keys.CONTROL)
    saveas.perform()
    # Pause again, to avoid 
    time.sleep(2)
    # app('System Events').keystroke('\r')
    kbrd = PyKeyboard()
    kbrd.press_key('Return')
    time.sleep(2)

if __name__ == '__main__':

    DEBUG = False 
    SLEEPTIME = 1
    CWD = os.getcwd()
    USER_BUCKET = 'models'
    SAVE_DIR = CWD + '/../data/{}/'.format(USER_BUCKET)

    if DEBUG:
        users = ['patricknorton', 'taylorswift']
    else:
        users = get_users('../data/{}.txt'.format(USER_BUCKET))

    # Account for users that have been scraped in previous iteration
    raw_pages = set( os.listdir('../data/{}/'.format(USER_BUCKET)) + os.listdir('../data/raw/') + os.listdir('../data/travel') )

    for user in users:
        # Check if exists
        if any(user.lower() in s.lower() for s in raw_pages):
            continue

        # Set profile, inside for loop because doesn't exist after used
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", SAVE_DIR)

        # Load driver to view page
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
        # Close driver each time to free system memory
        driver.close()
