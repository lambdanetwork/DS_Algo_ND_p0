"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

phoneNumber = {};

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        incoming_number = text[0];
        answering_number = text[1];
        phoneNumber[incoming_number] = True;
        phoneNumber[answering_number] = True;

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        incoming_number = call[0];
        answering_number = call[1];
        phoneNumber[incoming_number] = True;
        phoneNumber[answering_number] = True;
        
print ("There are {0} different telephone numbers in the records.".format(len(phoneNumber)))
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
