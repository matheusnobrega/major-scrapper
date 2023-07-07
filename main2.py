from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import pandas as pd

BASE = 'https://www.hltv.org'
info_jogadores = []

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

for link in majors:
    driver.get(BASE + link)

    botao_players = driver.find_element(By.PARTIAL_LINK_TEXT, 'Players')
    botao_players.click()

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    camp = soup.find('div', {'class': 'event-hub-title'}).getText()
    tabela = soup.find('table', {'class': 'stats-table player-ratings-table'})

    trs = tabela.findAll('tr')

    for tr in trs[1:]:
        jogador = {}

        jogador['name'] = tr.find('td', {'class':'playerCol'}).getText()
        jogador['nationality'] = tr.find('img', {'class':'flag'})['alt']
        jogador['team'] = tr.find('td', {'class': 'teamCol'}).getText()
        jogador['maps'] = int(tr.find('td', {'class': 'statsDetail'}).getText())
        jogador['rounds'] = int(tr.find('td', {'class': 'statsDetail gtSmartphone-only'}).getText())
        jogador['KD-diff'] = tr.find('td', {'class': 'kdDiffCol'}).getText()
        jogador['KD'] = tr.findAll('td', {'class': 'statsDetail'})[-1].getText()
        jogador['rating'] = tr.find('td', {'class': 'ratingCol'}).getText()
        jogador['event'] = camp

        info_jogadores.append(jogador)

dataset = pd.DataFrame(info_jogadores)
    
dataset.to_csv('major-stats.csv', sep = ';', index = False, encoding = 'utf-8')


driver.quit()
