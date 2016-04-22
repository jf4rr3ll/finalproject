#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Final Project Module"""

import random


def createcharacter():
    """Defines a function to create a character
    """
    print ('Welcome, Adventurer! We are about to embark on an exciting journey,'
    + ' but first we need some information about you.')
    PLAYERNAME = raw_input('Player Name: ')
    CHARNAME = raw_input('Character Name: ')
    CHARAGE = raw_input('Welcome ' + CHARNAME + ', how old are you? ')
    CHARGENDER = raw_input(CHARNAME + ', are you Male or Female? ')
    CHARHEIGHT = raw_input('How tall are you? ')
    CHARWEIGHT = raw_input('How much do you weigh? ')
    CHAREYES = raw_input('What color are your eyes? ')
    CHARHAIR = raw_input('How about your hair color? ')
    CHARSKIN = raw_input('And skin color? ')
    CHARCLASS = raw_input('Select a class: Barbarian, Bard, Cleric, Druid, '
                          'Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, '
                          'Wizard: ')
    CHARALIGN1 = raw_input('Align yourself, adventurer! Good, Neutral, or'
                           ' Evil? ')
    CHARALIGN2 = raw_input('Complete your alignment: Lawful, Neutral, or'
                           ' Chaotic? ')
    CHARALIGN = CHARALIGN2 + ' ' + CHARALIGN1
    print 'Welcome ' + CHARNAME + ', are you ready to determine your abilities?'
    print 'Excellent! Let\'s roll the dice!'
    ROLL = raw_input('Hit Enter to roll the dice')
    CHARSTR = random.randint(1, 10)
    CHARDEX = random.randint(1, 10)
    CHARCON = random.randint(1, 10)
    CHARINT = random.randint(1, 10) 
    CHARWIS = random.randint(1, 10)
    CHARCHA = random.randint(1, 10)
    ABILITIES = ('Strength: ' + str(CHARSTR) + '.' +  '\n'
    + 'Dexterity: ' + str(CHARDEX) + '.' +  '\n'
    + 'Constitution: ' + str(CHARCON) + '.' +  '\n'
    + 'Intelligence: ' + str(CHARINT) + '.' +  '\n'
    + 'Wisdom: ' + str(CHARWIS) + '.' +  '\n'
    + 'Charisma: ' + str(CHARCHA) + '.' +  '\n')
        
    return CHARNAME + ' ' + CHARCLASS + ' ' + CHARALIGN + ' ' + ABILITIES


