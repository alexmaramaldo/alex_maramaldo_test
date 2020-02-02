import pytest
from my_libraries.string_compare import StringCompare


class TestStringCompare:
    def test_versions_same_length_first_bigger_case1(self):
        string_1 = '1.2.1'
        string_2 = '1.2.0'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is greater than '{string_2}'",\
            "Should return a +ve number if first version is bigger than the second with same length [case 1]"

    def test_versions_same_length_first_bigger_case2(self):
        string_1 = '1.4.1.0'
        string_2 = '1.4.0.6'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is greater than '{string_2}'",\
            "Should return a +ve number if first version is bigger than the second with same length [case 2]"

    def test_versions_same_length_first_bigger_case3(self):
        string_1 = '6'
        string_2 = '2'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is greater than '{string_2}'",\
            "Should return a +ve number if first version is bigger than the second with same length [case 3]"

    def test_versions_same_length_second_bigger_case1(self):
        string_1 = '1.2.0'
        string_2 = ' 1.2.1'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is less than '{string_2}'",\
            "Should return a +ve number if first version is smaller than the second with same length [case 1]"

    def test_versions_same_length_second_bigger_case2(self):
        string_1 = '1.4.0.6'
        string_2 = '1.4.1.0'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is less than '{string_2}'",\
            "Should return a -ve number if first version is smaller than the second with same length [case 2]"

    def test_versions_same_length_second_bigger_case3(self):
        string_1 = '2'
        string_2 = '6'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is less than '{string_2}'",\
            "Should return a -ve number if first version is smaller than the second with same length [case 3]"

    def test_versions_same_length_equals(self):
        string_1 = '1.2.3.4'
        string_2 = '1.2.3.4'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is equal to '{string_2}'",\
            "Should return zero if are equal with same length"

    def test_versions_doifferent_length_first_bigger_case1(self):
        string_1 = '1.2.1.0.0.0.1'
        string_2 = '1.2.0.2.9.0.1.2.1.2.3.5'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is greater than '{string_2}'",\
            "Should return a +ve number if first version is bigger than the second with different length [case 1]"

    def test_versions_different_length_first_bigger_case2(self):
        string_1 = '1.4.1.0.0.0.0.0.0'
        string_2 = '1.4.0.6'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is greater than '{string_2}'",\
            "Should return a +ve number if first version is bigger than the second with different length [case 2]"

    def test_versions_different_length_first_bigger_case3(self):
        string_1 = '6'
        string_2 = '1.0.0.0.0'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is greater than '{string_2}'",\
            "Should return a +ve number if first version is bigger than the second with different length [case 3]"

    def test_versions_different_length_second_bigger_case1(self):
        string_1 = '1.2.0.2.2.3.5.7.1'
        string_2 = '1.2.1.0.0.1'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is less than '{string_2}'",\
            "Should return a -ve number if first version is smaller than the second with different length [case 1]"

    def test_versions_different_length_second_bigger_case2(self):
        string_1 = '1.4.0.6.0.0'
        string_2 = '1.4.1.0.0.9.0.5'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is less than '{string_2}'",\
            "Should return a -ve number if first version is smaller than the second with different length [case 2]"

    def test_versions_different_length_second_bigger_case3(self):
        string_1 = '1.0'
        string_2 = '5.9.8.5.2'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is less than '{string_2}'",\
            "Should return a -ve number if first version is smaller than the second with different length [case 3]"

    def test_versions_different_length_equals_case1(self):
        string_1 = '1.2.3.0.0.0.0.0.0'
        string_2 = '1.2.3'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is equal to '{string_2}'",\
            "Should return zero if are equal with different length [case 1]"

    def test_versions_different_length_equals_case2(self):
        string_1 = '1.2.3.0.0.1.0'
        string_2 = '1.2.3.0.0.1.0.0.0'
        assert StringCompare(string_1, string_2).result == f"'{string_1}' is equal to '{string_2}'",\
            "Should return zero if are equal with different length [case 2]"

    def test_should_raise_error_if_not_string_parameter(self):
        with pytest.raises(AttributeError):
            StringCompare('1', 3.6)

    def test_should_raise_error_if_unexpected_character(self):
        with pytest.raises(ValueError):
            StringCompare('2.3.d.1', '2.b.4.a').result
