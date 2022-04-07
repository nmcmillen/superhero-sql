from connections.connection import execute_query

## DELETE THE CREATED TEST TABLE ##
def delete_test_table():
    delete_testable = """
    DROP TABLE TESTABLE
    """

    execute_query(delete_testable)


## DELETE A HERO BY NAME
def delete_a_hero():
    bye_hero = """
    DELETE FROM heroes
    WHERE name = '{0}'
    """
    execute_query(bye_hero.format('Testman'))


# delete_test_table()
delete_a_hero()

