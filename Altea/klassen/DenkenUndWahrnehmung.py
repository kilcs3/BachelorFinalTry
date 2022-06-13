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

drive.implicitly_wait(5)

findThemaDenken = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/12"]')
findThemaDenken.click()
time.sleep(3)


findVerwirrung = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findVerwirrungLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/39"]')
findVerwirrungLink.click()

time.sleep(2)

uebersichtKommentareVerwirrung = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]')

Liste = []
VerwirrungListe = []

for kommentarVerwirrung in range(len(uebersichtKommentareVerwirrung)):
    VerwirrungListe.append(uebersichtKommentareVerwirrung[kommentarVerwirrung].text)
time.sleep(15)

findThemaDenken = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/12"]')
findThemaDenken.click()

drive.implicitly_wait(10)
findVergesslichkeit = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
#findVergesslichkeitKlasse = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/div/div[2]')
#findVergesslichkeitTherat = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/div/div[2]/div')
drive.implicitly_wait(20)
findVergesslichkeitLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/38"]')
#findVergesslichkeitLinkContentWraper = drive.find_element(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/div/div[2]/div/div')
#findVergesslichkeitLinkKlasse = drive.find_element(By.CSS_SELECTOR, 'a[class_="link"]')
findVergesslichkeitLink.click()

time.sleep(3)

uebersichtKommentareVergesslichkeit = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]')
vergesslichkeitsListe = []
for KommentarVergesslichkeit in range(len(uebersichtKommentareVergesslichkeit)):
    vergesslichkeitsListe.append(uebersichtKommentareVergesslichkeit[KommentarVergesslichkeit].text)
drive.implicitly_wait(25)

findThemaDenken = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/12"]')
findThemaDenken.click()

drive.implicitly_wait(20)
findKonzentration = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findKonzentrationLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/16"]')
findKonzentrationLink.click()

time.sleep(3)

uebersichtKommentareKonzentration = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]')
Konzentrationsliste = []

for KommentarKonzentration in range(len(uebersichtKommentareKonzentration)):
    Konzentrationsliste.append(uebersichtKommentareKonzentration[KommentarKonzentration].text)

drive.implicitly_wait(20)




data = pd.DataFrame(Liste)
data['kommentareVerwirrung'] = VerwirrungListe
data['kommentareVergesslichkeit'] = vergesslichkeitsListe
data['kommentareKonzentration'] = Konzentrationsliste
data.to_csv('tableDenken', index = False)


