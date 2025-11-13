import pytest
from app import add_numbers,sub_numbers

def test_add_numbers():
    assert add_numbers(2,3)==5
    assert add_numbers(-1,1)==0
    assert add_numbers(10,10)==20

def test_sub_numbers():
    assert sub_numbers(5,3)==2
    assert sub_numbers(23,3)==20
    assert sub_numbers(3,3)==0


