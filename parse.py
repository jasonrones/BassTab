# Import Libraries
import sys

# All notes in range
notes = {
    1: "c,,",
    2: "cis,,",
    3: "d,,",
    4: "dis,,",
    5: "e,,",
    6: "f,,",
    7: "fis,,",
    8: "g,,",
    9: "gis,,",
    10: "a,,",
    11: "ais,,",
    12: "b,,",
    13: "c,",
    14: "cis,",
    15: "d,",
    16: "dis,",
    17: "e,",
    18: "f,",
    19: "fis,",
    20: "g,",
    21: "gis,",
    22: "a,",
    23: "ais,",
    24: "b,",
    25: "c",
    26: "cis",
    27: "d",
    28: "dis",
    29: "e",
    30: "f",
    31: "fis",
    32: "g",
    33: "gis",
    34: "a",
    35: "ais",
    36: "b",
    37: "c'",
    38: "cis'",
    39: "d'",
    40: "dis'",
    41: "e'",
    42: "f'",
    43: "fis'",
    44: "g'",
    45: "gis'",
    46: "a'",
    47: "ais'",
    48: "b'",
    49: "c''",
    50: "cis''",
    51: "d''",
    52: "dis''",
    53: "e''",
    54: "f''",
    55: "fis''",
    56: "g''",
    57: "gis''",
    58: "a''",
    59: "ais''",
    60: "b''",
}

Tunings = {}
# String: NoteID
Tunings["standard"] = {
    "string1": 32,
    "string2": 27,
    "string3": 22,
    "string4": 17
}

# Default is standard
default_tuning = Tunings["standard"]

# Read .tab file
file = sys.argv[1]
tabFile = open(file, 'r')
tabs = tabFile.read().split()

# Parse Tablature
lilyNotes = ''
for tab in tabs:
    tabParts = tab.split(".")
    string = "string" + str(tabParts[0])
    fret = tabParts[1]
    rhythm = tabParts[2]
    noteID = Tunings["standard"][string] + int(fret)
    lilyNotes = lilyNotes + notes[noteID] + rhythm + ' '

print(lilyNotes)

# Print notes to file
with open('notes.txt', 'w') as f:
    f.write(lilyNotes)