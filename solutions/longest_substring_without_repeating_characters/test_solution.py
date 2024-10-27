import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("input_str, expected", [
    ("", 0),
    ("a", 1),
    ("au", 2),
    ("aab", 2),
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("abcde", 5),
    ("anviaj", 5),
])
def test_multiple_cases(solution, input_str, expected):
    assert solution.lengthOfLongestSubstring(input_str) == expected