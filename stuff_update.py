from connections.connection import execute_query

## CHANGE THE ABOUT ME SECTION OF A HERO ##
def update_hero_about(name, about):
    execute_query("""
    UPDATE heroes
    SET about_me = %(new_bio)s
    WHERE name = %(new_name)s
    """,
    {'new_name': name, 'new_bio': about})


# update_hero_about()