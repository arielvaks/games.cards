from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from strings.outomachia.Adve_def import main_page ,cart_page,category_page,product_page
import unittest

class testnumber1(unittest.TestCase):
    def test_search_in_python_org(self):
        driver = webdriver.Firefox(executable_path=r"C:\Users\Pasha\Documents\ariel vaks\geckodriver.exe")

        driver.implicitly_wait(10)
        driver.get("http://advantageonlineshopping.com/#/")
        driver.maximize_window()

        testnum1 = main_page(driver)
        testnum2 = cart_page(driver)
        testnum3 = category_page(driver)
        testnum4 = product_page(driver)

        # go to tablets

        testnum1.tablets()


        # click on the "HP ELITE X2 1011 G1 TABLET"

        testnum3.HP_ELITE_X2_1011_G1_TABLET()

        # click on the "HP ELITE X2 1011 G1 TABLET"
        testnum4.plus()

        #click on "add to cart"
        testnum4.add_to_cart()

        #go to home page
        testnum2.go_home_page()

        # go to speakers
        testnum1.go_speakers()

        # go to bose speaker
        testnum3.bose_sound()

        # add three times
        testnum4.plus()
        testnum4.plus()

        #add to cart
        testnum4.add_to_cart()

        # testnum2.how_many_tablets().text=="QTY: 3"
        # testnum2.how_many_speakers().text== "QTY: 2"


        self.assertEqual(testnum2.how_many_tablets().text,"QTY: 3")
        self.assertEqual(testnum2.how_many_speakers().text, "QTY: 2")

if __name__ == '__main__':
    unittest.main()

# a = PythonOrgSearch()
# a.test_search_in_python_org()



