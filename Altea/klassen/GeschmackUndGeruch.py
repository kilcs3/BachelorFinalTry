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

time.sleep(3)

#Finde die Themenübersicht (Liste aller Symptome und click auf Symptome "Atmung"

findThemenUebersicht = drive.find_elements(By.XPATH, '/html/body/div/main/section[3]/div/div/div/div/div[1]/a/div/div')
findLinkZuThemenUebersicht = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum"]')
findLinkZuThemenUebersicht.click()

time.sleep(2)

findThemaGeschmackLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/6"]')
findThemaGeschmackLink.click()
time.sleep(3)

findParosmie = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findParosmieLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/9"]')
findParosmieLink.click()

time.sleep(2)

uebersichtKommentareGeschmack = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]')

Liste = []
GeschmackListe = []

for KommenntarGeschmack in range(len(uebersichtKommentareGeschmack)):
    GeschmackListe.append(uebersichtKommentareGeschmack[KommenntarGeschmack].text)


data = pd.DataFrame(Liste)
data['kommentarGeschmack'] = GeschmackListe
data.to_csv('tableGeschmack', index = False)

drive.close()


