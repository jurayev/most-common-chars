from typing import List, Tuple
from collections import Counter
import unittest
import functools

# Solution 1
# Type Annotations showcase
def most_common_chars(string: str) -> List[str]:
  most_common: List[Tuple[str, int]] = Counter(string).most_common()
  i: int = 0
  k: str
  v: int
  for k, v in most_common:
    most_common[i] = k
    i += 1
  return most_common

# Solution 2
# Uncomment to run unittests
# def most_common_chars(string):
#   most_common = dict()
#   for char in string:
#     if char in most_common:
#       most_common[char] += 1
#     else:
#       most_common[char] = 1 
#   most_common = [(v, k) for k, v in most_common.items()]  
#   most_common.sort(key=lambda a: (a[0], -ord(a[1])), reverse=True)  
#   most_common = [v for k, v in most_common]
#   return most_common

class TestMostCommon(unittest.TestCase):

  # Logging decorator
  def log(func):
    @functools.wraps(func)
    def wrapper(cls):
      print("-"*10, func.__name__, "-"*10)
      func(cls)
      print("-"*10, "PASSED", "-"*10, "\n")

    return wrapper

  @log
  def test_lowercase_c_most_common(self):
    # Arrange
    input_data = "abcc"
    expected = ["c", "a", "b"]
    # Act
    actual = most_common_chars(input_data)
    # Assert
    self.assertListEqual(actual, expected, "Char 'c' must be the most common\n")

  @log
  def test_single_char(self):
    input_data = "a"
    expected = ["a"]
    actual = most_common_chars(input_data)
    self.assertListEqual(actual, expected, "Char 'a' must be the most common\n")

  @log
  def test_equal_frequency(self):
    input_data = "abc"
    expected = ["a", "b", "c"]
    actual = most_common_chars(input_data)
    self.assertListEqual(actual, expected, "All chars must be equally common\n")

  @log
  def test_mixedcase_C_most_common(self):
    input_data = "abcCCC"
    expected = ["C", "a", "b", "c"]
    actual = most_common_chars(input_data)
    self.assertListEqual(actual, expected, "Char 'C' must be the most common\n")  

  @log
  def test_whitespace_most_common(self):
    input_data = "abc  f"
    expected = [" ", "a", "b", "c", "f"]
    actual = most_common_chars(input_data)
    self.assertListEqual(actual, expected, "Whitespace char must be the most common\n")

  @log
  def test_mixed_chars(self):
    input_data = "!###333+@"
    expected = ["#", "3", "!", "+", "@"]
    actual = most_common_chars(input_data)
    self.assertListEqual(actual, expected, "Chars '#' and '3' must be the most common\n")

  @log
  def test_empty_input(self):
    input_data = ""
    expected = []
    actual = most_common_chars(input_data)
    self.assertListEqual(actual, expected, "There is no common chars\n")    

tests = TestMostCommon()
tests.test_lowercase_c_most_common()
tests.test_single_char()
tests.test_equal_frequency()
tests.test_mixedcase_C_most_common()
tests.test_whitespace_most_common()
tests.test_mixed_chars()
tests.test_empty_input()
