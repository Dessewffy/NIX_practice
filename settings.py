from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_preconfigured_chrome_driver() -> webdriver.Chrome:
    options = Options()
    options.add_experimental_option('detach', True)

    return webdriver.Chrome(options=options)
