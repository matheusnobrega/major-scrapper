from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Caminho para o webdriver baixado em https://chromedriver.chromium.org/downloads
path = '/home/takeofriedrich/Documentos/chromedriver'

driver = webdriver.Chrome(path,options=options)

driver.get("https://pt.wikipedia.org/wiki/Selenium_(software)")
text = driver.find_element_by_class_name('mw-parser-output').text

print(text)

driver.close()
