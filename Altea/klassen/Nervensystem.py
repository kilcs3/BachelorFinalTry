from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.headless = True


drive = selenium.webdriver.Chrome(r"/Users/sabinekilchherr/PycharmProject/BachelorFinalTry/Altea/driver/chromedriver")
drive.get('https://www.altea-community.com/login')

#Login

searchInputLog = drive.find_element(By.XPATH, '//*[@id="root"]/main/section/div/div/div/form/input')
searchInputLog.send_keys("kurt.schmied.85@gmail.com")
searchInputPas = drive.find_element(By.XPATH, '//*[@id="root"]/main/section/div/div/div/form/div[1]/input')
searchInputPas.send_keys("Sonne_1234*")
searchInputSubBut = drive.find_element(By.XPATH, '//*[@id="root"]/main/section/div/div/div/form/div[2]/button[1]')
searchInputSubBut.submit()

drive.implicitly_wait(3)

#Finde die Themenübersicht (Liste aller Symptome und click auf Symptome "Atmung"

findThemenUebersicht = drive.find_elements(By.XPATH, '/html/body/div/main/section[3]/div/div/div/div/div[1]/a/div/div')
findLinkZuThemenUebersicht = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum"]')
findLinkZuThemenUebersicht.click()

drive.implicitly_wait(2)

findNervensystem = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/25"]')
findNervensystem.click()

findNeuropatie = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findNeuropatieLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/52"]')
findNeuropatieLink.click()

drive.implicitly_wait(15)

uebersichtKommentareNeuropatie1 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]/div')
uebersichtKommentareNeuropatie2 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[3]/div')
uebersichtKommentareNeuropatie3 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[4]/div')
uebersichtKommentareNeuropatie4 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[5]/div')

Liste = []
NeuropathieListe1 = []
NeuropathieListe2 = []
NeuropathieListe3 = []
NeuropathieListe4 = []

drive.implicitly_wait(10)

for KommentarNeuropatie1 in range(len(uebersichtKommentareNeuropatie1)):
    NeuropathieListe1.append(uebersichtKommentareNeuropatie1[KommentarNeuropatie1].text)

for KommentarNeuropatie2 in range(len(uebersichtKommentareNeuropatie2)):
    NeuropathieListe2.append(uebersichtKommentareNeuropatie2[KommentarNeuropatie2].text)

for KommentarNeuropatie3 in range(len(uebersichtKommentareNeuropatie3)):
    NeuropathieListe3.append(uebersichtKommentareNeuropatie3[KommentarNeuropatie3].text)

for KommentarNeuropatie4 in range(len(uebersichtKommentareNeuropatie4)):
    NeuropathieListe4.append(uebersichtKommentareNeuropatie4[KommentarNeuropatie4].text)

data= pd.DataFrame(Liste)
data['KommentarNeuropatie1'] = NeuropathieListe1
data['KommentarNeuropatie2'] = NeuropathieListe2
data['KommentarNeuropatie3'] = NeuropathieListe3
data['KommentarNeuropatie4'] = NeuropathieListe4
data.to_csv('tableNeuropathie', index=False)
