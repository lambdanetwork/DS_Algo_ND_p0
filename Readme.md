# Analysis per project

### Task0:
- Excluding the logic to parse a csv to python list. The big-O for this algorithm is **constant**
- In this code, the logic is just access the first element of `texts` and `calls`, and to access further information.

### Task1:
- The time-complexity for this algorithm is **O(n)**
- In this code, we have to loop each information on `texts` and `calls`, store it in dictionary
- finally once we have all the phone_number, we run `len` function to get the length of dictionary with 

### Task1:
![](screenshots/task1.png)
- The time-complexity for this algorithm is **O(n)**
- In this code, we have to loop each information on `texts` and `calls`, store it in dictionary
- finally once we have all the phone_number, we run `len` function to get the length of dictionary with 

### Task2:
- The time-complexity for this algorithm is **O(m*n)**
- In this code, we will create a dictionary, with key is phone_number, and value is duration.
- Then we loop each call to populate the dictionary:
  - if the phone is already registered in dictionary, we will add the duration with latest duration
  - if the phone is not already in dictionary, this duration will be the initial value
- Lastly once we get the dictionary of total_duration of each phone_number, we just need to loop one more time and find the longest duration
- So the complexity is based on the length of `calls.txt` and length of dictionary that we used to store duration


### Task3:
- The time-complexity for this algorithm is **O(n)**
- In this code, we will loop all the calls and we will classify into three different data
  1. All call that is made from (080) to (080)
  2. extract the area_code of this call and store it in `Set` to avoid duplicate
  3. extract the mobile_code of this call and store it in `Set` to avoid duplicate
- To answer question B, just get the length of calls.txt and the data from number 1 above.
- For answer of question A, we just print the phone number that we have stored in no.2, no.3 above


### Task4:
- The time-complexity for this algorithm is **O(m*n)**
- The hint to this question is telemarketer: 
  1. will not send nor receive text
  2. will make outgoing call but not incoming call

- To answer this question, we will create 3 dictionary, so that we can quickly access the data with O(1):
  1. text_outgoing_phone_number
  2. call_incoming_number -> list of outgoing number
  3. call_answering_number -> list of receving number

- Once we get the three dictionaries populated.
  1. loop from call_incoming_number 
     * for each number, make sure this number is not in text_outgoing_number (never send nor receive text)
     *  this number is not in call_answering_number, as in never receive a call