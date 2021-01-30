from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from strings.outomachia.Adve_def import main_page ,cart_page,category_page , product_page ,new_user,payment
import unittest
class testnumber8(unittest.TestCase):
    def testnumber8(self):
        driver = webdriver.Firefox(executable_path=r"C:\Users\Pasha\Documents\ariel vaks\geckodriver.exe")

        driver.implicitly_wait(10)
        driver.get("http://advantageonlineshopping.com/#/")
        driver.maximize_window()

        testnum2 = main_page(driver)
        testnum3 = cart_page(driver)
        testnum1 = category_page(driver)
        testnum4 = product_page(driver)
        testnum5= new_user(driver)
        testnum6 = payment(driver)

        # go to tablets

        testnum2.tablets()


        # click on the "HP ELITE X2 1011 G1 TABLET"

        # # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[id='17']")))
        # testnum1.HP_ELITE_X2_1011_G1_TABLET()
        #
        #
        #
        # # click on the "HP ELITE X2 1011 G1 TABLET"
        # testnum4.plus()
        #
        # #click on "add to cart"
        # testnum4.add_to_cart()
        #
        # #go to home page
        # testnum3.go_home_page()

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


        #go to cart page
        testnum2.shopping_cart()

        #click checkout

        testnum3.checkout()

        #clicl register

        testnum3.register()

        #write "ariel" in firt name
        testnum5.user_name()
        testnum5.password()
        testnum5.email()
        testnum5.confirm_password()
        testnum5.agree()
        testnum5.register()

        #press next
        testnum6.next()


        #write detailes of username and password
        testnum6.user_name()
        testnum6.password()

        testnum6.paynow()
        #go back to shopping cart
        testnum2.shopping_cart()


        self.assertEqual(testnum3.empty_shopping_cart(),"Your shopping cart is empty")



if __name__ == '__main__':
    unittest.main()