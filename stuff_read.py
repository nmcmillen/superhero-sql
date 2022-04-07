from connections.connection import execute_query

## JOSH'S PRINT EXAMPLE TO SHOW ALL SUPER HEROES ##
def show_all_heroes():
    select_heroes = """
        SELECT * FROM heroes
    """
    heroes = execute_query(select_heroes).fetchall()
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


## PRINT THE ENEMIES OF A HERO (SPECIFIC TO THE HUMMINGBIRD) ##
def show_enemies():
    select_enemies = """
        SELECT name
        FROM heroes
        WHERE id IN (
            SELECT hero2_id
            FROM relationships
            WHERE hero1_id = 4 AND relationship_type_id = 2);
    """
    enemy = execute_query(select_enemies).fetchall()
    print("The Enemies Are:")
    for enemies in enemy:
        print("- " + enemies[0])


# show_all_heroes()
# print_hero_name()
# show_enemies()