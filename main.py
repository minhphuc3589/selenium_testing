import unittest

from unit_test import TestUnit

if __name__ == "__main__":
    suite = unittest.TestSuite()

    #################### Staff Test ####################
    suite.addTest(TestUnit("test_login", "", "http://localhost:8080/NaikiStore/dashboard", others={
        "id": {
            "account": "email",
            "password": "password",
            "login_button": "loginButton"
        },
        "credentials": {
            "account": "staffu@naikistore.com",
            "password": "Huhu123@",
            "role": "STAFF"
        },
        "url": {
            "login": "http://localhost:8080/NaikiStore/login"
        }
    }))

    suite.addTest(TestUnit("test_link_with_login", "http://localhost:8080/NaikiStore/", "http://localhost:8080/NaikiStore/", others={
        "id": {
            "account": "email",
            "password": "password",
            "login_button": "loginButton",
        },
        "credentials": {
            "account": "staffu@naikistore.com",
            "password": "Huhu123@",
            "role": "STAFF"
        },
        "url": {
            "login": "http://localhost:8080/NaikiStore/login"
        }
    }))

    suite.addTest(TestUnit("test_link_with_login", "http://localhost:8080/NaikiStore/cart", "http://localhost:8080/NaikiStore/login", others={
        "id": {
            "account": "email",
            "password": "password",
            "login_button": "loginButton",
        },
        "credentials": {
            "account": "staffu@naikistore.com",
            "password": "Huhu123@",
            "role": "STAFF"
        },
        "url": {
            "login": "http://localhost:8080/NaikiStore/login"
        }
    }))

    suite.addTest(TestUnit("test_link_with_login", "http://localhost:8080/NaikiStore/order", "http://localhost:8080/NaikiStore/login", others={
        "id": {
            "account": "email",
            "password": "password",
            "login_button": "loginButton",
        },
        "credentials": {
            "account": "staffu@naikistore.com",
            "password": "Huhu123@",
            "role": "STAFF"
        },
        "url": {
            "login": "http://localhost:8080/NaikiStore/login"
        }
    }))

    #################### Customer Test ####################
    suite.addTest(TestUnit("test_login", "", "http://localhost:8080/NaikiStore/home", others={
        "id": {
            "account": "email",
            "password": "password",
            "login_button": "loginButton"
        },
        "credentials": {
            "account": "minhphuc3589@gmail.com",
            "password": "uw9RDvHx",
            "role": "CUSTOMER"
        },
        "url": {
            "login": "http://localhost:8080/NaikiStore/login"
        }
    }))

    suite.addTest(TestUnit("test_link_with_login", "http://localhost:8080/NaikiStore/dashboard", "http://localhost:8080/NaikiStore/login", others={
        "id": {
            "account": "email",
            "password": "password",
            "login_button": "loginButton",
        },
        "credentials": {
            "account": "minhphuc3589@gmail.com",
            "password": "uw9RDvHx",
            "role": "CUSTOMER"
        },
        "url": {
            "login": "http://localhost:8080/NaikiStore/login"
        }
    }))

    #################### Guest Test ####################
    suite.addTest(TestUnit("test_link_without_login", "http://localhost:8080/NaikiStore/myvouchers", "http://localhost:8080/NaikiStore/myvouchers", others={
        "id": {
            "account": "email",
            "password": "password",
            "login_button": "loginButton",
        },
        "credentials": {
            "account": "minhphuc3589@gmail.com",
            "password": "uw9RDvHx"
        },
        "url": {
            "login": "http://localhost:8080/NaikiStore/login"
        }
    }))


    runner = unittest.TextTestRunner()
    runner.run(suite)