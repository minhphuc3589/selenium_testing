from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestUnit(unittest.TestCase):
    def setUp(self, method, original_url, expected_url, others):
        # Khởi tạo Chrome (cần cài chromedriver)
        super().__init__(method)
        self.driver = webdriver.Chrome()
        self.original_url = original_url
        self.expected_url = expected_url
        self.others = others
        
    def login(self) -> webdriver.Chrome:
        driver: webdriver.Chrome = self.driver
        driver.get(self.original_url)

        driver.find_element(By.ID, self.others.id.username).send_keys(self.others.value.username)
        driver.find_element(By.ID, self.others.id.password).send_keys(self.others.value.password)
        driver.find_element(By.ID, self.others.id.button).click()

        time.sleep(2)
        
        return driver

    def test_login(self) -> None:
        driver: webdriver.Chrome = self.login()
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
        
    def test_link_with_login(self) -> None:
        pass
        
    def test_link_without_login(self) -> None:
        driver: webdriver.Chrome = self.driver
        driver.get(self.original_url)
        
        driver.find_element(By.ID, self.others.id.link).click()
        
        time.sleep(2)
        
        actual_url = driver.current_url
        self.assertEqual(
            actual_url,
            self.expected_url,
            f"""
            =>>> URL không khớp sau khi chuyển hướng Link!
            URL thực tế sau khi login: {actual_url}
            URL mong muốn sau khi login: {self.expected_url}
            """
        )

    def tearDown(self):
        # Đóng trình duyệt sau khi test xong
        self.driver.quit()

