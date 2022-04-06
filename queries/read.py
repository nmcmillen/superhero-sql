import sys
sys.path.append(".")
from connections.connection import *

## JOSH'S PRINT EXAMPLE TO SHOW ALL SUPER HEROES ##
select_heroes = """
    SELECT * FROM heroes
"""

heroes = execute_query(select_heroes).fetchall()
for hero in heroes:
    print("Heroes are " + (hero[1]))


## WILL PRINT 'CHILL WOMAN' ##
select_chill = """
    Select name from heroes
    where name = 'Chill Woman'
"""

chill = execute_query(select_chill).fetchone()
print("Printing Chill Woman: " + (chill[0]))

## PRINT THE ENEMIES OF A HERO (SPECIFIC TO THE HUMMINGBIRD) ##
select_enemies = """
    SELECT name
    FROM heroes
    WHERE id IN (
		SELECT hero2_id
		FROM relationships
		WHERE hero1_id = 4 AND relationship_type_id = 2);
"""
enemy = execute_query(select_enemies).fetchall()
for enemies in enemy:
    print("The enemy is " + enemies[0])