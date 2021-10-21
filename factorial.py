import unittest
from test_cases import get_ans_form

class TestCalculaMedia(unittest.TestCase):

    def test_1(self):
        result = get_ans_form()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()