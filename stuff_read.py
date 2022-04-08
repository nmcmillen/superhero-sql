from connections.connection import execute_query

## SHOW ALL SUPER HEROES ##
def show_all_heroes():
    show_heroes = """
        SELECT * FROM heroes
        ORDER BY name ASC
    """
    heroes = execute_query(show_heroes).fetchall()
    print("The Superheroes Are:")
    for hero in heroes:
        print("- " + hero[1])


## WILL PRINT 'CHILL WOMAN' ##
def print_hero_name():
    select_chill = """
        Select name from heroes
        where name = 'Chill Woman'
    """
    chill = execute_query(select_chill).fetchone()
    print("Printing Chill Woman: " + (chill[0]))


## SEARCHES ENEMIES OF A HERO INPUT ##
def show_specific_enemies(search):
    enemies = execute_query("""
    SELECT h2.name
    FROM relationships
    INNER JOIN heroes h1
    ON h1.id=relationships.hero1_id
    INNER JOIN heroes h2
    ON h2.id=relationships.hero2_id
    WHERE h1.name = %(search_name)s and relationship_type_id = 1
    """,
    {'search_name': search}).fetchall()
    if not enemies:
         print("Has no enemies")
    for enemy in enemies:
        # print("Something enemies are:")
        print("- " + enemy[0])


## SEARCHES FRIEND OF A HERO INPUT ##
def show_specific_friends(search):
    friends = execute_query("""
    SELECT h2.name
    FROM relationships
    INNER JOIN heroes h1
    ON h1.id=relationships.hero1_id
    INNER JOIN heroes h2
    ON h2.id=relationships.hero2_id
    WHERE h1.name = %(search_name)s and relationship_type_id = 1
    """,
    {'search_name': search}).fetchall()
    if not friends:
         print("Has no friends")
    for friend in friends:
        # print("Something friends are:")
        print("- " + friend[0])


# show_all_heroes()
# print_hero_name()
# show_enemies()
# show_specific_enemies()
# show_specific_friends()