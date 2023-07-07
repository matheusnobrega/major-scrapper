from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

BASE = 'https://www.hltv.org'

options = uc.ChromeOptions()
#options.add_argument("--headless")

# Caminho para o webdriver baixado em https://chromedriver.chromium.org/downloads
path = "C:\Program Files (x86)\chromedriver.exe"

service = Service(executable_path=path)
driver = uc.Chrome(use_subprocess=True, service=service,options=options)

driver.get("https://www.hltv.org/stats/events?matchType=Majors")

botao = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "CybotCookiebotDialogBodyButton")) # (By.CLASS_NAME, "S-dialog__closebtn") (By.XPATH, "//span[@id='NewReleases_btn_next']")
                )
botao.click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

tds = soup.findAll('td', {'class':'name-col'})

majors = [td.find('a')['href'] for td in tds]

print(majors)

for link in majors:
    driver.get(BASE + link)


driver.quit()
