from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def get_browser():
    chrome_options = Options()

    # Keep Browser Open when done
    chrome_options.add_experimental_option("detach", True)

    # Don't show browser
    chrome_options.add_argument('--headless=new')

    browser = webdriver.Chrome(options=chrome_options)
    browser.set_window_size(1300, 1600)
    return browser
