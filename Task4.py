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

outgoingCalls = []
incomingCalls = []
outgoingTexts = []
incomingTexts = []

for call in calls:
    outgoingCalls.append(call[0])
    incomingCalls.append(call[1])

for text in texts:
    outgoingTexts.append(text[0])
    incomingTexts.append(text[1])

telemarketers = [telemarketer for telemarketer in outgoingCalls if telemarketer not in incomingCalls]
telemarketers = [telemarketer for telemarketer in telemarketers if telemarketer not in outgoingTexts]
telemarketers = [telemarketer for telemarketer in telemarketers if telemarketer not in incomingTexts]
telemarketers.sort()

print("These numbers could be telemarketers: ")
for items in set(telemarketers):
    print(items)