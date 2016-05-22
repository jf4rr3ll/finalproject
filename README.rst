######################
Dungeonmaster's Helper
######################

***********
Overview
***********

Dungeonmaster's Helper is a digitally created character sheet that generates
a character sheet for Dungeons and Dragons players. The program helps players
unfamiliar with character creation by prompting them for various inputs, and
also includes digital dice in order to automatically update the character sheet
with changes in level, stats, health, etc. 

***********
Personas
***********

.. table:: 

    +---------------------+-----------------------+----------------------------+
    | **Name**            | **Details**           |  **Goals**                 |
    +=====================+=======================+============================+
    | Michelle,           | A 21 year old student,| Wants a better way to keep |
    | the Dungeonmaster   | youngest sister, and  | all of the character sheets|
    |                     | acting dungeonmaster  | organized, and make sure   |
    |                     | for the family D&D    | her brothers can't cheat by|
    |                     | games.                | erasing or changing their  |
    |                     |                       | stats or HP when no one is |
    |                     |                       | looking, and "accidentally"|
    |                     |                       | rolling the dice off the   |
    |                     |                       | table.                     |
    +---------------------+-----------------------+----------------------------+
    | John, the           | A 31 year old IT      | Doesn't like having to keep|
    | Experienced Player  | professional who plays| track of his stats as he   |
    |                     | with his family in his| levels up, or doing lots of| 
    |                     | spare time.           | math in the margins of his |
    |                     |                       | character sheet to track   |
    |                     |                       | damage. Has limited free   |
    |                     |                       | time to play, and wants to |
    |                     |                       | make the most of it.       |
    +---------------------+-----------------------+----------------------------+
    | Chris,              | A 27 year old middle  | New to the game, and not   |
    | the Newbie          | sibling who enjoys    | familiar with how to fill  |
    |                     | causing mischeif.     | out a character sheet or   |
    |                     | Chaotic Evil.         | track stats. As a casual   |
    |                     |                       | player only looking to play|
    |                     |                       | with family, wants an easy |
    |                     |                       | way to play without taking |
    |                     |                       | time to learn all of the   |
    |                     |                       | particulars.               |
    +---------------------+-----------------------+----------------------------+

*******************
Problem Scenarios
*******************

.. table:: 

    +--------------------+------------------------+----------------------------+
    |**Problem Scenario**|**Current Alternatives**|  **Value Proposition**     |
    +====================+========================+============================+
    | Michelle the       | Michelle tries to watch| Creating a digital         |
    | Dungeonmaster wants| carefully when they    | character sheet that she   |
    | to make sure her   | write in their stats,  | could modify, or that would|
    | brothers can't     | damage, HP, and other  | be updated automatically   |
    | cheat on their     | game info.             | by digital dice rolls would|
    | character sheets.  |                        | help avoid cheating, and   |
    |                    |                        | also likely help the game  |
    |                    |                        | to move along more quickly.|
    +--------------------+------------------------+----------------------------+
    | John, the          | John uses a calculator | A digital character sheet  |
    | Experienced Player | to keep track of his HP| with automatic updates for |
    | wants all the math | and damage.            | all of his moves would mean| 
    | to be done for him |                        | John doesn't have to update|
    | automatically every|                        | anything manually, so he is|
    | time he rolls.     |                        | free to focus on how to get|
    |                    |                        | the basilisk to go after   |
    |                    |                        | his brother instead of him.|
    +--------------------+------------------------+----------------------------+
    | Chris, the Newbie  | There are some digital | Creating a tool to prompt  |
    | needs an easy way  | character sheets online| new players for the inputs |
    | to fill and update | but they won't update  | that need to be added to   |
    | his character sheet| based on his gameplay. | their character sheet makes|
    | because he is not  |                        | the game more accessible.  |
    | familiar with the  |                        | Adding the option to have  |
    | game.              |                        | the sheet updated to       |
    |                    |                        | reflect gameplay is useful |
    |                    |                        | to new players as well.    |
    +--------------------+------------------------+----------------------------+

*******************
User Stories
*******************

.. table::

    +--------------------------------------------------------------------------+
    | As Michelle the Dungeonmaster, I want to be able to uphold the integrity |
    | of our games by digitalizing the character sheets, and the dice rolling  |
    | in order to avoid players modifying their character sheets and stats     |
    | after their creation, or fudging the numbers of a bad roll.              |
    +--------------------------------------------------------------------------+

.. table::

    +--------------------------------------------------------------------------+
    | As John the Experience Player, I want to be able to use one program to   |
    | keep track of my character stats that responds to my digital dice rolls. |
    | I want my character sheet to immediately respond to new information.     |
    +--------------------------------------------------------------------------+

.. table::

    +--------------------------------------------------------------------------+
    | As Christopher the Newbie, I don't want to have to read a bunch of player|
    | manuals before I can play this game with my family. I want to be prompted|
    | for all the necessary information, and have my character sheet created   |
    | for me automatically based on what I put in.                             |
    +--------------------------------------------------------------------------+

.. table::

    +--------------------------------------------------------------------------+
    | As Christopher the Newbie, I also don't want to have to learn the math   |
    | behind different types of events, and would prefer if it could be        |
    | calculated for me, and updated in the appropriate spot on my character   |
    | sheet.                                                                   |
    +--------------------------------------------------------------------------+

*******************
Acceptance Stories
*******************

.. table::

    +--------------------------------------------------------------------------+
    | Scenario 1: Creating a Character                                         |
    | Given that all requested inputs have been entered,                       |
    | And none of the inputs have generated an error,                          |
    | When the user "rolls" for their skills,                                  |
    | Then their character sheet will automatically populated with the correct |
    | traits and skill values for their character.                             |
    +--------------------------------------------------------------------------+

