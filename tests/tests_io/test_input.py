import unittest
from app.io.input import read_text_from_file, read_text_from_file_pd

class TestInputFunctions(unittest.TestCase):
    input_filename = "./test_data/input.txt"
    incorrect_type_filename = "./test_data/image.jpg"
    input_filename_pd = "./test_data/input.csv"

######### Python read file functions test #########
    # Read existing correct file
    def test_read_text_from_file_existing_file(self):
        expected_text = "Some test data."
        actual_text = read_text_from_file(self.input_filename)
        self.assertEqual(actual_text.strip(), expected_text)

    # Read existing incorrect file
    def test_read_text_from_file_incorrect_file(self):
        text = read_text_from_file(self.incorrect_type_filename)
        self.assertRaises(UnicodeDecodeError)

    # Read non-existing file
    def test_read_text_from_file_nonexisting_file(self):
        text = read_text_from_file("nonexistent_file.txt")
        self.assertRaises(FileNotFoundError)

######### Pandas read file functions test #########
    # Read existing correct file
    def test_read_text_from_file_pd_existing_file(self):
        expected_text = "   name  age\n   John   15\nJessica   17"
        actual_text = read_text_from_file_pd(self.input_filename_pd)
        self.assertEqual(actual_text, expected_text)

    # Read existing incorrect file
    def test_read_text_from_file_pd_incorrect_file(self):
        text = read_text_from_file_pd(self.incorrect_type_filename)
        self.assertRaises(UnicodeDecodeError)

    # Read non-existing file
    def test_read_text_from_file_pd_nonexisting_file(self):
        text = read_text_from_file_pd("nonexistent_file.csv")
        self.assertRaises(FileNotFoundError)

if __name__ == '__main__':
    unittest.main()
