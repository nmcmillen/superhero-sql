import sys
sys.path.append("/workspace/superhero-sql")
from connections.connection import execute_query

## CREATE NEW CHARACTER ##
def create():
    create_new_character = """
    INSERT INTO heroes
    VALUES(DEFAULT, '{0}', '{1}', '{2}')
    """
    execute_query(create_new_character.format('hello there 12', 'not sure', 'try again'))

print("Does this happen twice?")
create()