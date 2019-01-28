"""
    This file is used to generate the "Hardcoded" arena.
    I was bored of hardcoding so I automated it.
    Kinda stupid I know.
"""

# Middle column
arenamid = [1, 3, 7, 12, 17]

# Left to Middle
arena1 = [[5, 10, 15], [2, 6, 11, 16], arenamid]

# Right to Middle
arena2 = [[9, 14, 19], [4, 8, 13, 18], arenamid]

# Arena
a = {}

node = {1: 60, 2: 180, 3: 210}

for ipart, part in enumerate([arena1, arena2]):  # Iterate over both paths
    for index, col in enumerate(part):  # iterate over each column
        if index < 2:  # Omit middle column
            for ic, cell in enumerate(col):
                a[cell] = {
                    30 + ipart * 120: part[index + 1][ic],  # Upper left is 30
                    330 - ipart * 120: part[index + 1][ic + 1],  # Lower left is 330
                }
                if ic != 0:  # If not the topmost
                    a[cell][90] = col[ic - 1]  # Add the above cell
                if ic != len(col) - 1:  # If not the bottommost
                    a[cell][270] = col[ic + 1]  # Add the below cell

for i, cell in enumerate(arenamid):  # Now middle
    a[cell] = {}
    if i != 0:  # If not the topmost
        a[cell][90] = arenamid[i - 1]  # Add the above cell
    if i != len(arenamid) - 1:  # If not the bottommost
        a[cell][270] = arenamid[i + 1]  # Add the below cell

# Linking
for n in a:
    for d, nei in a[n].items():
        a[nei][(d + 180) % 360] = n

from json import dumps as jdump

print(jdump(a, indent=4))
