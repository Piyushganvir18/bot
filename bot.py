from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import json

path="./bot/chromedriver.exe"
driver=webdriver.Chrome(path)

def LOGIN(username,password):
    driver.get("https://www.instagram.com/")
    time.sleep(5)
    enter_username=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME,'username')))
    enter_username.send_keys(username)
    time.sleep(3)
    enter_password=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME,'password')))
    enter_password.send_keys(password)
    time.sleep(3)
    enter_password.send_keys(Keys.RETURN)
    time.sleep(5)
    #popup
    try:
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
        time.sleep(5)
    except:
        pass         
    #popup2
    try:
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(4)
    except:
        pass    
    time.sleep(3)
    #click on message
    driver.find_element(By.XPATH,'    /html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/span/div/a/div').click()
    time.sleep(4.5)
    
    
def searchAndSend(person,dm):
    # click on new message
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div').click()
    time.sleep(5)
    flag = False
    # enter name
    enter_person_name= WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/input')))
    enter_person_name.send_keys(person)
    time.sleep(3)
    try:
        # select_person
        select_person=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div[1]/div[1]/div/div/div[2]/div/div/span[2]/span/span')
        actions1=ActionChains(driver)
        actions1.click(select_person)
        time.sleep(5)
        actions1.perform()
        time.sleep(5)
        flag = True
    except:
        # click on cut button
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div/div').click()
        time.sleep(5)
        flag = False
    if(flag):
        # click on next button
        next_button=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div')))
        actions1=ActionChains(driver)
        actions1.click(next_button)
        time.sleep(5)
        actions1.perform()
        time.sleep(5)
        # type and send message
        messagebox=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')))
        time.sleep(4)
        messagebox.send_keys(dm)
        time.sleep(3)
        messagebox.send_keys(Keys.RETURN)
        print('sent to',person)
        a = open('./bot/Log_List.txt', 'a')
        str1 = "sent to " + person + "\n"
        a.write(str1)
        a.close()
        time.sleep(4)

def LOGOUT():
    # click on more
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/span/div/a/div').click()
    time.sleep(5)
    # click on log out
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[6]/div[1]/div/div/div/div/div').click()
    time.sleep(6)

your_array = []
with open('./bot/info/usernames.txt', 'r') as f:
    f.readline()  #first line skip
    for name in f:
        your_array.append(name)
f = open('./bot/info/accounts.json')
message = "DO YOU WANT PROMOTE YOUR BUSINESS?? || HERE I HAVE SOMETHING FOR YOU || IF WANT TO KNOW MORE ABOUT US CONTACT: https://www.instagram.com/promoting_genix_official/ || JUST DM HIM"
accounts = json.load(f)
for account in accounts:
    if not your_array:
        break
    print(account['username'],account['password'])
    LOGIN(account['username'],account['password'])
    time.sleep(20)
    for i in range(15):
        if not your_array:
            break
        person = your_array.pop()
        searchAndSend(person,message)
    LOGOUT()