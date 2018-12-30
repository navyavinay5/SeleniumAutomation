from framework.base.Selenium_driver import SeleniumDriver

class ProductListPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _product="(//h2)[5]"


    def goToPLP(self):
        self.elementClick(self._product, "xpath")