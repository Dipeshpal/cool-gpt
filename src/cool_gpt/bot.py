from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from element_manager import *
import time


def setup_driver(debug=True):
    """
    This sets up the driver in headless mode
    :return: selenium driver
    """
    # to open the Chrome browser try to set up the driver
    try:
        print('Setting up driver...')
        if debug:
            print('Make sure you have the chromedriver.exe in the same directory as this script.')
            print('If you don\'t have it, download it from https://chromedriver.chromium.org/downloads')
            print('Currently only supports Chrome and Windows.')
            print('To disable above message, set "setup_driver(debug=True)"')
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        time.sleep(2)
        # to open the url in browser
        driver.get(
            'https://www.toolbot.ai/apps/Jarvis%20AI%20Helper?desc=A%20comprehensive%20AI%20tool%20to%20answer%20all%20your%20queries&placeholder=Ask%20me%20anything!%20')

        # open the chatbot
        driver.find_element(By.XPATH, get_xpath(driver, 'Y3g6utaFWEEXTIo')).click()
        time.sleep(2)
        print('Driver setup complete.')
        return driver
    except Exception as e:
        print(e)
        raise e


last_res = ''
response = ''


def ask(message: str, driver):
    """
    :param message: the message to ask the chatbot
    :param driver: the driver to use
    :return: response from the chatbot
    """
    try:
        global last_res
        global response

        driver.find_element(By.XPATH, get_xpath(driver, 'LWsEweTq87BAOpN')).clear()

        # to type content in input field
        driver.find_element(By.XPATH, get_xpath(driver, 'LWsEweTq87BAOpN')).send_keys(message)
        time.sleep(2)

        # to click on the element(Loading...) found
        driver.find_element(By.XPATH, get_xpath(driver, '1Xk8JF95dFcOjTb')).click()
        time.sleep(4)

        while last_res == response:
            try:
                response = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[3]/div').text
                time.sleep(4)
            except:
                time.sleep(4)
        last_res = response
        return response
    except Exception as e:
        print(e)
        raise e


if __name__ == '__main__':
    # from cool_gpt import bot

    driver = setup_driver()
    while True:
        message = input('You: ')
        print('Bot:', ask(message, driver))
