from selenium import webdriver
from selenium.webdriver.common.by import By

givenTestData = ["NFLX", "MSFT", "TSLA"]
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/finance/")
elementsXpath = "//section[@aria-labelledby='smart-watchlist-title']//div[contains(@class, 'COaKTb')]"
stocks = driver.find_elements(By.XPATH, elementsXpath)
q3 = []
q4 = []
assertion_results = []
for stock in stocks:
    if stock not in givenTestData:
        q3.append(stock.text)

for testStock in givenTestData:
    if testStock not in stocks:
        q4.append(testStock)

pageTitle = driver.title

try:
    try:
        assert 'Google Finance' in pageTitle
    except AssertionError as e:
        assertion_results.append(f"Assertion failed for page title: {str(e)}")
    try:
        for testStock in givenTestData:
            for stock in stocks:
                assert stock.text == testStock
    except AssertionError as e:
        assertion_results.append(f"Assertion failed for the two list: {str(e)}")

finally:
    # Print all assertion results after the test completes
    for result in assertion_results:
        print(result)

print(q3)
print(q4)
