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

## PRINT THE ENEMIES OF A HERO (SPECIFIC TO THE HUMMINGBIRD) ##
# def show_enemies():
#     select_enemies = """
#         SELECT name
#         FROM heroes
#         WHERE id IN (
#             SELECT hero2_id
#             FROM relationships
#             WHERE hero1_id = 4 AND relationship_type_id = 2);
#     """
#     enemy = execute_query(select_enemies).fetchall()
#     print("The Enemies Are:")
#     for enemies in enemy:
#         print("- " + enemies[0])


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

SELECT heroes.name, relationships.hero1_id, relationships.hero2_id, relationships.relationship_type_id
FROM heroes
RIGHT OUTER JOIN relationships ON heroes.id=relationships.hero1_id where relationship_type_id=1



SELECT h1.name, relationships.hero1_id, h2.name, relationships.hero2_id, relationships.relationship_type_id
FROM relationships
INNER JOIN heroes h1
ON h1.id=relationships.hero1_id
INNER JOIN heroes h2
ON h2.id=relationships.hero2_id
WHERE h1.name = 'The Hummingbird' and relationship_type_id = 2

SELECT h2.name, relationships.relationship_type_id
FROM relationships
INNER JOIN heroes h1
ON h1.id=relationships.hero1_id
INNER JOIN heroes h2
ON h2.id=relationships.hero2_id
WHERE h1.name = 'The Hummingbird' and relationship_type_id = 2


def show_specific_enemies():
    select_enemies = """
    SELECT h2.name
    FROM relationships
    INNER JOIN heroes h1
    ON h1.id=relationships.hero1_id
    INNER JOIN heroes h2
    ON h2.id=relationships.hero2_id
    WHERE h1.name = 'The Seer' and relationship_type_id = 2
    """
    enemies = execute_query(select_enemies).fetchall()
    print(enemies)
    if not enemies:
         print("Has no enemies")
    for enemy in enemies:
        print("- " + enemy[0])

def show_specific_friends():
    select_friends = """
    SELECT h2.name
    FROM relationships
    INNER JOIN heroes h1
    ON h1.id=relationships.hero1_id
    INNER JOIN heroes h2
    ON h2.id=relationships.hero2_id
    WHERE h1.name = 'Chill Woman' and relationship_type_id = 1
    """
    friends = execute_query(select_friends).fetchall()
    if not friends:
         print("Has no friends")
    for friend in friends:
        print("Something friends are:")
        print("- " + friend[0])


-- # def show_specific_enemies():
-- #     select_enemies = """
-- #     SELECT h2.name
-- #     FROM relationships
-- #     INNER JOIN heroes h1
-- #     ON h1.id=relationships.hero1_id
-- #     INNER JOIN heroes h2
-- #     ON h2.id=relationships.hero2_id
-- #     WHERE h1.name = 'The Hummingbird' and relationship_type_id = 2
-- #     """
-- #     enemies = execute_query(select_enemies).fetchall()
-- #     if not enemies:
-- #          print("Has no enemies")
-- #     for enemy in enemies:
-- #         print("- " + enemy[0])