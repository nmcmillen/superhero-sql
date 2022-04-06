import sys
sys.path.append(".")
from connections.connection import *

# execute_query(INSERT VARIABLE HERE)

## CREATES NEW ABILITY BY PASSING IN PARAMETER WITH .FORMAT ##
create_ability = """
INSERT INTO ability_types
VALUES(DEFAULT, '{0}')
"""

# execute_query(create_ability.format('Flying'))
# USING 'FLYING' IS FIRST PARAMETER. CAN ADD MORE 2,3, ETC.


## CREATED NEW TABLE CALLE "test_table" ## 
create_new_test_table = """
CREATE TABLE test_table (
    id int generated always as identity primary key,
    name varchar,
    ability varchar
)
"""
