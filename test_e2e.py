import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        time.sleep(2)

        checkOutPage = CheckOutPage(self.driver)
        products = checkOutPage.getCardTitles()
        confirmations = ConfirmPage(self.driver)



        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text

            if productName == "Blackberry":
                checkOutPage.getCardFooter().click()

        # time.sleep(2)
        checkOutPage.pressCheckOut().click()
        confirmations.confirmationCheckOut().click()

        #self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")
        confirmations.enterText().send_keys("ind")

        time.sleep(5)
        #self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmations.selectIndia().click()

        #self.driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
        confirmations.checkingAgreeBox().click()

        #self.driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
        confirmations.purchaseButton().click()



        assert confirmations.succesTextDisplayed().is_displayed()
        print("modified for github purposes in GitDemo")


        #self.driver.find_element(By.CSS_SELECTOR, "a[aria-label='close']").click()
        confirmations.closeButton().click()