from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from strings.outomachia.Adve_def import main_page ,cart_page,category_page ,product_page
import time
import unittest
class testnumber1(unittest.TestCase):
    def testnumber4(self):
        driver = webdriver.Firefox(executable_path=r"C:\Users\Pasha\Documents\ariel vaks\geckodriver.exe")

        driver.implicitly_wait(10)
        driver.get("http://advantageonlineshopping.com/#/")
        driver.maximize_window()

        testnum2 = main_page(driver)
        testnum3 = cart_page(driver)
        testnum1 = category_page(driver)
        testnum4 = product_page(driver)

        # go to tablets

        testnum2.tablets()


        # click on the "HP ELITE X2 1011 G1 TABLET"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[id='17']")))
        testnum1.HP_ELITE_X2_1011_G1_TABLET()



        # click on the "HP ELITE X2 1011 G1 TABLET"
        testnum4.plus()

        #click on "add to cart"
        testnum4.add_to_cart()

        #go to home page
        testnum3.go_home_page()

        # go to speakers
        testnum2.go_speakers()

        # go to bose speaker
        testnum1.bose_sound()

        # add three times
        testnum4.plus()
        testnum4.plus()

        #add to cart
        testnum4.add_to_cart()


        #go to shopping cart
        testnum2.shopping_cart()
        # time.sleep(2)


        self.assertEqual(testnum3.label_of_shopping_cart().text,"SHOPPING CART")


if __name__ == '__main__':
    unittest.main()





