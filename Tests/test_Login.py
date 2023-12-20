from Lib.SitePageFactory.Login_page import Loginpage
import pytest

class Test_login():

    def test_loginpagetittle(self,browser_assignment):
       Fetched_loginpage_title= browser_assignment.get_tittle()
       print("fitched loging page tittle",Fetched_loginpage_title)
       if Fetched_loginpage_title=="Facebook – log in or sign up":
           assert True
       else :
           assert False

    def test_loginpage(self,browser_assignment):
        Loginpage(browser_assignment).username_textbox().send_keys("7794915048")
        Loginpage(browser_assignment).password_textbox().send_keys("Ilovecricket@123#")
        Loginpage(browser_assignment).Login_button()
        login_tittle = browser_assignment.get_tittle()
        print(login_tittle)
        if login_tittle == "Facebook – log in or sign up":
            assert True
        else :
            assert False
    @pytest.mark.regression
    def test_invalid_loginpage(self,browser_assignment):
        Loginpage(browser_assignment).username_textbox().send_keys("77949150481")
        Loginpage(browser_assignment).password_textbox().send_keys("Ilovecricket@123#1")
        Loginpage(browser_assignment).Login_button()
        invalid_message =Loginpage(browser_assignment).invalid_linktext().text
        print(invalid_message)

        # if invalid_message == "The password that you've entered is incorrect. ":
        #     assert True
        # else :
        #     assert False