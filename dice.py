#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Final Project Module"""

import random


def rolldie():
    """Defines a function to roll varying types of dice for gameplay.

        Args:
        None.

        Returns:
        string containing the result of the roll.

        Example:
        >>> rolldie()
        Roll what type of dice? D4, D6, D8, D10, D12, D20: d4
        'You rolled 3'
        >>> rolldie()
        Roll what type of dice? D4, D6, D8, D10, D12, D20: d20
        'You rolled 15'
        >>> rolldie()
        Roll what type of dice? D4, D6, D8, D10, D12, D20: d56
        'Invalid dice, Adventurer. Please try again.'        
    """
    diecast = str(0)
    dice = str(raw_input('Roll what type of dice? D4, D6, D8, D10, D12, D20: '))
    if dice == 'd4':
        diecast = random.randint(1, 4)
        return 'You rolled ' + str(diecast)
    elif dice == 'd6':
        diecast = random.randint(1, 6)
        return 'You rolled ' + str(diecast)
    elif dice == 'd8':
        diecast = random.randint(1, 8)
        return 'You rolled ' + str(diecast)
    elif dice == 'd10':
        diecast = str(random.randint(0, 9))+str(random.randint(0, 9))+'%'
        return 'You rolled ' + str(diecast)
    elif dice == 'd12':
        diecast = random.randint(1, 12)
        return 'You rolled ' + str(diecast)
    elif dice == 'd20':
        diecast = random.randint(1, 20)
        return 'You rolled ' + str(diecast)
    else:
        return 'Invalid dice, Adventurer. Please try again.'
