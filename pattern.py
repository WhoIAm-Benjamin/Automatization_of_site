import pyautogui # clicks
import keyboard # for testing
import os # paths
import re # regex
import logging # for logs
from selenium import webdriver # web driver for work in browser
from selenium.common import exceptions as ex
from time import sleep

logging.basicConfig(level = logging.DEBUG,
					format = '%(asctime)s : %(levelname)s : %(message)s',
					filename = r'logs.log',
					filemode = 'w')

def main():
    """
    :return: None
    """
    global regex
    logging.info('Definition "main"')
    global driver
    regex = re.compile('\w{14}\-')
    logging.debug('Regex is enable')
    width, height = pyautogui.size()
    logging.info('Width: {}, Height: {}'.format(width, height))
    # keyboard.wait('ctrl+1')
    # path = os.path.join(os.getcwd(), 'Web Drivers', 'operadriver.exe')
    path = os.path.join(os.getcwd(), 'Web Drivers', 'chromedriver.exe')
    chromeoptions = webdriver.ChromeOptions()
    logging.debug('chromeoptions is enable')
    chromeoptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    # chromeoptions.add_argument("--no-sandbox")
    # chromeoptions.add_argument("--disable-setuid-sandbox")
    chromeoptions.add_argument("--remote-debugging-port=9222")  # don't remote
    chromeoptions.add_argument("--disable-dev-shm-using")
    chromeoptions.add_argument("--disable-extensions")
    chromeoptions.add_argument("--disable-gpu")
    chromeoptions.add_argument("start-maximized")
    chromeoptions.add_argument("disable-infobars")
    # chromeoptions.add_argument("--headless")
    # chromeoptions.add_argument('--disable-blink-features')
    # chromeoptions._binary_location = r'C:\Users\Трясучкин\AppData\Local\Programs\Opera\launcher.exe'
    logging.debug('Options was appended')
    try:
        driver = webdriver.Chrome(executable_path=path, options = chromeoptions)
        logging.debug('Not errors in start browser')
    except ex.WebDriverException as e:
        print('See logs')
        logging.warning('Crash browser: {}'.format(e))
        sleep(5)

if __name__ == '__main__':
    main()