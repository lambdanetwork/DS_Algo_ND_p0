"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

unique_tele_nums = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        unique_tele_nums.add(text[0])
        unique_tele_nums.add(text[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        unique_tele_nums.add(call[0])
        unique_tele_nums.add(call[1])
        
print ("There are {0} different telephone numbers in the records.".format(len(unique_tele_nums)))
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
