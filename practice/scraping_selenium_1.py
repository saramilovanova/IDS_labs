from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

MAIN_URL = 'https://www.rtvslo.si/gospodarstvo/vinarji-opozarjajo-na-kolicinsko-slabo-letino-kakovost-pridelanega-grozdja-pa-je-izjemna/726699'

driver = webdriver.Chrome()
driver.get(MAIN_URL)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

show_comments_btn = driver.find_element(By.CLASS_NAME, 'link-show-comments') # class of anchor tag
show_comments_btn.click()
time.sleep(3)

results = []
comments = driver.find_elements(By.CLASS_NAME, 'comment')
for comment in comments:
    p = comment.find_element(By.TAG_NAME, 'p')
    text = p.text.replace("\n", " ").strip()
    results.append(text)

df = pd.DataFrame(results, columns=['comment'])
df.to_csv('data/comments.csv', index=False)

driver.quit()
