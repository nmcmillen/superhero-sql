# This is why you'll execute a series of SQL statements during demo day.
from connection import execute_query

# select_heroes = """
#     SELECT * FROM heroes
#     ORDER BY id DESC 
# """

create_testable = """
create table TESTABLE (
    id int generated always as identity primary key,
    name varchar,
    ability varchar
)
"""

# execute_query(create_testable)


# heroes = execute_query(select_heroes).fetchall()
# for hero in heroes:
#     print(hero[1])