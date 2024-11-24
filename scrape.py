import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import WebDriverException
import time

def scrape_website(url):
    """Scrapes the content of a website and returns the HTML source or an error message."""
    print("Scraping website...", url)

    firefox_driver_path = "/home/abdullahalazmi/Downloads/web_scrapping/geckodriver-v0.35.0-linux64/geckodriver"

    firefox_binary_path = "/usr/lib64/firefox/firefox"

    options = webdriver.FirefoxOptions()
    options.binary_location = firefox_binary_path
    options.add_argument("--headless")  # Run in headless mode (optional for running without UI)

    try:
        driver = webdriver.Firefox(service=Service(firefox_driver_path), options=options)

        driver.set_page_load_timeout(30)

        driver.get(url)
        print("Website loaded successfully!")

        html = driver.page_source

        time.sleep(5)

        return html

    except WebDriverException as e:
        error_message = f"Error occurred: {str(e)}"
        print(error_message)
        return error_message

    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        print(error_message)
        return error_message

    finally:
        try:
            driver.quit()
        except:
            pass
