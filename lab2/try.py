from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json

MAIN_URL = "https://quotes.toscrape.com/" # this is a static website, it can print everything without waiting
driver = webdriver.Chrome()
driver.get(MAIN_URL)

# print(driver.page_source) # this is the source code of the page
# sleep(10)

divs = driver.find_elements(By.CSS_SELECTOR, "div.quote") # list of all quotes
print(f"Found {len(divs)} quotes on the page.")

# First quote
quote_div = divs[0]
# print(divs[0].get_attribute("outerHTML"))
quote = quote_div.find_element(By.CSS_SELECTOR, "span.text")
print(quote.text)
# len(divs) quotes on the page
assert len(divs) > 0 # a test in python, doesn't affect the output, ensure the output is as you want it
assert len(divs) == 10

# Get tags
tags = quote_div.find_elements(By.CSS_SELECTOR, "div.tags a.tag")
tags[0].text # first tag

# the next for loop is one line above (a mapping)
for tag in tags:
    print(tag.text)

# [tag.text for tag in tags]
# list comprehension
# a quick way to make a list

def changeText(text):
    return text + "|"

# map(changeText, [tag.text for tag in tags])


result = []

for quote_div in divs:
    entry = {
        "quote": quote_div.find_element(By.CSS_SELECTOR, "span.text").text,
        "by": quote_div.find_element(By.CSS_SELECTOR, "span small.author").text, # add span small to ensure that it is this quote's author
        "tags": [tag.text for tag in quote_div.find_elements(By.CSS_SELECTOR, "div.tags a.tag")]
    }
    result.append(entry)

# Save the result to a JSON file
with open("quotes.json", "w") as f:
    json.dump(result, f, indent=4)

driver.close() # close the browser
