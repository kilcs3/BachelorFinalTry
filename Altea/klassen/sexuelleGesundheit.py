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

findSexuelleUndReprodutiveGesundheit =drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/21"]')
findSexuelleUndReprodutiveGesundheit.click()

drive.implicitly_wait(11)

findMenstruation = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findMenstruationLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/27"]')
findMenstruationLink.click()

uebersichtKommentareMens1 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]/div')
uebersichtKommentareMens2 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[3]/div')

ListeMens1 = []
ListeMens2 = []
Liste = []

for kommentarMens1 in range(len(uebersichtKommentareMens1)):
    ListeMens1.append(uebersichtKommentareMens1[kommentarMens1].text)

for kommentarMens2 in range(len(uebersichtKommentareMens2)):
    ListeMens2.append(uebersichtKommentareMens2[kommentarMens2].text)

drive.implicitly_wait(12)

data = pd.DataFrame(Liste)
data['KommentarMens1'] = ListeMens1
data['KommentarMens2'] = ListeMens2
data.to_csv('tableMens', index=False)