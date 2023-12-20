''' this module is used to handle locators of the page like findelement and findelements and also syncronization issues like implicity wait and explicity waits 
this module contain the functions of webdriver and webdriver wait'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basepage():
    __TIMEOUT = 30 
    def __init__(self,browser) :
        self.browser = browser
        self.webdriver_wait = WebDriverWait(self.browser,Basepage.__TIMEOUT)

    def visit_url(self,url):
        self.browser.get(url)
        self.browser.maximize_window()

    def find_element_by_locator(self,locator):
        return self.webdriver_wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements_by_locator(self,locator):
        return self.webdriver_wait.until(EC.visibility_of_all_elements_located(locator))
    
    def close_browser(self):
        return self.browser.close()
    
    def quit_browser(self):
        return self.browser.quit()
    
    def get_tittle(self):
        return self.browser.title