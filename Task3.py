"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
 
# helper ==========================
def get_mobile_prefix(str):
  if(not(")" in str) and str.find("140") != 0):
    [prefix, number] = str.split(" ");
    return prefix
  else:
    return None

def get_fixed_line(str):
  if(")" in str):
    close_brace_index = str.find(")");
    area = str[1:close_brace_index];
    return area;
  else:
    return None;
    
# main ==========================
area_codes = set();
mobile_prefix = set();
fixed_lines_in_bangalore = 0;
total = 0;

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    total = len(calls)
    for call in calls:
      incoming_number = call[0];
      answering_number = call[1];
      area_incoming = get_fixed_line(incoming_number)
      area_answering = get_fixed_line(answering_number)
      if(area_incoming == "080" and area_answering == "080"):
        fixed_lines_in_bangalore+=1;

      mobile_incoming = get_mobile_prefix(incoming_number);
      mobile_answering = get_mobile_prefix(answering_number);

      if(area_incoming is not None):
        area_codes.add(area_incoming)
      if(area_answering is not None):
        area_codes.add(area_answering)
      if(mobile_incoming is not None):
        mobile_prefix.add(mobile_incoming)
      if(mobile_answering is not None):
        mobile_prefix.add(mobile_answering)

#PART A
print("The numbers called by people in Bangalore have codes: {}, {}".format(", ".join(area_codes), ", ".join(mobile_prefix)))
#PART B
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format((round(fixed_lines_in_bangalore / total * 100, 2))))

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
