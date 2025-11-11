import unittest

from unit_test import TestUnit

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestUnit("test_login", "http://localhost:8080/NaikiStore/login", "http://localhost:8080/NaikiStore/dashboard"))

    runner = unittest.TextTestRunner()
    runner.run(suite)