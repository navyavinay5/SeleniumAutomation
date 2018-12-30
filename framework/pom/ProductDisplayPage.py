from framework.base.Selenium_driver import SeleniumDriver

class ProductDisplayPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _fabric="//span[text()='FabricGrip']"

    def type(self):
        self.elementClick(self._fabric,"xpath")
