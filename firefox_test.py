from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

geckodriver_path = "/home/abdullahalazmi/Downloads/web_scrapping/geckodriver"

options = Options()
options.binary_location = "/var/lib/flatpak/app/io.gitlab.librewolf-community/x86_64/stable/8d5f03119c548e7cf57dadb8a6df75ac204fb79ea1545450fd9278faed060c61/files/librewolf"
options.add_argument("--headless")  # Optional: Headless mode

try:
    driver = webdriver.Firefox(service=Service(geckodriver_path), options=options)

    driver.get("https://www.google.com")
    print("Title:", driver.title)

except Exception as e:
    print("Error occurred:", str(e))

finally:
    try:
        driver.quit()
    except NameError:
        pass
