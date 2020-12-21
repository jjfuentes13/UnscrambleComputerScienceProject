"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

"""

"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

telephoneNumbers = set()

for textsNumber in texts:
    telephoneNumbers.add(textsNumber[0])
    telephoneNumbers.add(textsNumber[1])

for callsNumber in calls:
    telephoneNumbers.add(callsNumber[0])
    telephoneNumbers.add(callsNumber[1])

uniqueNumbers = len(telephoneNumbers)

# print(uniqueNumbers)

print("There are " + str(uniqueNumbers) + " different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
