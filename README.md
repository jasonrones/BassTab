# Introduction

[lilypond](http://lilypond.org) is a powerful system for typesetting beautiful music.

As a bass player I sometimes want to transcribe a piece into notation and/or tablature.  Not
being an expert at converting from string+fret positions on the bass into standard notation,
I wanted to be able to enter music by giving string+fret together with tuning information to lilypond.


## Simplified Tab Notation
This project using simplified tab notation from [jeremy9959's BanjoTab project](https://github.com/jeremy9959/BanjoTab)

Each note is entered as (string).(fret).(duration) - So 2.0.4 means a quarter note on
the open second string.

### Notation Not Supported
* Dotted Notes
* Triplets
* Articulations

## Running Script

```bash
$ python3 parse.py tab.txt
```

The output will be written to notes.txt and the contents can be copy/pasted into your .ly (LilyPond) file.