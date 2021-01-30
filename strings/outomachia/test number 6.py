from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from strings.outomachia.Adve_def import main_page ,cart_page,category_page , product_page
import unittest
import time
class testnumber6(unittest.TestCase):
    def testnumber6(self):
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
        driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")


        # click on the "HP ELITE X2 1011 G1 TABLET"

        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[id='17']")))
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

        #go to home

        testnum3.go_home_page()

        #go to mices

        testnum2.go_mices()

        #go to HP_Z3200_Wireless_Mouse
        testnum1.HP_Z3200_Wireless_Mouse()

        #pick the color white
        testnum4.pick_the_color_white()

        #add to cart
        testnum4.add_to_cart()

        # go to shopping cart
        testnum2.shopping_cart()

        #edit product number 1


        ActionChains(driver).click(testnum3.edit_product()[0]).perform()


        #add 1 to the Quantity of the first product

        testnum4.plus()
        testnum4.add_to_cart()




        # edit product number 2
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "ul.roboto-light > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > tool-tip-cart:nth-child(1) > div:nth-child(1) > table:nth-child(2) > tfoot:nth-child(2) > tr:nth-child(2) > td:nth-child(1) > button:nth-child(1)")))
        ActionChains(driver).click(testnum3.edit_product()[1]).perform()

        # add 1 to the Quantity of the second product

        testnum4.plus()
        testnum4.add_to_cart()


        self.assertEqual(testnum3.how_many_mouses().text,"QTY: 2")
        self.assertEqual(testnum3.how_many_speakers2().text, "QTY: 4")

if __name__ == '__main__':
    unittest.main()

