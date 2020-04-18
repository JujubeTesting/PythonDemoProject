import unittest

class MyTestCase(unittest.TestCase):
    def test_case1(self):
        print("Executed testcase3-case1 ffrom demo2 package")
        self.assertEqual(True, True)

    def test_case2(self):
        print("Executed testcase3-case2 ffrom demo2 package")
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
