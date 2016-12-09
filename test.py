import pytest
from mfMath import util

class Test_standard_deviation:

    def test_emptyList(self):
         assert util.standard_deviation([]) == None

    def test_math(self):
        assert util.standard_deviation([1,2]) == 0.5

    def test_is_list(self):
        with pytest.raises(TypeError):
            util.standard_deviation("x")

    def test_list_all_numbers(self):
        with pytest.raises(TypeError):
            util.standard_deviation([1,2,3,4,"2"])

    def test_atleast_length_two(self):
        assert util.standard_deviation([1]) == None


class Test_standard_error:

    def test_emptyList(self):
        assert util.standard_error([]) == None

    def test_math(self):
        assert util.standard_error([1,2]) == 0.35355339059327373

    def test_is_list(self):
        with pytest.raises(TypeError):
            util.standard_error("x")

    def test_list_all_numbers(self):
        with pytest.raises(TypeError):
            util.standard_error([1,2,3,4,"2"])

    def test_atleast_length_two(self):
        assert util.standard_error([1]) == None

