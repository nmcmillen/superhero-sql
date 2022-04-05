-- CREATES THE TEST TABLE --
create_testable = """
create table TESTABLE (
    id int serial primary key,
    name varchar,
    ability varchar
)
"""
execute_query(create_testable)


-- DELETES TESTABLE THAT WAS CREATED --
delete_testable = """
drop table testable
"""