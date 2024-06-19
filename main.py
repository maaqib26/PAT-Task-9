from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Swag_Labs:
    # username & password data
    username = "standard_user"
    password = "secret_sauce"

    # Locators Data

    username_locator = "user-name"
    password_locator = "password"
    login_locator = "login-button"
    web_page_content_locator = "//body"


    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start_automation(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(2)
            return True
        except:
            print("ERROR: Not able to start python automation")
            return FALSE

    def login_webpage(self):
        if self.start_automation():
            try:
                self.driver.find_element(by=By.NAME,value=self.username_locator).send_keys(self.username)
                sleep(2)
                self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
                sleep(2)
                self.driver.find_element(by=By.NAME,value=self.login_locator).click()
                sleep(2)
                return True
            except:
                print("ERROR: Please check the credentials")
                return False
    def fetch_title(self):
        if self.login_webpage():
            return self.driver.title
        else:
            print("ERROR: Not able to fetch the webpage title")
            return False

    def fetch_url(self):
        if self.login_webpage():
            return self.driver.current_url
        else:
            print("ERROR: Not able to fetch the webpage url")
            return False

    def fetch_web_content(self):
        if self.login_webpage():
            text_content = self.driver.find_element(by=By.XPATH,value=self.web_page_content_locator).text
            # Save the text content to a text file
            with open("Webpage_task_11.txt", "w") as f:
                f.write(text_content)
        else:
            print("ERROR: Not able to fetch the webpage contents")
            return False

    def shutdown(self):
        self.driver.quit()
        return None

if __name__ == "__main__":
    url = "https://www.saucedemo.com/"
    sauce_labs = Swag_Labs(url)
    print(sauce_labs.start_automation())
    print(sauce_labs.login_webpage())
    print(sauce_labs.fetch_title())
    print(sauce_labs.fetch_url())
    sauce_labs.fetch_web_content()
    sauce_labs.shutdown()