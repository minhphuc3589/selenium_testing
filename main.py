import unittest

from unit_test import TestUnit

if __name__ == "__main__":
    suite = unittest.TestSuite()

    # Staff User Login Test
    suite.addTest(TestUnit("test_login", "", "http://localhost:8080/NaikiStore/dashboard", others={
        "id": {
            "account": "email",
            "password": "password",
            "login_button": "loginButton"
        },
        "credentials": {
            "account": "staffu@naikistore.com",
            "password": "Huhu123@"
        },
        "url": {
            "login": "http://localhost:8080/NaikiStore/login"
        }
    }))

    suite.addTest(TestUnit("test_link_with_login", "http://localhost:8080/NaikiStore/home", "http://localhost:8080/NaikiStore/dashboard", others={
        "id": {
            "account": "email",
            "password": "password",
            "login_button": "loginButton",
        },
        "credentials": {
            "account": "staffu@naikistore.com",
            "password": "Huhu123@"
        },
        "url": {
            "login": "http://localhost:8080/NaikiStore/login"
        }
    }))

    suite.addTest(TestUnit("test_link_with_login", "", "http://localhost:8080/NaikiStore/dashboard", others={
        "id": {
            "account": "email",
            "password": "password",
            "login_button": "loginButton",
        },
        "credentials": {
            "account": "staffu@naikistore.com",
            "password": "Huhu123@"
        },
        "url": {
            "login": "http://localhost:8080/NaikiStore/login"
        }
    }))


    runner = unittest.TextTestRunner()
    runner.run(suite)