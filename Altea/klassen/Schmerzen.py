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

findThemaSchmerzen = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/19"]')
findThemaSchmerzen.click()

findKopfschmerzen = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findKopfschmerzenLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/46"]')
findKopfschmerzenLink.click()

drive.implicitly_wait(13)

uebersichtKommentareKopfschmerzen1 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]/div')
uebersichtKommentareKopfschmerzen2 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[3]/div')
uebersichtKommentareKopfschmerzen3 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[4]/div')
uebersichtKommentareKopfschmerzen4 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[5]/div')

drive.implicitly_wait(4)

Liste1 = []
ListeKopfschmerzen1 = []
ListeKopfschmerzen2 = []
ListeKopfschmerzen3 = []
ListeKopfschmerzen4 = []

for KommentarKopfschmerzen1 in range(len(uebersichtKommentareKopfschmerzen1)):
    ListeKopfschmerzen1.append(uebersichtKommentareKopfschmerzen1[KommentarKopfschmerzen1].text)

for KommentarKopfschmerzen2 in range(len(uebersichtKommentareKopfschmerzen2)):
    ListeKopfschmerzen2.append(uebersichtKommentareKopfschmerzen2[KommentarKopfschmerzen2].text)

for KommentarKopfschmerzen3 in range(len(uebersichtKommentareKopfschmerzen3)):
    ListeKopfschmerzen3.append(uebersichtKommentareKopfschmerzen3[KommentarKopfschmerzen3].text)

for KommentarKopfschmerzen4 in range(len(uebersichtKommentareKopfschmerzen4)):
    ListeKopfschmerzen4.append(uebersichtKommentareKopfschmerzen4[KommentarKopfschmerzen4].text)

drive.implicitly_wait(4)

findThemaSchmerzen = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/19"]')
findThemaSchmerzen.click()

findGliederSchmerzen = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findGliederSchmerzenLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/24"]')
findGliederSchmerzenLink.click()

time.sleep(7)

uebersichtKommentareMuskelschmerzen1 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]/div')
uebersichtKommentareMuskelschmerzen2 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[3]/div')
uebersichtKommentareMuskelschmerzen3 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[4]/div')
uebersichtKommentareMuskelschmerzen4 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[5]/div')
uebersichtKommentareMuskelschmerzen5 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[6]/div')
uebersichtKommentareMuskelschmerzen6 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[7]/div')
uebersichtKommentareMuskelschmerzen7 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[8]/div')
uebersichtKommentareMuskelschmerzen8 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[9]/div')
uebersichtKommentareMuskelschmerzen9 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[10]/div')
uebersichtKommentareMuskelschmerzen10 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[11]/div')
Liste1 = []
ListeMuskelschmerzen1 = []
ListeMuskelschmerzen2 = []
ListeMuskelschmerzen3 = []
ListeMuskelschmerzen4 = []
ListeMuskelschmerzen5 = []
ListeMuskelschmerzen6 = []
ListeMuskelschmerzen7 = []
ListeMuskelschmerzen8 = []
ListeMuskelschmerzen9 = []
ListeMuskelschmerzen10 = []

drive.implicitly_wait(12)

for KommentarMuskelschmerzen1 in range(len(uebersichtKommentareMuskelschmerzen1)):
    ListeMuskelschmerzen1.append(uebersichtKommentareMuskelschmerzen1[KommentarMuskelschmerzen1].text)

for KommentarMuskelschmerzen2 in range(len(uebersichtKommentareMuskelschmerzen2)):
    ListeMuskelschmerzen2.append(uebersichtKommentareMuskelschmerzen2[KommentarMuskelschmerzen2].text)

for KommentarMuskelschmerzen3 in range(len(uebersichtKommentareMuskelschmerzen3)):
    ListeMuskelschmerzen3.append(uebersichtKommentareMuskelschmerzen3[KommentarMuskelschmerzen3].text)

for KommentarMuskelschmerzen4 in range(len(uebersichtKommentareMuskelschmerzen4)):
    ListeMuskelschmerzen4.append(uebersichtKommentareMuskelschmerzen4[KommentarMuskelschmerzen4].text)

for KommentarMuskelschmerzen5 in range(len(uebersichtKommentareMuskelschmerzen5)):
    ListeMuskelschmerzen5.append(uebersichtKommentareMuskelschmerzen5[KommentarMuskelschmerzen5].text)

for KommentarMuskelschmerzen6 in range(len(uebersichtKommentareMuskelschmerzen6)):
    ListeMuskelschmerzen6.append(uebersichtKommentareMuskelschmerzen6[KommentarMuskelschmerzen6].text)

for KommentarMuskelschmerzen7 in range(len(uebersichtKommentareMuskelschmerzen7)):
    ListeMuskelschmerzen7.append(uebersichtKommentareMuskelschmerzen7[KommentarMuskelschmerzen7].text)

for KommentarMuskelschmerzen8 in range(len(uebersichtKommentareMuskelschmerzen8)):
    ListeMuskelschmerzen8.append(uebersichtKommentareMuskelschmerzen8[KommentarMuskelschmerzen8].text)

for KommentarMuskelschmerzen9 in range(len(uebersichtKommentareMuskelschmerzen9)):
    ListeMuskelschmerzen9.append(uebersichtKommentareMuskelschmerzen9[KommentarMuskelschmerzen9].text)

for KommentarMuskelschmerzen10 in range(len(uebersichtKommentareMuskelschmerzen10)):
    ListeMuskelschmerzen10.append(uebersichtKommentareMuskelschmerzen10[KommentarMuskelschmerzen10].text)

drive.implicitly_wait(8)

data = pd.DataFrame(Liste1)
data['KommentareKopfschmerzen1'] = ListeKopfschmerzen1
data['KommentareKopfschmerzen2'] = ListeKopfschmerzen2
data['KommentareKopfschmerzen3'] = ListeKopfschmerzen3
data['KommentareKopfschmerzen4'] = ListeKopfschmerzen4
data['KommentareMuskelschmerzen1'] = pd.Series(ListeMuskelschmerzen1)
data['KommentareMuskelschmerzen2'] = pd.Series(ListeMuskelschmerzen2)
data['KommentareMuskelschmerzen3'] = pd.Series(ListeMuskelschmerzen3)
data['KommentareMuskelschmerzen4'] = pd.Series(ListeMuskelschmerzen4)
data['KommentareMuskelschmerzen5'] = pd.Series(ListeMuskelschmerzen5)
data['KommentareMuskelschmerzen6'] = pd.Series(ListeMuskelschmerzen6)
data['KommentareMuskelschmerzen7'] = pd.Series(ListeMuskelschmerzen7)
data['KommentareMuskelschmerzen8'] = pd.Series(ListeMuskelschmerzen8)
data['KommentareMuskelschmerzen9'] = pd.Series(ListeMuskelschmerzen9)
data['KommentareMuskelschmerzen10'] = pd.Series(ListeMuskelschmerzen10)

data.to_csv('tableSchmerzen', index=False)
