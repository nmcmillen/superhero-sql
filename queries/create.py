from connection import execute_query

create_testable = """
create table TESTABLE (
    id int generated always as identity primary key,
    name varchar,
    ability varchar
)
"""

# execute_query(create_testable)

def another_sum(a, b):
    return a + b
