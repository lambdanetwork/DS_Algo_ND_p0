"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

text_outgoing_phone_number = {};
call_incoming_number =  {};
call_answering_number =  {};

answer = set();

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        incoming_number = text[0];
        answering_number = text[1];
        text_outgoing_phone_number[incoming_number] = True;
        text_outgoing_phone_number[answering_number] = True;

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        incoming_number = call[0];
        answering_number = call[1];
        call_incoming_number[incoming_number] = True;
        call_answering_number[answering_number] = True;

for incoming_call in call_incoming_number:
    if not(incoming_call in text_outgoing_phone_number) and not(incoming_call in call_answering_number):
        answer.add(incoming_number)


print("These numbers could be telemarketers: {}".format(", ".join(answer)))
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

