#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Final Project Module"""

import random
import dice


print 'Welcome, Adventurer! We are about to embark on an exciting journey, \
but first we need some information about you. Type createcharacter() to begin!'

CHARNAME = ''
CHARCLASS = ''
CHARALIGN = ''
CHARSTR = ''
CHARDEX = ''
CHARCON = ''
CHARINT = ''
CHARWIS = ''
CHARCHA = ''
ABILITIES = ''
HP = 100
ATK = 0
DIECAST = 0


def createcharacter():
    "Defines the function to create a new character sheet"
    global CHARNAME
    global CHARCLASS
    global CHARALIGN
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
    global CHARSTR
    global CHARDEX
    global CHARCON
    global CHARINT
    global CHARWIS
    global CHARCHA
    global ABILITIES
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
    print 'You rolled the following stats: \n' + ABILITIES
    return

CHARSHEET = (('-' * 40) + ' \nCharacter Name: ' + CHARNAME + ' HP: '
             + str(HP) + ' \nClass: ' + CHARCLASS + ' Alignment: '
             + CHARALIGN + '\n' + ('-' * 40) + '\n' + ABILITIES + ('-' * 40))
        
print CHARSHEET

def rolldie():
    """Defines a function to roll varying types of dice for gameplay.        
    """
    global DIECAST
    DICE = str(raw_input('Roll what type of dice? D4, D6, D8, D10, D12, D20: '))
    if DICE == 'd4':
        DIECAST = random.randint(1, 4)
        return DIECAST
    elif DICE == 'd6':
        DIECAST = random.randint(1, 6)
        return DIECAST
    elif DICE == 'd8':
        DIECAST = random.randint(1, 8)
        return DIECAST
    elif DICE == 'd10':
        DIECAST = str(random.randint(0, 9))+str(random.randint(0, 9))+'%'
        return DIECAST
    elif DICE == 'd12':
        DIECAST = random.randint(1, 12)
        return DIECAST
    elif DICE == 'd20':
        DIECAST = random.randint(1, 20)
        return DIECAST
    else:
        return 'Invalid dice, Adventurer. Please try again.'


def attack():
    global DIECAST
    ROLL = rolldie()
    if ROLL == 'Invalid dice, Adventurer. Please try again.':
        return 'Invalid dice, Adventurer. Please try again.'
    else:
        ATK = DIECAST
        return 'Your attack hits for ' + str(ATK) + ' damage!'

def damagetaken():
    global HP
    global DIECAST
    ROLL = rolldie()
    if ROLL == 'Invalid dice, Adventurer. Please try again.':
        return 'Invalid dice, Adventurer. Please try again.'
    else:
        HP = HP - DIECAST
        return 'Your HP is now ' + str(HP)

def healing():
    global HP
    global DIECAST
    ROLL = rolldie()
    if ROLL == 'Invalid dice, Adventurer. Please try again.':
        return 'Invalid dice, Adventurer. Please try again.'
    else:
        HP = HP + DIECAST
        return 'Your HP is now ' + str(HP)

print 'To get your updated character sheet, type print CHARSHEET.'
