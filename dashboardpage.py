from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):
    # Define the locators for dashboard
    DASHBOARD_HEADER = (By.ID, "dashboard-header")

    def get_dashboard_header_text(self):
        return self.find_element(*self.DASHBOARD_HEADER).text

    def edit:
     return s
