# This is why you'll execute a series of SQL statements during demo day.
#from connections.connection import execute_query

# select_heroes = """
#     SELECT * FROM heroes
# """

# heroes = execute_query(select_heroes).fetchall()
# for hero in heroes:
#     print(hero[1])

# create_testable = """
# create table TESTABLE (
#     id int generated always as identity primary key,
#     name varchar,
#     ability varchar
# )
# """

# create_ability = """
# INSERT INTO ability_types
# VALUES(DEFAULT, 'Brickwall')
# """
# execute_query(create_ability)

# execute_query(INSERT VARIABLE HERE)


# ability = 'Flying'

# sql1 = '''SELECT * {0}
# FROM {1} INNER JOIN {2}
# ON {1}.{3} = {2}.{3}
# Order By {4} desc;
# '''

# print(sql1.format('Spot','Dogs', 'Owners', 'DogID', 'Speed'))

#create_ability = """
#INSERT INTO ability_types
#VALUES(DEFAULT, '{0}')
#"""

#execute_query(create_ability.format('Flying'))

import queries.different_name as dn
dn.create()