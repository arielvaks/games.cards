from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class main_page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
    def tablets (self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='tabletsImg']")))
        try:
            a = self.driver.find_element_by_css_selector("div[id='tabletsImg']")

            return ActionChains(self.driver).click(a).perform()
        except:
            self.driver.find_element_by_css_selector("div[id='tabletsImg']").click()


    def go_speakers(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id='speakersTxt']")))
        try:
            a = self.driver.find_element_by_css_selector("span[id='speakersTxt']")

            return ActionChains(self.driver).click(a).perform()
        except:
            self.driver.find_element_by_css_selector("span[id='speakersTxt']").click()
    def shopping_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[id='shoppingCartLink']")))
        try:
            a = self.driver.find_element_by_css_selector("a[id='shoppingCartLink']")

            return ActionChains(self.driver).click(a).perform()
        except:
            self.driver.find_element_by_css_selector("a[id='shoppingCartLink']").click()
    def go_mices(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id='miceTxt']")))
        try:
            a = self.driver.find_element_by_css_selector("span[id='miceTxt']")

            return ActionChains(self.driver).click(a).perform()
        except:
            self.driver.find_element_by_css_selector("span[id='miceTxt']").click()

    def delete_first_item(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "tr.ng-scope:nth-child(1) > td:nth-child(3) > div:nth-child(2) > div:nth-child(1)")))
        try:
            a = self.driver.find_element_by_css_selector("tr.ng-scope:nth-child(1) > td:nth-child(3) > div:nth-child(2) > div:nth-child(1)")

            return ActionChains(self.driver).click(a).perform()
        except:
            self.driver.find_element_by_css_selector("tr.ng-scope:nth-child(1) > td:nth-child(3) > div:nth-child(2) > div:nth-child(1)").click()





class cart_page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
    def go_home_page(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a>span[class='roboto-medium ng-binding']")))
        try:
            a = self.driver.find_element_by_css_selector("a>span[class='roboto-medium ng-binding']")


            return ActionChains(self.driver).click(a).perform()
        except:
            self.driver.find_element_by_css_selector("a>span[class='roboto-medium ng-binding']").click()
    def how_many_tablets(self):

        return  self.driver.find_element_by_css_selector("tr.ng-scope:nth-child(1) > td:nth-child(2) > a:nth-child(1) > label:nth-child(2)")

    def how_many_speakers(self):

        return  self.driver.find_element_by_css_selector("ul.roboto-light > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > tool-tip-cart:nth-child(1) > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > a:nth-child(1) > label:nth-child(2)")

    def list_of_items(self):
        return self.driver.find_elements_by_css_selector("td[class ='smollCell quantityMobile']")

    def list_of_colors(self):
        return self.driver.find_elements_by_css_selector("span[class='productColor']")

    def list_of_names(self):
        return self.driver.find_elements_by_css_selector("tr>td>label.roboto-regular")





    def how_many_tablets2(self):

        return  self.driver.find_element_by_css_selector("ul.roboto-light > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > tool-tip-cart:nth-child(1) > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > a:nth-child(1) > label:nth-child(2)")

    def how_many_speakers2(self):

        return  self.driver.find_element_by_css_selector("ul.roboto-light > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > tool-tip-cart:nth-child(1) > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > a:nth-child(1) > label:nth-child(2)")

    def how_many_mouses(self):

        return self.driver.find_element_by_css_selector("ul.roboto-light > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > tool-tip-cart:nth-child(1) > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1) > label:nth-child(2)")

    def color_number_one(self):

        return  self.driver.find_element_by_css_selector("ul.roboto-light > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > tool-tip-cart:nth-child(1) > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1) > label:nth-child(3)")

    def color_number_two(self):

        return  self.driver.find_element_by_css_selector("ul.roboto-light > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > tool-tip-cart:nth-child(1) > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > a:nth-child(1) > label:nth-child(3) > span:nth-child(1)")

    def color_number_three(self):

        return  self.driver.find_element_by_css_selector("ul.roboto-light > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > tool-tip-cart:nth-child(1) > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > a:nth-child(1) > label:nth-child(3) > span:nth-child(1)")

    def name_of_first_item(self):

        return  self.driver.find_element_by_css_selector("ul.roboto-light > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > tool-tip-cart:nth-child(1) > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1) > h3:nth-child(1)")

    def name_of_second_item(self):

        return  self.driver.find_element_by_css_selector("ul.roboto-light > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > tool-tip-cart:nth-child(1) > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > a:nth-child(1) > h3:nth-child(1)")

    def name_of_third_item(self):

        return  self.driver.find_element_by_css_selector("ul.roboto-light > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > tool-tip-cart:nth-child(1) > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > a:nth-child(1) > h3:nth-child(1)")


    def price_of_first_item_pop_up_window(self):

        return self.driver.find_element_by_css_selector("ul.roboto-light > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > tool-tip-cart:nth-child(1) > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(3) > p:nth-child(1)")

    def price_of_second_item_pop_up_window(self):

        return self.driver.find_element_by_css_selector("tr.ng-scope:nth-child(2) > td:nth-child(3) > p:nth-child(1)")

    def price_of_third_item_pop_up_window(self):

        return self.driver.find_element_by_css_selector("ul.roboto-light > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > tool-tip-cart:nth-child(1) > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(3) > p:nth-child(1)")

    def label_of_shopping_cart(self):

        return self.driver.find_element_by_css_selector("div>section>article>nav>a.select")

    def price_of_first_item(self):
        return self.driver.find_element_by_css_selector(".fixedTableEdgeCompatibility > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(6) > p:nth-child(2)")

    def price_of_second_item(self):
        return self.driver.find_element_by_css_selector(".fixedTableEdgeCompatibility > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(6) > p")

    def price_of_third_item(self):
        return self.driver.find_element_by_css_selector(".fixedTableEdgeCompatibility > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(6) > p:nth-child(2)")







class category_page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def HP_ELITE_X2_1011_G1_TABLET (self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[id='17']")))
        try:
            a = self.driver.find_element_by_css_selector("img[id='17']")

            return ActionChains(self.driver).click(a).perform()

        except:
            self.driver.find_element_by_css_selector("img[id='17']").click()


    def HP_Z3200_Wireless_Mouse(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[id='28']")))
        try:
            a = self.driver.find_element_by_css_selector("img[id='28']")

            return ActionChains(self.driver).click(a).perform()
        except:
            self.driver.find_element_by_css_selector("img[id='28']").click()

    def bose_sound(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[id='25']")))
        try:
            a = self.driver.find_element_by_css_selector("img[id='25']")

            return ActionChains(self.driver).click(a).perform()
        except:
            self.driver.find_element_by_css_selector("img[id='25']").click()

    def get_page_catagory(self):

        return self.driver.find_element_by_css_selector(".categoryTitle")
    def go_back_to_mainpage(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='ng-scope']")))
        try:
            a = self.driver.find_element_by_css_selector("a[class='ng-scope']")

            return ActionChains(self.driver).click(a).perform()

        except:
            self.driver.find_element_by_css_selector("a[class='ng-scope']").click()



class product_page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def plus(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='ng-scope']")))
        try:
            a = self.driver.find_element_by_css_selector("div[class='plus']")

            return ActionChains(self.driver).click(a).perform()
        except:
            self.driver.find_element_by_css_selector("a[class='ng-scope']").click()

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='roboto-medium ng-scope']")))
        try:
            a = self.driver.find_element_by_css_selector("button[class='roboto-medium ng-scope']")

            return ActionChains(self.driver).click(a).perform()
        except:
            self.driver.find_element_by_css_selector("button[class='roboto-medium ng-scope']").click()

    def pick_the_color_white(self):

        for i in self.driver.find_elements_by_css_selector("span[id='bunny']"):
            if i.get_attribute("title")=="WHITE":
                return ActionChains(self.driver).click(i).perform()

    def go_back_to_tablets(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body>div>nav>a[class='ng-binding']")))
        try:
            a = self.driver.find_element_by_css_selector("body>div>nav>a[class='ng-binding']")

            return ActionChains(self.driver).click(a).perform()
        except:
            self.driver.find_element_by_css_selector("body>div>nav>a[class='ng-binding']").click()


