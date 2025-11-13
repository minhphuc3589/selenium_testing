import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestUnit(unittest.TestCase):
    def __init__(self, methodName: str, original_url: str, expected_url: str, others: dict):
        super().__init__(methodName)
        self.original_url = original_url
        self.expected_url = expected_url
        self.others = others

        self.custom_status = {
            "status": None,
            "message": ""
        }

        with open("test_report.log", "a") as f:
            f.write(f"Initializing test case: {methodName}\n")
            f.write(f"Original URL: {original_url}\n")
            f.write(f"Expected URL: {expected_url}\n")
            f.write("\n"*2)

    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def login(self) -> webdriver.Chrome:
        driver = self.driver
        driver.get(self.others.get("url", {}).get("login", "http://localhost:8080/NaikiStore/login"))

        driver.find_element(By.ID, self.others.get("id", {}).get("account", "username")).send_keys(self.others.get("credentials", {}).get("account", ""))
        driver.find_element(By.ID, self.others.get("id", {}).get("password", "password")).send_keys(self.others.get("credentials", {}).get("password", ""))
        driver.find_element(By.ID, self.others.get("id", {}).get("login_button", "loginButton")).click()

        time.sleep(2)

        return driver

    def test_login(self) -> None:
        driver = self.login()

        actual_url = driver.current_url

        try:
            self.assertEqual(
                actual_url,
                self.expected_url,
                f"""
                =>>> URL is not correct after Login!
                The real URL after Login: {actual_url}
                The expected URL after login: {self.expected_url}
                """
            )


            with open("test_report.log", "a") as f:
                f.write("TEST PASSED:\n")
                f.write(f"URL after login is correct: {actual_url}\n")
                f.write("-"*100 + "\n"*2)

        except AssertionError as e:
            with open("test_report.log", "a") as f:
                f.write(f"TEST FAILED:\n")
                f.write(f"{str(e)}\n")
                f.write("-"*100 + "\n"*2)

    def test_link_with_login(self) -> None:
        driver = self.login()
        
        driver.get(self.original_url)

        driver.find_element(By.ID, self.others.get("id", {}).get("link", "")).click()

        actual_url = driver.current_url

        try:
            self.assertEqual(
                actual_url,
                self.expected_url,
                f"""
                =>>> URL is not correct after Login!
                The real URL after Login: {actual_url}
                The expected URL after login: {self.expected_url}
                """
            )

            with open("test_report.log", "a") as f:
                f.write("TEST PASSED:\n")
                f.write(f"URL after login is correct: {actual_url}\n")
                f.write("-"*100 + "\n"*2)

        except AssertionError as e:
            with open("test_report.log", "a") as f:
                f.write(f"TEST FAILED:\n")
                f.write(f"{str(e)}\n")
                f.write("-"*100 + "\n"*2)


    def test_link_without_login(self) -> None:
        driver = self.driver
        driver.get(self.original_url)

        driver.find_element(By.ID, self.others.get("id", {}).get("link", "")).click()

        actual_url = driver.current_url


        try:
            self.assertNotEqual(
                actual_url,
                self.expected_url,
                f"""
                =>>> URL is not correct!
                The real URL without Login: {actual_url}
                The expected URL without login: {self.expected_url}
                """
            )

            with open("test_report.log", "a") as f:
                f.write("TEST PASSED:\n")
                f.write(f"URL without login is correct: {actual_url}\n")
                f.write("-"*100 + "\n"*2)

        except AssertionError as e:
            with open("test_report.log", "a") as f:
                f.write(f"TEST FAILED:\n")
                f.write(f"{str(e)}\n")
                f.write("-"*100 + "\n"*2)

    def tearDown(self):
        self.driver.quit()