import pytest
from pages.login_page import LoginPage

#positive test to login successful
def test_success_login(page):
    lp = LoginPage(page)
    lp.navigate()
    lp.login("", "")
    lp.verify_dashboard()
#negative test case wrong username
def test_failure_login(page):
    lp = LoginPage(page)
    lp.navigate()
    lp.login("drajjsdfn@gmail.com", "password")
    lp.verify_log_case()
#positive case check username and password field visible
def test_input_field(page):
    lp = LoginPage(page)
    lp.navigate()
    assert page.locator(lp.username).is_visible()
    assert page.locator(lp.password).is_visible()
#positive cases check login button enabled
def test_submit_button(page):
    lp = LoginPage(page)
    lp.navigate()
    assert page.locator(lp.lgn_btn).is_enabled()
#positive test case checks logout successful
def test_logout(page):
    lp = LoginPage(page)
    lp.navigate()
    lp.logout("", "")
    lp.verify_log_case()