''' This module contain elements details - Loginpage
'''
from selenium.webdriver.common.by import By
from Lib.Utiles.base_page_object import Basepage
from selenium.common.exceptions import NoSuchElementException,TimeoutException

class Loginpage(Basepage):
    
    def __init__(self,browser):
        Basepage.__init__(self,browser)
        self.browser = browser

    Locators_dictionary = {
                        'username_textbox' :(By.ID,"email" ),
                      'password_textbox':(By.ID,'pass'),
                      'Login_button':(By.ID,'u_0_5_p0'),
                      'invalid_linktext':(By.CLASS_NAME,"_9ay7")
       
   }
    
    def username_textbox(self):
       try:
          return self.browser.find_element_by_locator(Loginpage.Locators_dictionary['username_textbox'])
       except(NoSuchElementException,TimeoutException):
        return None
    def password_textbox(self):
        try :
            return self.browser.find_element_by_locator(Loginpage.Locators_dictionary['password_textbox'])
        except(NoSuchElementException,TimeoutException):
            return None
    def Login_button(self):
        try :
            return self.browser.find_element_by_locator(Loginpage.Locators_dictionary['Login_button']).click()
        except:
            return None
    def invalid_linktext(self):
        try:
            return self.browser.find_element_by_locator(Loginpage.Locators_dictionary['invalid_linktext'])
        except(NoSuchElementException,TimeoutException):
             return None




        
        
        

   
      
       
        
    
           



    
