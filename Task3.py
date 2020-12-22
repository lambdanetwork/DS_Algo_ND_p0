"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
 
# helper ==========================
def get_mobile_prefix(str):
  mobile_prefixes = ['7','8','9'];
  if(mobile_prefixes.index(str[0]) >= 0):
    # if str start with oneof 7,8,9, get the first 4 digits
    prefix = str[0:4]
    return prefix
  else:
    return None

def get_area_code(str):
  if(")" in str):
    close_brace_index = str.find(")");
    # index 0 is always "("
    area_code = str[1:close_brace_index];
    return area_code;
  else:
    return None;
    
def is_telemarketer(str):
  if(str.startswith("140")):
    return true
    
# main ==========================
bangalore_area_code = set();
fixed_lines_in_bangalore = 0;
total_call_from_bangalore = 0;

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    total = len(calls)
    for call in calls:
      if call[0].startswith("(080)"):
        # add all call from bangalore
        total_call_from_bangalore +=1;
        if(call[1].startswith("(080)")):
          fixed_lines_in_bangalore+=1;

        # try to get the area code or mobile-prefixes
        area_code = get_area_code(call[1]);
        if(area_code is not None):
          bangalore_area_code.add(area_code)
          continue

        if(is_telemarketer(call[1])):
          bangalore_area_code.add("140")
          continue

        # else, must be mobile number, just get prefix
        bangalore_area_code.add(get_mobile_prefix(call[1]))

#FINALLY, sort the answer
bangalore_area_code = list(bangalore_area_code);
bangalore_area_code.sort();

        
#PART A
print("""The numbers called by people in Bangalore have codes: 
{}""".format("\n".join(bangalore_area_code)))
#PART B
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format((round(fixed_lines_in_bangalore / total_call_from_bangalore * 100, 2))))

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
