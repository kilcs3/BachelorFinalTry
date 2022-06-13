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
drive.implicitly_wait(7)
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

findThemaSchlaf = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/15"]')
findThemaSchlaf.click()

time.sleep(5)

findSchlaf = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/div/div')
findSchlafLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/19"]')
findSchlafLink.click()
drive.implicitly_wait(10)

uebersichtKommentareSchlaf1 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]/div')
uebersichtKommentareSchlaf2 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[3]/div')

drive.implicitly_wait(2)

uebersichtKommentareSchlaf3 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[4]/div')
uebersichtKommentareSchlaf4 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[5]/div')
uebersichtKommentareSchlaf5 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[6]/div')

drive.implicitly_wait(19)

Liste = []
SchlafListe1 = []
SchlafListe2 = []
SchlafListe3 = []
SchlafListe4 = []
SchlafListe5 = []

for KommentarSchlaf1 in range(len(uebersichtKommentareSchlaf1)):
    uebersichtKommentareSchlaf1.append(uebersichtKommentareSchlaf1[KommentarSchlaf1].text)

for KommentarSchlaf2 in range(len(uebersichtKommentareSchlaf2)):
    uebersichtKommentareSchlaf2.append(uebersichtKommentareSchlaf2[KommentarSchlaf2].text)

for KommentarSchlaf3 in range(len(uebersichtKommentareSchlaf3)):
    uebersichtKommentareSchlaf3.append(uebersichtKommentareSchlaf3[KommentarSchlaf3].text)

drive.implicitly_wait(11)


for KommentarSchlaf4 in range(len(uebersichtKommentareSchlaf4)):
    uebersichtKommentareSchlaf4.append(uebersichtKommentareSchlaf4[KommentarSchlaf4].text)

for KommentarSchlaf5 in range(len(uebersichtKommentareSchlaf5)):
    uebersichtKommentareSchlaf5.append(uebersichtKommentareSchlaf5[KommentarSchlaf5].text)
drive.implicitly_wait(33)
data = pd.DataFrame(Liste)
data['kommentareSchlaf1']= SchlafListe1
data['kommentareSchlaf2']= SchlafListe2
data['kommentareSchlaf3']= SchlafListe3
data['kommentareSchlaf4']= SchlafListe4
data['kommentareSchlaf5']= SchlafListe5
data.to_csv('tableSchlaf', index=False)

drive.close()

