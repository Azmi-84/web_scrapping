import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import WebDriverException
import time

def scrape_website(url):
    """Scrapes the content of a website and returns the HTML source or an error message."""
    print("Scraping website...", url)

    geckodriver_path = "/home/abdullahalazmi/Downloads/web_scrapping/geckodriver"

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")

    try:
        driver = webdriver.Firefox(service=Service(geckodriver_path), options=options)

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
