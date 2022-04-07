from connections.connection import execute_query

## CHANGE THE ABOUT ME SECTION OF A HERO
def update_hero_about():
    update_about = """
    UPDATE heroes
    SET about_me = '{1}'
    WHERE name = '{0}'
    """
    execute_query(update_about.format('Testman', 'tEST CHANGE IT'))

update_hero_about()