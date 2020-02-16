from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import secrets
import pickle

def save_cookies(driver, filename):
    with open(filename, 'wb') as f:
        pickle.dump(driver.get_cookies(), f)

def load_cookies(driver, filename):
    with open(filename, 'rb') as f:
        cookies = pickle.load(f)
        
        for cookie in cookies:
            driver.add_cookie(cookie)

def signin_printly(driver):
    email = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/form/div[1]/input')
    email.send_keys(secrets.email)

    password = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/form/div[2]/div[1]/input')
    password.send_keys(secrets.password)

    # Click sign in
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/form/div[3]/input').click()

if __name__ == '__main__':
    driver = webdriver.Chrome(secrets.chromedriver_dir)
    driver.get('https://www.printful.com/dashboard/library')

    signin_printly(driver)

    upload_btn = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[3]/table/tr/td[1]/a')
    upload_btn.click()

    base_window = driver.window_handles[0]
    driver.switch_to_window(driver.window_handles[1])
