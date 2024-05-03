from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get('http://localhost:3000/register')

search_box = driver.find_element(By.XPATH, '/html/body/div[2]/form/div[1]/input')
search_box.send_keys('Dory1')
search_box1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/div[2]/input')
search_box1.send_keys('ABC123')
search_box2 = driver.find_element(By.XPATH, '/html/body/div[2]/form/div[3]/input')
search_box2.send_keys('99999999999999999999999999999999999999')
search_box2 = driver.find_element(By.XPATH, '/html/body/div[2]/form/div[4]/input')
search_box2.send_keys('123456')

search_button = driver.find_element(By.XPATH, '/html/body/div[2]/form/button')
search_button.click()

element = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]')
value = element.text




address = ["Gamla Stan","Royal Palace of Stockholm","Vasa Museum", "Skansen Open-Air Museum","Gröna Lund Amusement Park","Stockholm City Hall","Fotografiska","ABBA The Museum","National Museum of Sweden","Ericsson Globe","Stadshuset Restaurant","Östermalm Saluhall","Djurgården Island","The ABBA Tribute Museum","Kungsträdgården Park","Nobel Museum","Moderna Museet","Tantolunden Park"]
info = []
if value == '×\nLicense plate already registered by other user':
    driver.get('http://localhost:3000')
    search_button = driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li/a')
    search_button.click()
    search_box = driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li/ul/form/div[1]/input')
    search_box.send_keys('789')
    search_box1 = driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li/ul/form/div[2]/input')
    search_box1.send_keys('123456')
    search_button = driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li/ul/form/button')
    search_button.click()
    for i in range(18):
        search_box = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/form/div[1]/input')
        search_box.send_keys('ABC123')
        search_box1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/form/div[2]/input')
        search_box1.send_keys('1')
        select_element = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/form/div[3]/select')
        select = Select(select_element)

        select.select_by_index(i)

        search_button = driver.find_element(By.XPATH, '/ html / body / div[2] / div[2] / div / form / button')
        search_button.click()
        element = driver.find_element(By.XPATH, '/ html / body / div[2] / div[1] / div / div[1]')
        value = element.text
        sub_list = ["ABC123", address[i]]
        if value == '×\nThis car is already parked in the selected location. Do not waste your money !':
            info.append(sub_list)
            break

print(info)


input("Press any key to exit...")


