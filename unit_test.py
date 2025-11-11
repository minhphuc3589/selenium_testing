import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestUnit(unittest.TestCase):
    def __init__(self, methodName: str, original_url: str, expected_url: str):
        super().__init__(methodName)
        self.original_url = original_url
        self.expected_url = expected_url

    def setUp(self):
        # Khởi tạo Chrome
        self.driver = webdriver.Chrome()
        
    def login(self) -> webdriver.Chrome:
        driver = self.driver
        driver.get(self.original_url)

        driver.find_element(By.ID, "email").send_keys("staffu@naikistore.com")
        driver.find_element(By.ID, "password").send_keys("123456")
        driver.find_element(By.ID, "loginButton").click()

        time.sleep(2)
        return driver

    def test_login(self):
        driver = self.login()
        actual_url = driver.current_url
        self.assertEqual(
            actual_url,
            self.expected_url,
            f"""
            =>>> URL không khớp sau khi Login!
            URL thực tế sau khi login: {actual_url}
            URL mong muốn sau khi login: {self.expected_url}
            """
        )

    def tearDown(self):
        self.driver.quit()