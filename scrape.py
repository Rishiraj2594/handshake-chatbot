from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_top_links(search_query, num_links=5):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options)

    driver.get(f"https://hnssearch.io/search?s={search_query}")
    time.sleep(4)  # Wait for the page to load (you might replace this with WebDriverWait)
    searchs = driver.find_element(By.ID, 'root')

    links = searchs.find_elements(By.CSS_SELECTOR, ".text-lg.text-blue-800.font-bold.dark\\:text-blue-400")
    top_links = [link.get_attribute('href') for link in links[:num_links]]

    driver.close()
    return top_links

