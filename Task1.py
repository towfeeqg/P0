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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
uniqueNumbers = []

for rows in texts:
    sendingTextNumber = rows[0]
    receivingTextNumber = rows[1]

    if sendingTextNumber not in uniqueNumbers: uniqueNumbers.append(sendingTextNumber)
    if receivingTextNumber not in uniqueNumbers: uniqueNumbers.append(receivingTextNumber)

for rows in calls:
    sendingCallNumber = rows[0]
    receivingCallNumber = rows[1]

    if sendingCallNumber not in uniqueNumbers: uniqueNumbers.append(sendingCallNumber)
    if receivingCallNumber not in uniqueNumbers: uniqueNumbers.append(receivingCallNumber)
    
print(f"There are {len(uniqueNumbers)} different telephone numbers in the records.")
