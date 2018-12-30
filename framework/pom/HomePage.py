from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.common.action_chains import ActionChains



class HomePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _departs="//a[@id='nav-link-shopall']//span[@class='nav-line-2']"
    _artsAndCrafts="//div[@id='nav-flyout-shopAll']//span[text()='Arts & Crafts']"

    def goToHp(self):
        dept=self.getElement(self._departs,"xpath")
        actions=ActionChains(self.driver)
        actions.move_to_element(dept).perform()

        self.elementClick(self._artsAndCrafts, "xpath")


