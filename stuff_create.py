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

## CREATES NEW ABILITY BY PASSING IN PARAMETER WITH .FORMAT ##
def create_ability_type():
    new_ability = """
    INSERT INTO ability_types
    VALUES(DEFAULT, '{0}')
    """

    execute_query(new_ability.format('Pure Strength'))
    # USING 'FLYING' AS FIRST PARAMETER. CAN ADD MORE 2,3, ETC.


## CREATE A NEW CHARACTER WITH NAME, ABOUT ME, and BIO PARAMETERS ##
def create_new_character():
    create_character = """
    INSERT INTO heroes
    VALUES(DEFAULT, '{0}', '{1}', '{2}')
    """
    execute_query(create_character.format('Testman', 'Test about', 'asomethinaglsdfnplwaejfj'))



# create_test_table()
# create_ability_type()
# create_new_character()