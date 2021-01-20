from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from strings.outomachia.Adve_def import main_page ,cart_page,category_page , product_page
import unittest
class testnumber1(unittest.TestCase):
    def testnumber2(self):
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



        print(testnum3.list_of_colors()[0].get_attribute("title"))

        # self.assertEqual(testnum3.list_of_items()[0].text,"1")
        # self.assertEqual(testnum3.list_of_items()[1].text,"3")
        # self.assertEqual(testnum3.list_of_items()[2].text,"2")
        # self.assertEqual(testnum3.list_of_colors()[0].get_attribute("title"),"GRAY")
        # self.assertEqual(testnum3.list_of_colors()[1].get_attribute("title"),"TURQUOISE")
        # self.assertEqual(testnum3.list_of_colors()[2].get_attribute("title"),"BLACK")
        self.assertEqual(testnum3.how_many_tablets2().text, "QTY: 2")
        self.assertEqual(testnum3.how_many_speakers2().text, "QTY: 3")
        self.assertEqual(testnum3.how_many_mouses().text, "QTY: 1")
        self.assertEqual(testnum3.color_number_one().text, "Color: WHITE")
        self.assertEqual(testnum3.color_number_two().text, "TURQUOISE")
        self.assertEqual(testnum3.name_of_first_item().text, "HP Z3200 WIRELESS MOUSE")
        self.assertEqual(testnum3.name_of_second_item().text, "BOSE SOUNDLINK WIRELESS SPE...")
        self.assertEqual(testnum3.name_of_third_item().text, "HP ELITE X2 1011 G1 TABLET")
        self.assertEqual(testnum3.price_of_first_item_pop_up_window().text,"$29.99")
        self.assertEqual(testnum3.price_of_second_item_pop_up_window().text,"$387.00")
        self.assertEqual(testnum3.price_of_third_item_pop_up_window().text, "$2,558.00")



if __name__ == '__main__':
    unittest.main()



