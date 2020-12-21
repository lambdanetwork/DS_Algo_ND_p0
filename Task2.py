"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
phone_duration = {};

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        incoming_number = call[0];
        answering_number = call[1];
        duration = call[3]

        if(incoming_number in phone_duration):
            phone_duration[incoming_number] = phone_duration[incoming_number] + int(duration)
        else:
            phone_duration[incoming_number] = int(duration);
        
        if(answering_number in phone_duration):
            phone_duration[answering_number] = phone_duration[answering_number] + int(duration)
        else:
            phone_duration[answering_number] = int(duration);
        
max_duration = 0;
max_phone_number = [];
for phone_number, duration in phone_duration.items():
    if(duration > max_duration):
        max_duration = duration;
        max_phone_number = [phone_number];
    elif(duration == max_duration):
        max_phone_number.append(phone_number);


for phone_number in max_phone_number:
    print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(phone_number, max_duration))
    
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

