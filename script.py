from selenium import webdriver
from time import sleep

for i in range(892, 1892):
    driver = webdriver.Chrome()

    if i < 10:
        num = '0000'
    elif i < 100:
        num = '000'
    elif i < 1000:
        num = '00'
    elif i >= 1000:
        num = '0'

    driver.get("https://cbssidearmlive.akamaized.net/live-e/20190319/kean/m-basebl/d55826a3-d2b1-4b1e-b93e-89aac36a809e/master_700/00000/master_700_" + num + str(i) + ".ts")
    sleep(5)
    driver.close()
