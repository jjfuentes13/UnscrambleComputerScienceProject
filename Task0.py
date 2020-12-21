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
"""
Worst case time complexity is O(1)
"""
print("First record of texts, " + texts[0][0] + " texted " + texts[0][1] + " at the time of " + texts[0][2])

print("Last record of calls, " + calls[-1][0] + " called " + calls[-1][1] + " at the time of " + calls[-1][2] + " , and lasting " + calls[-1][3] + " seconds")


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

