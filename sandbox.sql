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



-- def update_hero_about(name, bio):
--     execute_query("""
--     UPDATE heroes
--     SET about_me = '%(bio)s'
--     WHERE name = '%(name)s'
--     """,
--     {'name': name, 'bio': bio})

-- ## CREATE A NEW CHARACTER WITH NAME, ABOUT ME, and BIO PARAMETERS ##
-- # def create_new_character(name, about, bio):
-- #     name = input("Enter a super hero name:")
-- #     create_character = """
-- #     INSERT INTO heroes
-- #     VALUES(DEFAULT, '{0}', '{1}', '{2}')
-- #     print('0' now has been created and their bio says '2')
-- #     """.format(name, about, bio)
-- #     execute_query(create_character)