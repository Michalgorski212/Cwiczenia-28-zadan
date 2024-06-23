import unittest
import threading
import time
import sqlite3
import os

def exercise1():
    import unittest

    def divide_numbers(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        return result

    class TestDivision(unittest.TestCase):
        def test_division_by_zero(self):
            self.assertEqual(divide_numbers(10, 0), "Error: Division by zero is not allowed.")

        def test_valid_division(self):
            self.assertEqual(divide_numbers(10, 2), 5)
            self.assertEqual(divide_numbers(9, 3), 3)

    if __name__ == '__main__':
        unittest.main()

def exercise2():
    import unittest

    def prompt_for_integer(input_value):
        try:
            return int(input_value)
        except ValueError:
            raise ValueError("Invalid integer input")

    class TestPromptForInteger(unittest.TestCase):
        def test_valid_integer(self):
            self.assertEqual(prompt_for_integer("10"), 10)
            self.assertEqual(prompt_for_integer("0"), 0)
            self.assertEqual(prompt_for_integer("-5"), -5)

        def test_invalid_integer(self):
            with self.assertRaises(ValueError) as context:
                prompt_for_integer("abc")
            self.assertEqual(str(context.exception), "Invalid integer input")

            with self.assertRaises(ValueError) as context:
                prompt_for_integer("12.34")
            self.assertEqual(str(context.exception), "Invalid integer input")

    if __name__ == '__main__':
        unittest.main()


def exercise3():
    import unittest

    def open_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Error: File not found."

    class TestOpenFile(unittest.TestCase):
        def test_file_exists(self):
            # Create a temporary file for testing
            with open('testfile.txt', 'w') as file:
                file.write('This is a test file.')
            self.assertEqual(open_file('testfile.txt'), 'This is a test file.')
            os.remove('testfile.txt')

        def test_file_not_exists(self):
            self.assertEqual(open_file('nonexistentfile.txt'), "Error: File not found.")

    if __name__ == '__main__':
        unittest.main()

def exercise4():
    import unittest

    def prompt_for_numbers(input1, input2):
        try:
            num1 = float(input1)
            num2 = float(input2)
            return num1, num2
        except ValueError:
            raise TypeError("Both inputs must be numerical.")

    class TestPromptForNumbers(unittest.TestCase):
        def test_valid_numbers(self):
            self.assertEqual(prompt_for_numbers("10", "20"), (10.0, 20.0))
            self.assertEqual(prompt_for_numbers("3.14", "2.71"), (3.14, 2.71))
            self.assertEqual(prompt_for_numbers("-5", "0"), (-5.0, 0.0))

        def test_invalid_numbers(self):
            with self.assertRaises(TypeError) as context:
                prompt_for_numbers("abc", "20")
            self.assertEqual(str(context.exception), "Both inputs must be numerical.")

            with self.assertRaises(TypeError) as context:
                prompt_for_numbers("10", "xyz")
            self.assertEqual(str(context.exception), "Both inputs must be numerical.")

            with self.assertRaises(TypeError) as context:
                prompt_for_numbers("abc", "xyz")
            self.assertEqual(str(context.exception), "Both inputs must be numerical.")

    if __name__ == '__main__':
        unittest.main()

def exercise5():
    import unittest

    def open_file_with_permission_check(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except PermissionError:
            return "Error: Permission denied."

    class TestOpenFileWithPermissionCheck(unittest.TestCase):
        def test_permission_denied(self):
            # Create a temporary file and change its permissions to induce a PermissionError
            with open('testfile.txt', 'w') as file:
                file.write('This is a test file.')
            os.chmod('testfile.txt', 0o000)  # Remove all permissions
            self.assertEqual(open_file_with_permission_check('testfile.txt'), "Error: Permission denied.")
            os.chmod('testfile.txt', 0o644)  # Restore permissions to delete the file
            os.remove('testfile.txt')

        def test_file_exists(self):
            with open('testfile.txt', 'w') as file:
                file.write('This is a test file.')
            self.assertEqual(open_file_with_permission_check('testfile.txt'), 'This is a test file.')
            os.remove('testfile.txt')

    if __name__ == '__main__':
        unittest.main()

def exercise6():
    import unittest

    def get_list_element(lst, index):
        try:
            return lst[index]
        except IndexError:
            return "Error: Index out of range."

    class TestGetListElement(unittest.TestCase):
        def test_valid_index(self):
            self.assertEqual(get_list_element([1, 2, 3, 4, 5], 2), 3)
            self.assertEqual(get_list_element(['a', 'b', 'c'], 1), 'b')
            self.assertEqual(get_list_element([10, 20, 30], 0), 10)

        def test_invalid_index(self):
            self.assertEqual(get_list_element([1, 2, 3], 5), "Error: Index out of range.")
            self.assertEqual(get_list_element(['a', 'b', 'c'], -4), "Error: Index out of range.")

    if __name__ == '__main__':
        unittest.main()

def exercise7():
    import unittest

    def prompt_for_number():
        try:
            num = input("Please enter a number: ")
            return int(num)
        except KeyboardInterrupt:
            return "Error: Input cancelled by user."
        except ValueError:
            return "Error: Invalid number."

    class TestPromptForNumber(unittest.TestCase):
        def test_valid_number(self):
            self.assertEqual(prompt_for_number_simulated("10"), 10)
            self.assertEqual(prompt_for_number_simulated("-5"), -5)
            self.assertEqual(prompt_for_number_simulated("0"), 0)

        def test_invalid_number(self):
            self.assertEqual(prompt_for_number_simulated("abc"), "Error: Invalid number.")
            self.assertEqual(prompt_for_number_simulated("12.34"), "Error: Invalid number.")

        def test_keyboard_interrupt(self):
            self.assertEqual(prompt_for_number_simulated_keyboard_interrupt(), "Error: Input cancelled by user.")

    def prompt_for_number_simulated(input_value):
        try:
            num = input_value
            return int(num)
        except ValueError:
            return "Error: Invalid number."

    def prompt_for_number_simulated_keyboard_interrupt():
        try:
            raise KeyboardInterrupt
        except KeyboardInterrupt:
            return "Error: Input cancelled by user."

    if __name__ == '__main__':
        unittest.main()

def exercise8():
    import unittest

    def safe_divide(a, b):
        try:
            return a / b
        except ArithmeticError:
            return "Error: An arithmetic error occurred."

    class TestSafeDivide(unittest.TestCase):
        def test_division_by_zero(self):
            self.assertEqual(safe_divide(10, 0), "Error: An arithmetic error occurred.")

        def test_valid_division(self):
            self.assertEqual(safe_divide(10, 2), 5)
            self.assertEqual(safe_divide(9, 3), 3)

        def test_division_with_large_numbers(self):
            self.assertEqual(safe_divide(1e308, 1e308), 1.0)

        def test_division_with_small_numbers(self):
            self.assertEqual(safe_divide(1e-308, 1e-308), 1.0)

    if __name__ == '__main__':
        unittest.main()

def exercise9():
    import unittest

    def open_file_with_encoding_check(file_path, encoding='utf-8'):
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            return "Error: Encoding issue encountered."

    class TestOpenFileWithEncodingCheck(unittest.TestCase):
        def test_valid_encoding(self):
            with open('testfile_utf8.txt', 'w', encoding='utf-8') as file:
                file.write('This is a test file with UTF-8 encoding.')
            self.assertEqual(open_file_with_encoding_check('testfile_utf8.txt'),
                             'This is a test file with UTF-8 encoding.')
            os.remove('testfile_utf8.txt')

        def test_encoding_issue(self):
            with open('testfile_latin1.txt', 'w', encoding='latin-1') as file:
                file.write('This is a test file with Latin-1 encoding.')
            self.assertEqual(open_file_with_encoding_check('testfile_latin1.txt', encoding='utf-8'),
                             "Error: Encoding issue encountered.")
            os.remove('testfile_latin1.txt')

    if __name__ == '__main__':
        unittest.main()

def exercise10():
    import unittest

    def safe_list_append(lst, element):
        try:
            lst.append(element)
            return lst
        except AttributeError:
            return "Error: Provided object does not have an 'append' attribute."

    class TestSafeListAppend(unittest.TestCase):
        def test_valid_list_append(self):
            self.assertEqual(safe_list_append([1, 2, 3], 4), [1, 2, 3, 4])
            self.assertEqual(safe_list_append(['a', 'b'], 'c'), ['a', 'b', 'c'])

        def test_invalid_list_append(self):
            self.assertEqual(safe_list_append("not a list", 4),
                             "Error: Provided object does not have an 'append' attribute.")
            self.assertEqual(safe_list_append(123, 4), "Error: Provided object does not have an 'append' attribute.")
            self.assertEqual(safe_list_append({'key': 'value'}, 'new value'),
                             "Error: Provided object does not have an 'append' attribute.")

    if __name__ == '__main__':
        unittest.main()

def get_exercise_function(name):
    exercises = {
        'exercise1': exercise1,
        'exercise2': exercise2,
        'exercise3': exercise3,
        'exercise4': exercise4,
        'exercise5': exercise5,
        'exercise6': exercise6,
        'exercise7': exercise7,
        'exercise8': exercise8,
        'exercise9': exercise9,
        'exercise10': exercise10,
    }
    return exercises.get(name)

def main():
    while True:
        exercise_name = input("Enter the exercise name (e.g., 'exercise1') or 'exit' to quit: ")
        if exercise_name == 'exit':
            break

        exercise_function = get_exercise_function(exercise_name)
        if exercise_function:
            exercise_function()
        else:
            print("No exercise found with that name.")

if __name__ == "__main__":
    main()
