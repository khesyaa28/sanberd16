import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options =Options()
options.add_argument('--ignore-certificate-errors')
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, "/html//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "/html//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "/html//input[@id='login-button']").click()

    def test_failed_login_nulluname(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, "/html//input[@id='user-name']").send_keys("")
        driver.find_element(By.XPATH, "/html//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "/html//input[@id='login-button']").click()
        error_mess = driver.find_element(By.XPATH, "//div[@id='login_button_container']//form//h3").text
        self.assertIn("Epic sadface: Username is required", error_mess)

    def test_failed_login_nullpassword(self):
            driver = self.browser
            driver.get("https://www.saucedemo.com/")
            driver.find_element(By.XPATH, "/html//input[@id='user-name']").send_keys("standard_user")
            driver.find_element(By.XPATH, "/html//input[@id='password']").send_keys("")
            driver.find_element(By.XPATH, "/html//input[@id='login-button']").click()
            error_mess = driver.find_element(By.XPATH, "//div[@id='login_button_container']//form//h3").text
            self.assertIn("Epic sadface: Password is required", error_mess)
    def test_view_product_list(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, "/html//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "/html//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "/html//input[@id='login-button']").click()
        prod_header = driver.find_element(By.XPATH, "//div[@id='header_container']//span[@class='title']")
        self.assertTrue(prod_header)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()