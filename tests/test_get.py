import unittest


class TestFunction(unittest.TestCase):
    def test_get_element(self):
        self.assertEqual('foo', 'foo')


if __name__ == '__main__':
    unittest.main()
