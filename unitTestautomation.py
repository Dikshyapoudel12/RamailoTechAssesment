import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class myFrirstAutomation(unittest.TestCase):
    def setUp(self):
        s = ChromeService(ChromeDriverManager().install())  # it will install driver at runtime
        self.driver = webdriver.Chrome(service=s)  # it will initialize browser
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def loginTest(self):
        self.driver.get("https://esg.idea2mvp.in/")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("deekshyap@gmail.com")
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Dikshya1590!")
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//div[@class="bg-white p-6 rounded-xl shadow-2xl"]')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//button[@class="border-none py-2 text-base font-medium w-full  text-white bg-[#F73232] text-center cursor-pointer block px-2 py-2 rounded-md "]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//a[@class="text-[#5D3587] underline font-semibold"]').click()
        time.sleep(2)

    def signupTest(self):
        self.driver.get("https://esg.idea2mvp.in/")
        self.driver.find_element(By.XPATH, '//a[@class="text-[#5D3587] underline font-semibold"]').click()
        acutal_slogan = self.driver.find_element(By.XPATH, '//p[contains(text(),"enjoy the features")]').text
        expected_slogan = "Sign up to enjoy the features"
        self.assertEqual(acutal_slogan, expected_slogan)
        time.sleep(2)
        first_name = self.driver.find_element(By.XPATH, '//input[@name="user.first_name"]')
        first_name.send_keys("Dikshya")
        last_name = self.driver.find_element(By.XPATH, '//input[@name="user.last_name"]')
        last_name.send_keys("Poudel")
        company_name = self.driver.find_element(By.XPATH, '//input[@name="company_name"]')
        company_name.send_keys("ABC")
        user_email = self.driver.find_element(By.XPATH, '//input[@name="user_email"]')
        user_email.send_keys("dikshyap480@gmail.com")
        user_password = self.driver.find_element(By.XPATH, '//input[@name="user_password"]')
        user_password.send_keys("Abc1590!")
        organization_type = self.driver.find_element(By.XPATH, '//div[contains(@aria-labelledby,"organization_sector")]')
        Select(organization_type).select_by_visible_text("Services")
        organization_location = self.driver.find_element(By.XPATH, '//div[contains(@aria-labelledby,"organization_based")]')
        Select(organization_location).select_by_visible_text("Nepal")
        employee_number = self.driver.find_element(By.XPATH, '//div[contains(@aria-labelledby,"no_of_employees")]')
        Select(employee_number).select_by_visible_text("25-50")
        terms_and_condition = self.driver.find_element(By.XPATH,'//input[contains(@data-indeterminate,"false") and contains(@type, "check")]')
        terms_and_condition.click()
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(2)






if __name__ == '__main__':  # mathiko unittest lai call gareko
    unittest.main()