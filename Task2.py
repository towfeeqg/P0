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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

dict = {}

for call in calls:
    if call[0] not in dict:
        dict[call[0]] = int(call[3])
    elif call[1] not in dict:
        dict[call[1]] = int(call[3])
    elif  call[0] in dict:
        dict[call[0]] = dict.get(call[0]) + int(call[3])
    elif  call[1] in dict:
        dict[call[1]] = dict.get(call[1]) + int(call[3])

print(f'{max(dict, key = dict.get)} spent the longest time, {max(dict.values())} seconds, on the phone during September 2016.')