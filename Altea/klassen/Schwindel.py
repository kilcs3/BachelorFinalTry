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

findThemaSchwäche = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/topic/18"]')
findThemaSchwäche.click()

findSchwindel = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[3]/div/div/div/div[2]/ul')
findSchwindelLink = drive.find_element(By.CSS_SELECTOR, 'a[href="/forum/post/23"]')
findSchwindelLink.click()

drive.implicitly_wait(18)

uebersichtKommentareSchwindel1 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[15]/div')
uebersichtKommentareSchwindel2 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[16]/div')
uebersichtKommentareSchwindel3 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[18]/div')
uebersichtKommentareSchwindel4 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[19]/div')
uebersichtKommentareSchwindel5 = drive.find_elements(By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[20]/div')
uebersichtKommentareSchwindel6 = drive.find_elements(By.XPATH,'//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[21]/div')
uebersichtKommentareSchwindel7 = drive.find_elements(By.XPATH,'//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[22]/div')
uebersichtKommentareSchwindel8 = drive.find_elements(By.XPATH,'//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[23]/div')
uebersichtKommentareSchwindel9 = drive.find_elements(By.XPATH,'//*[@id="root"]/main/section[2]/div/div/div[1]/div[3]/div[2]/div[24]/div')

Liste = []
Schwindelliste1 = []
Schwindelliste2 = []
Schwindelliste3 = []
Schwindelliste4 = []
Schwindelliste5 = []
Schwindelliste6 = []
Schwindelliste7 = []
Schwindelliste8 = []
Schwindelliste9 = []

drive.implicitly_wait(9)


for KommentarSchwindel1 in range(len(uebersichtKommentareSchwindel1)):
    Schwindelliste1.append(uebersichtKommentareSchwindel1[KommentarSchwindel1].text)

for KommentarSchwindel2 in range(len(uebersichtKommentareSchwindel2)):
    Schwindelliste2.append(uebersichtKommentareSchwindel2[KommentarSchwindel2].text)

for KommentarSchwindel3 in range(len(uebersichtKommentareSchwindel3)):
    Schwindelliste3.append(uebersichtKommentareSchwindel3[KommentarSchwindel3].text)

for KommentarSchwindel4 in range(len(uebersichtKommentareSchwindel4)):
    Schwindelliste4.append(uebersichtKommentareSchwindel4[KommentarSchwindel4].text)

for KommentarSchwindel5 in range(len(uebersichtKommentareSchwindel5)):
    Schwindelliste5.append(uebersichtKommentareSchwindel5[KommentarSchwindel5].text)

for KommentarSchwindel6 in range(len(uebersichtKommentareSchwindel6)):
    Schwindelliste6.append(uebersichtKommentareSchwindel6[KommentarSchwindel6].text)

for KommentarSchwindel7 in range(len(uebersichtKommentareSchwindel7)):
    Schwindelliste7.append(uebersichtKommentareSchwindel7[KommentarSchwindel7].text)

for KommentarSchwindel8 in range(len(uebersichtKommentareSchwindel8)):
    Schwindelliste8.append(uebersichtKommentareSchwindel8[KommentarSchwindel8].text)

for KommentarSchwindel9 in range(len(uebersichtKommentareSchwindel9)):
    Schwindelliste9.append(uebersichtKommentareSchwindel9[KommentarSchwindel9].text)


drive.implicitly_wait(24)

data = pd.DataFrame(Liste)
data['KommentarSchwindel1'] = Schwindelliste1
data['KommentarSchwindel2'] = Schwindelliste2
data['KommentarSchwindel3'] = Schwindelliste3
data['KommentarSchwindel4'] = Schwindelliste4
data['KommentarSchwindel5'] = Schwindelliste5
data['KommentarSchwindel6'] = Schwindelliste6
data['KommentarSchwindel7'] = Schwindelliste7
data['KommentarSchwindel8'] = Schwindelliste8
data['KommentarSchwindel9'] = Schwindelliste9

data.to_csv('tableSchwindel', index=False)