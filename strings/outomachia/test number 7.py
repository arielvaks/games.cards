from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from strings.outomachia.Adve_def import main_page ,cart_page,category_page ,product_page
import unittest
class testnumber1(unittest.TestCase):
    def testnumber7(self):
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

        #go back to the tablets page
        testnum4.go_back_to_tablets()

        #check that we came back to the tablet page
        self.assertEqual(testnum1.get_page_catagory().text,"TABLETS")

        #go back to the main page
        testnum1.go_back_to_mainpage()

        # check that we came back to the main page
        self.assertEqual(driver.current_url,"http://advantageonlineshopping.com/#/")


if __name__ == '__main__':
    unittest.main()