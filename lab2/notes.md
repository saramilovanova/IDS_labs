#### Selenium

- It was developed for testing

- a driver is used for the browser (chrome)

https://toscrape.com/

1. Find how the page is organized (dev tools -> elements)
2. Right-click on the class, for ex., and copy xpath or css selector

Examples:

*xpath*: /html/body/div/div[2]/div[1]/div[1]

*selector*: body > div > div:nth-child(2) > div.col-md-8 > div:nth-child(1)

- The selector is a bit better, it looks like:

`div.quote` (for the `By.CSS_SELECTOR`)

- Also `(By.TAG_NAME, "div")` is possible

- When working with selenium, always working with drivers

- Consider using `time.sleep(2)` to wait for the page to load
- `driver.quit()` to close the browser


https://www.w3schools.com/cssref/css_selectors.php for the selector elements

- Selenium returns a list of objects

- In tags, anchor = link

- `find_element` vs `find_elements` -> the first one returns the first element, the second one returns a list of elements

- When there is a next button down the page, it is possible to click on it and scrape the next page

- There is infinite scroll option -> terrible for scraping; 

- Ads -> not static -> not good for scraping

- Disable caching; go incognito; disable popups; 

- Mobile mode also possible