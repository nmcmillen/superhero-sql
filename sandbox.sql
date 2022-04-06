-- CREATES THE TEST TABLE --
create_testable = """
create table TESTABLE (
    id int serial primary key,
    name varchar,
    ability varchar
)
"""

-- DELETES TESTABLE THAT WAS CREATED --
delete_testable = """
drop table testable
"""

-- CREATES A NEW ABILITY --
create_ability = """
INSERT INTO ability_types
VALUES(DEFAULT, 'Cloning')
"""