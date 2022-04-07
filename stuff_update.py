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

# cur.execute("""
# ...     INSERT INTO some_table (an_int, a_date, a_string)
# ...     VALUES (%s, %s, %s);
# ...     """,
# ...     (10, datetime.date(2005, 11, 18), "O'Reilly"))

# def update_hero_about():
#     update_about = """
#     UPDATE heroes
#     SET about_me = '{1}'
#     WHERE name = '{0}'
#     """
#     execute_query(update_about.format('Testman', 'tEST CHANGE IT'))

## CHANGE THE ABOUT ME SECTION OF A HERO ##
# def update_hero_about():
#     execute_query("""
#     UPDATE heroes
#     SET about_me = %(bio)s
#     WHERE name = %(name)s
#     """,
#     {'name': 'Testman', 'bio': 'Does it work?'})