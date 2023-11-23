from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import time

import undetected_chromedriver as uc
from undetected_chromedriver import ChromeOptions


options = Options()
options.add_extension('/metamask.crx')
driver = webdriver.Chrome(options=options)
driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome')
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)

#Главная стр.
driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[1]/div').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[3]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div/button[1]').click()
time.sleep(2)


#Ввод сид-фразы
seed = 'wrist wise piano movie room govern awake elevator protect alpha merry embody'
seed = seed.split()
for i in range(0, 12):
    driver.find_element(By.CSS_SELECTOR, f'[data-testid="import-srp__srp-word-{i}"]').send_keys(seed[i])
#Кнопка согласен
driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[4]/div/button').click()
time.sleep(2)


#Ввод пароля
passwd = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input')
passwd_repeat = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input')
passwd.send_keys('QWE-qwe-123')
time.sleep(2)
passwd_repeat.send_keys('QWE-qwe-123')
time.sleep(2)
#Импорт
driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[3]/label/h5').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button').click()
time.sleep(2)
#Понятно
driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button').click()
time.sleep(2)
#Далее
driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button').click()
time.sleep(2)
#Выполнено
driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="popover-content"]/div/div/section/div[1]/div/button').click()





driver.get('https://passport.gitcoin.co/')
#Sign in with Ethereum
driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/button').click()
time.sleep(2)
#Connect Wallet
shadow = driver.find_element(By.XPATH, '/html/body/onboard-v2').shadow_root
shadow.find_element(By.CSS_SELECTOR, '[class="wallet-button-container svelte-1vlog3j"]').click()
time.sleep(5)
#
driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]').click()
time.sleep(2)






#options = uc.ChromeOptions()
#options.headless = False
#options.add_extension('/metamask.crx')
#driver = uc.Chrome(options=options, version_main=118)
#driver.get("https://www.google.com/")



time.sleep(5000)
driver.quit()