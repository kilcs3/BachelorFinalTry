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

findThemaHaut = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/14"]')
findThemaHaut.click()

drive.implicitly_wait(5)

findHaarverlust = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findHaarverlustLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/31"]')
findHaarverlustLink.click()

drive.implicitly_wait(15)

uebersichtKommentareHaare1 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]')
uebersichtKommentareHaare2 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[3]')
uebersichtKommentareHaare3 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[4]')
uebersichtKommentareHaare4 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[5]')
uebersichtKommentareHaare5 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[6]')

drive.implicitly_wait(10)

Liste = []
HaarListe1 = []
HaarListe2 = []
HaarListe3 = []
HaarListe4 = []
HaarListe5 = []
for KommentarHaare1 in range(len(uebersichtKommentareHaare1)):
    HaarListe1.append(uebersichtKommentareHaare1[KommentarHaare1].text)

for KommentarHaare2 in range(len(uebersichtKommentareHaare2)):
    HaarListe2.append(uebersichtKommentareHaare2[KommentarHaare2].text)

for KommentarHaare3 in range(len(uebersichtKommentareHaare3)):
    HaarListe3.append(uebersichtKommentareHaare3[KommentarHaare3].text)

for KommentarHaare4 in range(len(uebersichtKommentareHaare4)):
    HaarListe4.append(uebersichtKommentareHaare4[KommentarHaare4].text)

for KommentarHaare5 in range(len(uebersichtKommentareHaare5)):
    HaarListe5.append(uebersichtKommentareHaare5[KommentarHaare5].text)





drive.implicitly_wait(30)

data= pd.DataFrame(Liste)
data['kommentareHaare1']=HaarListe1
data['kommentareHaare2']=HaarListe2
data['kommentareHaare3']=HaarListe3
data['kommentareHaare4']=HaarListe4
data['kommentareHaare5']=HaarListe5
data.to_csv('tableHaare', index=False)

drive.close()

