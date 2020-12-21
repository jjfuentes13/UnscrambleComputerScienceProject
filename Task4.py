"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

excludedNumbers = set()
potentialTelemarketer = set()

for textNumbers in texts:
    excludedNumbers.add(textNumbers[0])
    excludedNumbers.add(textNumbers[1])

for callNumbers in calls:
    excludedNumbers.add(callNumbers[1])
    
for call in calls:
    if not call[0] in excludedNumbers:
        potentialTelemarketer.add(call[0])

potentialTelemarketer = list(potentialTelemarketer)
telemarketerNumber = sorted(potentialTelemarketer)

print("These numbers could be telemarketers:")
print("\n".join(sorted(telemarketerNumber)))

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

