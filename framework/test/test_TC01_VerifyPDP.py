from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
from framework.pom.ProductDisplayPage import ProductDisplayPage

import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_login(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.plp=ProductListPage(self.driver)
        self.pdp=ProductDisplayPage(self.driver)

    @pytest.mark.run(order=1)
    def test_HomePage(self):
        self.hp.goToHp()

    @pytest.mark.run(order=2)
    def test_ProductListPage(self):
        self.plp.goToPLP()

    @pytest.mark.run(order=3)
    def test_ProductDisplayPage(self):
        self.pdp.type()