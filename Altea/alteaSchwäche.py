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

#Finde die Themenübersicht (Liste aller Symptome und click auf Symptome "Schwaeche"

findThemenUebersicht = drive.find_elements(By.XPATH, '/html/body/div/main/section[3]/div/div/div/div/div[1]/a/div/div')
findLinkZuThemenUebersicht = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum"]')
findLinkZuThemenUebersicht.click()

time.sleep(2)
findSympSchwaech = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/3"]')
findSympSchwaech.click()

time.sleep(2)

findZurueckZumSport = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findZurueckZumSportLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/7"]')
findZurueckZumSportLink.click()

time.sleep(2)

uebersichtKommentareSchwaeche = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]')
Liste = []

SchwaecheListe = []
for kommentarSchwaeche in range(len(uebersichtKommentareSchwaeche)):
    SchwaecheListe.append(uebersichtKommentareSchwaeche[kommentarSchwaeche].text)



data = pd.DataFrame(Liste)
data['kommentarSchwaeche'] = SchwaecheListe
data.to_csv('tableSchwaech.csv', index = False)