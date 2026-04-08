from playwright.sync_api import Page, expect, TimeoutError

# Page Object Model class for Login Page
class LoginPage:
    # Constructor to initialize page and locators
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://v2.zenclass.in/login" # Application URL
        # Locators
        self.username = "//input[@placeholder='Enter your mail']"
        self.password = "//input[@placeholder='Enter your password ']"
        self.lgn_btn = "//button[@type='submit']"
        self.drop_down_dash ="//img[@id='profile-click-icon']"
        self.logout_btn = "//div[contains(text(),'Log out')]"
        self.close_popup_btn = "//button[@aria-label='Close popup']" #Popup locator if anything appears

    # Navigate to login page
    def navigate(self):
        try:
            self.page.goto(self.url)
        except Exception as e:
            print("Navigation Failed:", e)

    # Perform login action
    def login(self, user, pwd):
        try:
            self.page.fill(self.username, user)
            self.page.fill(self.password, pwd)
            self.page.click(self.lgn_btn)
        except TimeoutError:
            print("Login elements not found")

    #perform logout
    def logout(self, user, pwd):
        try:
            self.page.fill(self.username, user)
            self.page.fill(self.password, pwd)
            self.page.click(self.lgn_btn)
            self.page.click(self.close_popup_btn)
            self.page.click(self.drop_down_dash)
            self.page.click(self.logout_btn)
        except TimeoutError:
            print("Logout failed")
    #verify login
    def verify_dashboard(self):
        from playwright.sync_api import expect
        expect(self.page.locator("text=dashboard")).to_be_visible()
    #verify error message
    def verify_log_case(self):
        from playwright.sync_api import expect
        expect(self.page.locator("text=login")).to_be_visible()
