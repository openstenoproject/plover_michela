# Plover Michela

Michela (Italian system) support for Plover.

This include support for compatible [MIDI-keyboard based machines](https://it.wikipedia.org/wiki/Macchina_Michela) (both 2 and 3+ octaves variants).


## Documentation

For details about the theories and the contents of the dictionaries (in Italian), see:
https://github.com/Sillabix/Plover-Michela


## Release history

### 2.0.0

* The theory has been updated to take full advantage of the inflectional suffixes
  based on grammar rules recently introduced. In particular:
  - The rules to indicate the endings of the words "e" and "i" have been modified
    to avoid conflicts caused by the previous diphthong-based system (for a full
    description refer to the Michela theory manual on GitHub).
  - The numeric dictionary' strokes have been changed (from `IU` to `Uu`) in
    order to avoid a series of possible conflicts.
  - The syllabic finger-spelling system has been modified: it now uses the
    combination `RX` and `RXI` for capital letters.
* Numerous definitions relating to prefixes / suffixes and formatting commands
  have been amended.

### 1.0.1

* fix wordlist: drop duplicate entries

### 1.0.0

* drop phonetic/orthographic differentiation, only support one "Michela" system
* add support for 2 variants of the Michela Keyboard machines

### 0.1.6

* fix a few entries in the orthographic dictionary

### 0.1.5

* move punctuation and spacing entries to a dedicated dictionary
* add more entries to the commands dictionary
* add support for orthographic theory
* fix conflicting dictionary entries

### 0.1.4

* update main dictionary and split it into three parts: main, numbers, and commands

### 0.1.3

* fix undo stroke (use `U`, not `X`)

### 0.1.2

* add dictionaries
