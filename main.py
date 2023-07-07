from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=options)

driver.get("https://pt.wikipedia.org/wiki/Selenium_(software)")
text = driver.find_element_by_class_name('mw-parser-output').text

print(text)

# Importante utilizar o quit() para reaproveitar o selenium sem precisar reiniciar o container
driver.quit()