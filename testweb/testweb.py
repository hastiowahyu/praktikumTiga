from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

my_json = open('./testcase.json', 'r')
json_data = my_json.read()

obj = json.loads(json_data)

PATH = "D:/chromeDriver/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://localhost:3000/")

nama_input = driver.find_element_by_name('username')
username_input = driver.find_element_by_name('emailid')
password_input = driver.find_element_by_name('mobileno')
repassword_input = driver.find_element_by_name('password')
submit = driver.find_element_by_name('register')

for i in obj:
    nama_input.clear()
    nama_input.send_keys(i['data']['username'])
    time.sleep(1)
    username_input.clear()
    username_input.send_keys(i['data']['emailid'])
    time.sleep(1)
    password_input.clear()
    password_input.send_keys(i['data']['mobileno'])
    time.sleep(1)
    repassword_input.clear()
    repassword_input.send_keys(i['data']['password'])
    time.sleep(1)
    submit.click()
    time.sleep(5)

driver.quit()