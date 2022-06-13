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
drive.implicitly_wait(35)
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

drive.implicitly_wait(10)

findThemaFatigue = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/13"]')
findThemaFatigue.click()
drive.implicitly_wait(20)

findIhreTippsFatigue = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findIhreTippsFatigueLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/36"]')
findIhreTippsFatigueLink.click()

drive.implicitly_wait(30)
#generaluebersichtFatigue = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]')
ubersichtKommentareFatigue = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]/div')
uebersichtKommentareFatigue = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[3]/div')
uebersichtKommentareFatigue3 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[4]/div')
uebersichtKommentareFatigue4 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[5]/div')
uebersichtKommentareFatigue5 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[6]')
Liste = []
FatigueListe = []
FatigueListe2 = []
FatigueListe3 = []
FatigueListe4 = []
FatigueListe5 = []
for KommentarFatigue in range(len(ubersichtKommentareFatigue)):
    FatigueListe.append(ubersichtKommentareFatigue[KommentarFatigue].text)

for KommentarFatigue2 in range(len(uebersichtKommentareFatigue)):
     FatigueListe2.append(uebersichtKommentareFatigue[KommentarFatigue2].text)

for KommentarFatigue3 in range(len(uebersichtKommentareFatigue3)):
    FatigueListe3.append(uebersichtKommentareFatigue3[KommentarFatigue3].text)

for KommentarFatigue4 in range(len(uebersichtKommentareFatigue4)):
    FatigueListe4.append(uebersichtKommentareFatigue4[KommentarFatigue4].text)

for KommentarFatigue5 in range(len(uebersichtKommentareFatigue5)):
    FatigueListe5.append(uebersichtKommentareFatigue5[KommentarFatigue5].text)


drive.implicitly_wait(25)
data = pd.DataFrame(Liste)
data['kommentareFatigue']= FatigueListe
data['kommentareFatigue2'] = FatigueListe2
data['kommentareFatigue3'] = FatigueListe3
data['kommentareFatigue4'] = FatigueListe4
data['kommentareFatigue5'] = FatigueListe5

data.to_csv('tableFatigue', index=False)

drive.close()