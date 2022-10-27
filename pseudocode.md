### Iteration 1 - Core

This iteration covers core functionality for leveling, combat, and character attributes.

#### Feature: Create a Character

> As a character I want to have a name so that I can be distinguished from other characters

- can get and set Name

- [x] Make sure we have a character
- [x] Can we set a name for a character

#### Feature: Alignment

> As a character I want to have an alignment so that I have something to guide my actions

- can get and set alignment
- alignments are Good, Evil, and Neutral

- [x] Is there an alignment
- [x] Set alignment to one of the options

#### Feature: Armor Class & HP

> As a combatant I want to have an armor class and HP so that I can resist attacks from my enemies

- has an Armor Class that defaults to 10
- has 5 HP by default

- [x] Is there an armor class
- [x] Can we set a value to the armor class
- [x] Does the armor class have HP
- [x] Can we assign the number of HP

#### Feature: Character Can Attack

> As a combatant I want to be able to attack other combatants so that I can survive to fight another day

- roll a 20 sided die (don't code the die)
- roll must meet or beat opponents armor class to hit
- a natural roll of 20 always hits

- [x] Set a dice variable to a chosen number
- [x] Create a conditional based on armor class and d20 roll
- [x] Create a conditional that a d20 roll of 20 always hits

#### Feature: Character Can Be Damaged

> As an attacker I want to be able to damage my enemies so that they will die and I will live

- If attack is successful, other character takes 1 point of damage when hit
- If a roll is a natural 20 then a critical hit is dealt and the damage is doubled
- when HP are 0 or fewer, the character is dead

- [x] Deal 1 point of damage when roll is greater than armor
- [x] Deal 2 points of damage when roll is 20
- [x] Target "dies" when enough damage is dealt

#### Feature: Character Has Abilities Scores

> As a character I want to have several abilities so that I am not identical to other characters except in name

- Abilities are Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma
- Abilities range from 1 to 20 and default to 10
- Abilities have modifiers according to the following table

| Score | Modifier | Score  | Modifier | Score  | Modifier | Score  | Modifier |
| :---: | :------: | :----: | :------: | :----: | :------: | :----: | :------: |
| **1** |    -5    | **6**  |    -2    | **11** |    0     | **16** |    +3    |
| **2** |    -4    | **7**  |    -2    | **12** |    +1    | **17** |    +3    |
| **3** |    -4    | **8**  |    -1    | **13** |    +1    | **18** |    +4    |
| **4** |    -3    | **9**  |    -1    | **14** |    +2    | **19** |    +4    |
| **5** |    -3    | **10** |    0     | **15** |    +2    | **20** |    +5    |

#### Feature: Character Ability Modifiers Modify Attributes

> As a character I want to apply my ability modifiers improve my capabilities in combat so that I can vanquish my enemy with extreme prejudice

- add Strength modifier to:
  - attack roll and damage dealt
  - double Strength modifier on critical hits
  - minimum damage is always 1 (even on a critical hit)
- add Dexterity modifier to armor class
- add Constitution modifier to HP (always at least 1 hit point)

#### Feature: A Character can gain experience when attacking

> As a character I want to accumulate experience points (xp) when I attack my enemies so that I can earn bragging rights at the tavern

- When a successful attack occurs, the character gains 10 experience points

- [x] On successful attack, xp for the player that made the attack goes up by 10

#### Feature: A Character Can Level

> As a character I want my experience points to increase my level and combat capabilities so that I can bring vengeance to my foes

- Level defaults to 1
- After 1000 experience points, the character gains a level
  - 0 xp -> 1st Level
  - 1000 xp -> 2nd Level
  - 2000 xp -> 3rd Level
  - etc.
- For each level:

  - HP increase by 5 plus Con modifier
  - 1 is added to attack roll for every even level achieved

  - [x] Does the lvl attribute exist
  - [x] For every 1000 xp the player gains, the player levels up 1 level
  - [x] Increase hp on level up

### Iteration 2 - Classes

Classes that a character can have.

#### Feature: Characters Have Classes

> As a player I want a character to have a class that customizes its capabilities so that I can play more interesting characters

##### Ideas

- changes in HP
- changes in attack and damage
- increased critical range or damage
- bonuses/penalties versus other classes
- special abilities
- alignment limitations

##### Samples

> As a player I want to play a Fighter so that I can kick ass and take names

- attacks roll is increased by 1 for every level instead of every other level
- has 10 HP per level instead of 5

> As a player I want to play a Rogue so that I can defeat my enemies with finesse

- does triple damage on critical hits
- ignores an opponents Dexterity modifier (if positive) to Armor Class when attacking
- adds Dexterity modifier to attacks instead of Strength
- cannot have Good alignment

> As a player I want to play a Monk so that I can enjoy being an Asian martial-arts archetype in a Medieval European setting

- has 6 hit point per level instead of 5
- does 3 points of damage instead of 1 when successfully attacking
- adds Wisdom modifier (if positive) to Armor Class in addition to Dexterity
- attack roll is increased by 1 every 2nd and 3rd level

> As a player I want to play a Paladin so that I can smite evil, write wrongs, and be a self-righteous jerk

- has 8 HP per level instead of 5
- +2 to attack and damage when attacking Evil characters
- does triple damage when critting on an Evil character (i.e. add the +2 bonus for a regular attack, and then triple that)
- attacks roll is increased by 1 for every level instead of every other level
- can only have Good alignment

### QUESTIONS

- why does the or operator not work

### more psuedocode

- if target has certain ability
  - for str
    - change the attack value of the character for strength modifier and double the strength modifier on crits
    - change the crit minimum dmg to 1
  - for dex
    - up the armor to a higher or lower value based on the modifier (example: armor = 10 without modifier. armor = 15 if strength is = 20 )
  - for const adds
