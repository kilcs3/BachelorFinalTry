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

findThemaHNO = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/16"]')
findThemaHNO.click()

findHalsschmerzen = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findHalsschmerzenLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/65"]')
findHalsschmerzenLink.click()

drive.implicitly_wait(4)

uebersichtKommentareHalschmerzen = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]/div')
ListeHalsschmerzen = []
Liste = []

for KommentarHalschmerzen in range(len(uebersichtKommentareHalschmerzen)):
    ListeHalsschmerzen.append(uebersichtKommentareHalschmerzen[KommentarHalschmerzen].text)
drive.implicitly_wait(15)

findThemaHNO = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/16"]')
findThemaHNO.click()

drive.implicitly_wait(9)

findOhrenschmerzen = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findOhrenschmerzenLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/62"]')
findOhrenschmerzenLink.click()

uebersichtOhrenschmerzen = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]/div')

OhrenschmerzenListe = []
for KommentarOhrenschmerzen in range(len(uebersichtOhrenschmerzen)):
    OhrenschmerzenListe.append(uebersichtOhrenschmerzen[KommentarOhrenschmerzen].text)
drive.implicitly_wait(27)

findThemaHNO = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/16"]')
findThemaHNO.click()

drive.implicitly_wait(1)

findOhrenGeraeusche = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findOhrenGeräuscheLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/57"]')
findOhrenGeräuscheLink.click()

uebersichtOhrenschmerzenGeraeusche = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]/div')


ListeOhrGeraeusche = []
for KommentarOhrgeraeusche in range(len(uebersichtOhrenschmerzenGeraeusche)):
    ListeOhrGeraeusche.append(uebersichtOhrenschmerzenGeraeusche[KommentarOhrgeraeusche].text)
drive.implicitly_wait(39)

findThemaHNO = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/16"]')
findThemaHNO.click()
drive.implicitly_wait(2)

findFieber = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findFieberLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/20"]')
findFieberLink.click()

uebersichtFieber1 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]/div')
uebersichtFieber2 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[3]/div')
uebersichtFieber3 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[4]/div')
uebersichtFieber4 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[5]/div')

ListeFieber1 = []
ListeFieber2 = []
ListeFieber3 = []
ListeFieber4 = []

drive.implicitly_wait(16)

for KommentarFieber1 in range(len(uebersichtFieber1)):
    ListeFieber1.append(uebersichtFieber1[KommentarFieber1].text)

for KommentarFieber2 in range(len(uebersichtFieber2)):
    ListeFieber2.append(uebersichtFieber2[KommentarFieber2].text)

for KommentarFieber3 in range(len(uebersichtFieber3)):
    ListeFieber3.append(uebersichtFieber3[KommentarFieber3].text)

for KommentarFieber4 in range(len(uebersichtFieber4)):
    ListeFieber4.append(uebersichtFieber4[KommentarFieber4].text)

time.sleep(3)

data = pd.DataFrame(Liste)
data['kommentarHalschmerzen'] = ListeHalsschmerzen
data['kommentareOhrenschmerzen'] = OhrenschmerzenListe
data['kommentarOhrengeraeusche'] = ListeOhrGeraeusche
data['kommentarFieber1'] = ListeFieber1
data['kommentarFieber2'] = ListeFieber2
data['kommentarFieber3'] = ListeFieber3
data['kommentarFieber4'] = ListeFieber4
data.to_csv('tableHNOFieber', index=False)
