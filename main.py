import unittest

from unit_test import TestUnit

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestUnit("test_login", "https://example.com"))

    runner = unittest.TextTestRunner()
    runner.run(suite)