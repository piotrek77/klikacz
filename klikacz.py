from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Konfiguracja Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Uruchamianie w trybie bez interfejsu graficznego (opcjonalne)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

#do ChromeDriver
driver_path = "d:/Programy/chromedriver/chromedriver.exe" 



def kliknij_przycisk():
    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
    try:
        driver.get("https://nakarmpsa.olx.pl/")


        przycisk = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.CSS_SELECTOR, ".single-pet-control-feed_button > span"))  )
        
##        przycisk = driver.find_element(By.XPATH, "//button[contains(text(), 'Nakarm psa')]")
        przycisk.click()
        print("click")
    except Exception as e:
        print(f"Blad: {e}")
    finally:
        time.sleep(1)
        driver.quit()


while True:
    kliknij_przycisk()
    time.sleep(6)  # Czekaj 

