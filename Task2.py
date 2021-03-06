"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
Worst case time complexity is O(n)
"""

callTime = {}

for call in calls:
    if call[0] in callTime:
        callTime[call[0]] += int(call[3])
    if call[0] not in callTime:
        callTime[call[0]] = int(call[3])
    if call[1] in callTime:
        callTime[call[1]] += int(call[3])
    if call[1] not in callTime:
        callTime[call[1]] = int(call[3])

longestCallTimeNumber = calls[0][0]

for time in callTime.keys():
    if callTime[time] > callTime[longestCallTimeNumber]:
        longestCallTimeNumber = time

print(str(longestCallTimeNumber) + " spent the longest time, " + str(callTime[longestCallTimeNumber]) + " seconds, on the phone during September 2016.")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

