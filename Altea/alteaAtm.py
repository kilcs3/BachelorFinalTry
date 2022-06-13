import os
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

findThemaAtmung = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/2"]')
findThemaAtmung.click()
time.sleep(3)

# findClassRow = drive.find_elements(By.XPATH, '/html/body/div/main/section[3]/div/div/div/div[2]/div/div[1]')
# findClassThreat = drive.find_elements(By.XPATH, '/html/body/div/main/section[3]/div/div/div/div[2]/div/div[1]/div')

findAtmenUndAngst = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div[3]/div[2]/div/div[2]/ul/li[1]/a')
findAtmenUndAngstLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/32"]')

findAtmenUndAngstLink.click()

time.sleep(2)

#KommentareAtmungAllesInklErklärung

uebersichtKommentareAtmung = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]')
# commentItemInner = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]/div')
# innerContent = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]/div/div[2]')
#Liste für Text reinschreiben und Liste für CSV
Liste = []
AtmungListe = []
for KommentarAtmung in range(len(uebersichtKommentareAtmung)):
    AtmungListe.append(uebersichtKommentareAtmung[KommentarAtmung].text)



data = pd.DataFrame(Liste)
data['kommentareAtmung'] = AtmungListe
data.to_csv('tableAt', index = False)

drive.close()




