#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Final Project Module"""

import random
import dice


print 'Welcome, Adventurer! We are about to embark on an exciting journey, \
but first we need some information about you. Type createcharacter() to begin!'


def createcharacter():
    "Defines the function to create a new character sheet"
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
    return

print 'Welcome ' + CHARNAME + ', are you ready to determine your abilities? \
Type rollstats() to get your stats!'

def rollstats():
    "Defines the function that rolls character stats."
    print 'Excellent! Let\'s roll the dice!'
    ROLL = raw_input('Hit Enter to roll the dice')
    CHARSTR = str(random.randint(1, 10))
    CHARDEX = str(random.randint(1, 10))
    CHARCON = str(random.randint(1, 10))
    CHARINT = str(random.randint(1, 10))
    CHARWIS = str(random.randint(1, 10))
    CHARCHA = str(random.randint(1, 10))
    ABILITIES = ('Strength: ' + CHARSTR + '\n'
                 + 'Dexterity: ' + CHARDEX + '\n'
                 + 'Constitution: ' + CHARCON + '\n'
                 + 'Intelligence: ' + CHARINT + '\n'
                 + 'Wisdom: ' + CHARWIS + '\n'
                 + 'Charisma: ' + CHARCHA + '\n')
    return

HP = 100
CHARSHEET = (('-' * 40) + ' \nCharacter Name: ' + CHARNAME + ' HP: '
             + str(HP) + ' \nClass: ' + CHARCLASS + ' Alignment: '
             + CHARALIGN + '\n' + ('-' * 40) + ABILITIES + ('-' * 40))
        
print CHARSHEET


def damagetaken():
    ROLL = dice.rolldie()
    DAMAGE = int(dice.diecast)
    HP = HP - DAMAGE
    return HP

print 'To get your updated character sheet, type print CHARSHEET.'
