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

findHerzKreislauf = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/24"]')
findHerzKreislauf.click()

drive.implicitly_wait(2)

findPotsPuls = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findPotsPulsLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/43"]')
findPotsPulsLink.click()

drive.implicitly_wait(5)

uebersichtPuls1 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[2]/div')
uebersichtPuls2 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[3]/div')
uebersichtPuls3 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[4]/div')
uebersichtPuls4 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[5]/div')
uebersichtPuls5 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[6]/div')
uebersichtPuls6 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[7]/div')
uebersichtPuls7 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[8]/div')
uebersichtPuls8 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[9]/div')
uebersichtPuls9 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[10]/div')
uebersichtPuls10 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[11]/div')

Liste = []

ListePuls1 = []
ListePuls2 = []
ListePuls3 = []
ListePuls4 = []
ListePuls5 = []
ListePuls6 = []
ListePuls7 = []
ListePuls8 = []
ListePuls9 = []
ListePuls10 = []


drive.implicitly_wait(3)

for KommentarPuls1 in range(len(uebersichtPuls1)):
    ListePuls1.append(uebersichtPuls1[KommentarPuls1].text)

for KommentarPuls2 in range(len(uebersichtPuls2)):
    ListePuls2.append(uebersichtPuls2[KommentarPuls2].text)

for KommentarPuls3 in range(len(uebersichtPuls3)):
    ListePuls3.append(uebersichtPuls3[KommentarPuls3].text)

for KommentarPuls4 in range(len(uebersichtPuls4)):
    ListePuls4.append(uebersichtPuls4[KommentarPuls4].text)

for KommentarPuls5 in range(len(uebersichtPuls5)):
    ListePuls5.append(uebersichtPuls5[KommentarPuls5].text)

for KommentarPuls6 in range(len(uebersichtPuls6)):
    ListePuls6.append(uebersichtPuls6[KommentarPuls6].text)

for KommentarPuls7 in range(len(uebersichtPuls7)):
    ListePuls7.append(uebersichtPuls7[KommentarPuls7].text)

for KommentarPuls8 in range(len(uebersichtPuls8)):
    ListePuls8.append(uebersichtPuls8[KommentarPuls8].text)

for KommentarPuls9 in range(len(uebersichtPuls9)):
    ListePuls9.append(uebersichtPuls9[KommentarPuls9].text)

for KommentarPuls10 in range(len(uebersichtPuls10)):
    ListePuls10.append(uebersichtPuls10[KommentarPuls10].text)

drive.implicitly_wait(17)

data = pd.DataFrame(Liste)
data['KommentarPuls1'] = pd.Series(ListePuls1)
data['KommentarPuls2'] = pd.Series(ListePuls2)
data['KommentarPuls3'] = pd.Series(ListePuls3)
data['KommentarPuls4'] = pd.Series(ListePuls4)
data['KommentarPuls5'] = pd.Series(ListePuls5)
data['KommentarPuls6'] = pd.Series(ListePuls6)
data['KommentarPuls7'] = pd.Series(ListePuls7)
data['KommentarPuls8'] = pd.Series(ListePuls8)
data['KommentarPuls9'] = pd.Series(ListePuls9)
data['KommentarPuls10'] = pd.Series(ListePuls10)
data.to_csv('tablePuls', index=False)
