import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from config import *
import random
import logging

import selenium_metamask_automation

from web3 import Web3

web3 = Web3(Web3.HTTPProvider("https://eth.llamarpc.com"))

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", filename="log.log",filemode="w")




tx=0


with open("wallet.txt", "r") as f:

    text=f.read().strip()
    lis=text.split("\n")

    


for i in range(len(lis)):

    

    


    chrome_options = Options()
    chrome_options.add_extension("Rabby Wallet.crx")

    driver = webdriver.Chrome(options=chrome_options, executable_path="chromedriver.exe")
    



    



    
    address=web3.eth.account.from_key(lis[i]).address

    



    sleep(2)

    
    driver.get("chrome-extension://acmacodkjbdgmoleebolmdjonilkdbch/popup.html")

    sleep(4)

    driver.find_element(By.XPATH, '//*[@id="root"]/div/section/footer/button').click()

    sleep(1)

    driver.find_element(By.XPATH, '//*[@id="root"]/div/section/footer/a/button').click()

    sleep(1)

    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[2]').click()

    sleep(1)

    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("wewewewe")

    sleep(1)

    driver.find_element(By.XPATH, '//*[@id="confirmPassword"]').send_keys("wewewewe")

    sleep(1)

    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/div[3]/button').click()

    sleep(2)

    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]').click()

    sleep(1)

    driver.find_element(By.XPATH, '//*[@id="key"]').send_keys(lis[i])

    sleep(1)

    driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div[3]/div/button').click()
    
    sleep(1)

    driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div[3]/div/button').click()

    driver.maximize_window()

    

    sleep(3)



    driver.get("https://app.zerion.io/connect-wallet")



    sleep(4)

    inp8=driver.find_element(By.XPATH, '//*[@id="PageWrapper"]/div/div/div[2]/div[2]/div/div[1]/div/div/button[2]').click()






    sleep(5)

    driver.switch_to.window(driver.window_handles[1])


    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[3]/div/button[1]').click()

    sleep(5)

    

    driver.switch_to.window(driver.window_handles[0])


    for i in range(txa):


        try:
            driver.get("https://app.zerion.io/send/token")

            sleep(3)

            driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[3]/div/div/div[3]/div/div/form/div[1]/button').click()

            sleep(2)

            driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[3]/div/div/div[3]/div/div/form/div[1]/div[1]/div/button[7]').click()

            sleep(1)



            driver.find_element(By.XPATH, '//*[@id="buy"]').send_keys(str(round(random.uniform(min_xdai, max_xdai), 7)))

            sleep(2)


            driver.find_element(By.XPATH, '//*[@id="send-to"]').send_keys(address)

            sleep(4)

            driver.find_element(By.XPATH, '//*[@id="PageWrapper"]/div/div[3]/div/div/form/button').click()

            sleep(4)

            driver.switch_to.window(driver.window_handles[1])

            sleep(4)


            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/section/div[3]/div/button').click()

            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/section/div[3]/div/button[1]').click()



            driver.switch_to.window(driver.window_handles[0])

            sleep(4)

            tx+=1

        except:

            pass

        (random.randint(tx_pause_min, tx_pause_max))
            
     

            



    
    
    logging.info(f"Wallet {address}| Success {tx}")
    tx=0

    driver.quit()

    

    































#C:\Users\1\AppData\Local\Google\Chrome\User Data\Default\Extensions\acmacodkjbdgmoleebolmdjonilkdbch\acmacodkjbdgmoleebolmdjonilkdbch.pem








