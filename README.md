# jusawi-ko
Jusawi-ko is a Discord bot designed to help with managing Project Moon Tabletop Roleplay Game characters.
Currently uses the Community Rules 3.0

Originally designed for Kawazoi Office, with love. ❤️

## Does not yet support Mysteries nor Distortions!

## Features

### Attributes

Tracks, updates, and maintains character attributes:

- Stats
  - Fortitude
  - Prudence
  - Justice
  - Charm
  - Insight
  - Temperance
- Derived Attributes
  - Heath Points
  - Stagger Threshold
  - Sanity Points
  - Light
  - Attack Modifier
  - Evade Modifier
  - Block Modifier
  - Equipment Rank Limit
  - Tool Slots

### Equipment & Skills

Supports custom-made equipment and skills, if legal in the Character Sheet.

### Combat Speed Tracking

Tracks the Speed of all combatants. Also has an optional 'Round 0' for surprise attacks.

### Challenge Rolling

Supports challenge rolls.

# Build Instructions
1. Use `virtualenv` to make a `venv` folder in the repo. Place all the following files into `/venv/`
2. Acquire Google authentication: Google application credentials, service account credentials, and a token
3. Acquire a Discord token
4. `touch` or otherwise create two files, named `activeplayer` and `playerdata`
