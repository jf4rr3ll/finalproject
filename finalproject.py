#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Final Project Module"""

import random


print 'Welcome, Adventurer! We are about to embark on an exciting journey, \
but first we need some information about you. Type createcharacter() to begin!'

PLAYERNAME = ''
CHARSHEET = ''
CHARNAME = ''
CHARAGE = ''
CHARGENDER = ''
CHARHEIGHT = ''
CHARWEIGHT = ''
CHAREYES = ''
CHARHAIR = ''
CHARSKIN = ''
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
AC = 10
CHARLEVEL = 1
ATK = 0
DIECAST = 0


def createcharacter():
    "Defines the function to create a new character sheet"
    global PLAYERNAME
    global CHARSHEET
    global CHARNAME
    global CHARAGE
    global CHARGENDER
    global CHARHEIGHT
    global CHARWEIGHT
    global CHAREYES
    global CHARHAIR
    global CHARSKIN
    global CHARCLASS
    global CHARALIGN
    PLAYERNAME = raw_input('Player Name: ')
    CHARNAME = raw_input('Character Name: ')
    CHARAGE = raw_input('Welcome ' + CHARNAME + ', how old are you? ')
    CHARGENDER = raw_input(CHARNAME + ', are you Male or Female? ')
    CHARHEIGHT = raw_input('How tall are you? (Ex: 6ft 2in)')
    CHARWEIGHT = raw_input('How much do you weigh? (Ex: 250lbs)')
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
    print 'Welcome ' + CHARNAME + ', are you ready to determine your \
    abilities? Type rollstats() to get your stats!'
    return


def rollstats():
    "Defines the function that rolls character stats."
    global CHARSTR
    global CHARDEX
    global CHARCON
    global CHARINT
    global CHARWIS
    global CHARCHA
    global ABILITIES
    global CHARSHEET
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
    CHARSHEET = (('-' * 40) + '\nPlayer: ' + PLAYERNAME + '\n' + ('-' * 40)
                 + ' \nCharacter Name: ' + CHARNAME + '\nLevel: '
                 + str(CHARLEVEL)
                 + '| HP: '+ str(HP) + '| AC: ' + str(AC) + '\n' + ('-' * 40)
                 + ' \nClass: ' + CHARCLASS + '| Alignment: '+ CHARALIGN
                 + '\n' + ('-' * 40) + '\nAge: ' + str(CHARAGE) + ' Height: '
                 + CHARHEIGHT + ' Weight: ' + CHARWEIGHT + '\nEye Color: '
                 + CHAREYES + '| Hair Color: ' + CHARHAIR + '| Skin Color: '
                 + CHARSKIN + '\n' + ('-' * 40) + '\n' + ABILITIES + ('-' * 40))
    print ('You rolled the following stats: \n' + ABILITIES + '\nWould you \
like to see your completed character sheet? \nIf so, type "print CHARSHEET". \
\nOtherwise, you can "attack()", record "damagetaken()", or use "healing()". \
\nRemember, you can see your updated character sheet by typing "print \
CHARSHEET"! Good luck, adventurer!')
    return


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
    global ATK
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
