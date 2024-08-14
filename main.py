from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

givenTestData = ["NFLX", "MSFT", "TSLA"]
service = Service(executable_path="/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get("https://www.google.com/finance/")
elementsXpath = "//section[@aria-labelledby='smart-watchlist-title']//div[contains(@class, 'COaKTb')]"
stocks = driver.find_elements(By.XPATH, elementsXpath)
q3 = []
q4 = []
assertion_results = []


def test_notInTestDataTest():
    for stock in stocks:
        if stock not in givenTestData:
            q3.append(stock.text)
    print(q3)


def test_inTestDataTest():
    for testStock in givenTestData:
        if testStock not in stocks:
            q4.append(testStock)
    print(q4)


pageTitle = driver.title


def test_titleTest():
    try:
        assert "Google Finance" in pageTitle
    except AssertionError as e:
        assertion_results.append(f"Assertion failed for page title: {str(e)}")


def test_stockCopmare():
    try:
        for testStock in givenTestData:
            for stock in stocks:
                assert stock.text == testStock
    except AssertionError as e:
        assertion_results.append(f"Assertion failed for the two list: {str(e)}")
