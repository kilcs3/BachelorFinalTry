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

findThemaPsyche = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/17"]')
findThemaPsyche.click()

drive.implicitly_wait(14)

findStress = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findStressLink = drive.find_element(By.CSS_SELECTOR, '[href="/forum/post/22"]')
findStressLink.click()

ubersichtStress1 = drive.find_elements(By.XPATH,'//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]/div')
ubersichtStress2 = drive.find_elements(By.XPATH,'//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[3]/div')
ubersichtStress3 = drive.find_elements(By.XPATH,'//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[4]/div')
ubersichtStress4 = drive.find_elements(By.XPATH,'//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[5]/div')
ubersichtStress5 = drive.find_elements(By.XPATH,'//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[6]/div')

Liste =[]
ListeStress1 =[]
ListeStress2 =[]
ListeStress3 =[]
ListeStress4 =[]
ListeStress5 =[]

drive.implicitly_wait(12)

for KommentarStress1 in range(len(ubersichtStress1)):
    ListeStress1.append(ubersichtStress1[KommentarStress1].text)

for KommentarStress2 in range(len(ubersichtStress2)):
    ListeStress2.append(ubersichtStress2[KommentarStress2].text)

for KommentarStress3 in range(len(ubersichtStress3)):
    ListeStress3.append(ubersichtStress3[KommentarStress3].text)

for KommentarStress4 in range(len(ubersichtStress4)):
    ListeStress4.append(ubersichtStress4[KommentarStress4].text)

for KommentarStress5 in range(len(ubersichtStress5)):
    ListeStress5.append(ubersichtStress5[KommentarStress5].text)

findThemaPsyche = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/17"]')
findThemaPsyche.click()

drive.implicitly_wait(36)

findAngst = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findAngstLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/21"]')
findAngstLink.click()

uebersichtAngst1 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]')
uebersichtAngst2 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[3]/div')
uebersichtAngst3 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[4]/div')
uebersichtAngst4 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[5]/div')
uebersichtAngst5 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[6]/div')


ListeAngst1 = []
ListeAngst2 = []
ListeAngst3 = []
ListeAngst4 = []
ListeAngst5 = []


drive.implicitly_wait(2)

for KommentarAngst1 in range(len(uebersichtAngst1)):
    ListeAngst1.append(uebersichtAngst1[KommentarAngst1].text)

for KommentarAngst2 in range(len(uebersichtAngst2)):
    ListeAngst2.append(uebersichtAngst2[KommentarAngst2].text)

for KommentarAngst3 in range(len(uebersichtAngst3)):
    ListeAngst3.append(uebersichtAngst3[KommentarAngst3].text)

for KommentarAngst4 in range(len(uebersichtAngst4)):
    ListeAngst4.append(uebersichtAngst4[KommentarAngst4].text)

for KommentarAngst5 in range(len(uebersichtAngst5)):
    ListeAngst5.append(uebersichtAngst5[KommentarAngst5].text)

drive.implicitly_wait(17)

data = pd.DataFrame(Liste)
data['kommentarStress1'] = ListeStress1
data['kommentarStress2'] = ListeStress2
data['kommentarStress3'] = ListeStress3
data['kommentarStress4'] = ListeStress4
data['kommentarStress5'] = ListeStress5
data['kommentarAngst1'] = ListeAngst1
data['kommentarAngst2'] = ListeAngst2
data['kommentarAngst3'] = ListeAngst3
data['kommentarAngst4'] = ListeAngst4
data['kommentarAngst5'] = ListeAngst5

data.to_csv('tableAngstUndStress', index=False)
