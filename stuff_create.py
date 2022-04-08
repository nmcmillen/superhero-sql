from connections.connection import execute_query

## CREATED NEW TABLE CALLED "test_table" ## 
def create_test_table():
    new_test_table = """
    CREATE TABLE test_table (
        id int generated always as identity primary key,
        name varchar,
        ability varchar
    )
    """
    execute_query(new_test_table)


## CREATES NEW ABILITY BY PASSING IN PARAMETER ##
def create_ability_type(ability):
    execute_query("""
    INSERT INTO ability_types
    VALUES(DEFAULT, %(new_ability)s)
    """,
    {'new_ability': ability})


def create_new_character(name, about, bio):
    execute_query("""
    INSERT INTO heroes
    VALUES(DEFAULT, %(new_name)s, %(new_about)s, %(new_bio)s)
    """,
    {'new_name': name, 'new_about': about, 'new_bio': bio})


# create_test_table()
# create_ability_type()
# create_new_character()