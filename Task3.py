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

areaCodes = set()

for prefix in calls:
  if prefix[0].find('(080)') != -1:
    if prefix[1][0] == "(":
      areaCodes.add(prefix[1][:prefix[1].find(")")+1])
    if prefix[1][0:3] == "140":
      areaCodes.add("140")
    if prefix[1][0] == "7" or prefix[1][0] == "8" or prefix[1][0] == "9":
      areaCodes.add(prefix[1][:4])

print("The numbers called by people in Bangalore have codes:")
print("\n".join(sorted(areaCodes)))

fromBangalore = 0 
toBangalore = 0

for fixedCalls in calls:
  if fixedCalls[0].find("(080)") != -1:
    fromBangalore += 1
    if fixedCalls[1].find("(080)") != -1:
      toBangalore += 1

callPercentage = (toBangalore/fromBangalore)*100
roundedPercentage = round(callPercentage,2)
print(str(roundedPercentage) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits

"""