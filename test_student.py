import unittest
from student import get_grade

class TestStudent(unittest.TestCase):
    def test_get_grade(self):
        self.assertEqual(get_grade(95), "A")
        self.assertEqual(get_grade(80), "B")
        self.assertEqual(get_grade(65), "C")
        self.assertEqual(get_grade(40), "F")
        self.assertEqual(get_grade(-5), "Error: Invalid score")
        self.assertEqual(get_grade(110), "Error: Invalid score")

if __name__ == "__main__":
    unittest.main()
