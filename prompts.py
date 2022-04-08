from stuff_create import *
from stuff_read import *
from stuff_update import *
from stuff_delete import *

## PROMPT TO CREATE NEW ABILITY ##
def add_ability():
    print('What is your super hero ability do you want to add?')
    ability = input()
    create_ability_type(ability)

## PROMPT TO CREATE CHARACTER ##
def create_character():
    print('What is your super heros name?')
    name = input()
    print('Tell me about your super hero')
    about = input()
    print('How did your super hero get their powers?')
    bio = input()
    create_new_character(name, about, bio)


## PROMPT TO UPDATE THE ABOUT ME SECTION OF A CHOSEN CHARACTER ##
def change_about_section():
    print('Choose a character name to update their "About Me" section:')
    show_all_heroes()
    name = input()
    print('What do you want their "About Me" to say?')
    about = input()
    update_hero_about(name, about)


## PROMPT TO DELETE HERO BY NAME ##
def delete_hero_by_name():
    print('You have the powers to eliminate one hero, who will it be?')
    show_all_heroes()
    name = input()
    delete_a_hero(name)
    print(name + ' has been eliminated')


# add_ability()
# change_about_section()
# create_character()
# delete_hero_by_name()

