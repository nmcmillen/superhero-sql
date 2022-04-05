import pytest
from demo import *

def test_if_true():
    assert True

def test_create_table():
    assert execute_query(create_testable) == True