import pytest
from queries.create import *
from queries.read import *
from queries.update import *
from queries.delete import *

def test_if_true():
    assert True

def test_another_sum():
    assert another_sum(3, 2) == 5

# def test_create_table():
#     assert execute_query(create_testable) == True

# select_chill = """
#     Select name from heroes
#     where name = 'Chill Woman'
# """

# WORKING WITH SELECT_CHILL IN READ.PY
def test_hero_return_chill():
    chill = execute_query(select_chill).fetchone()
    assert chill[0] == 'Chill Woman'
