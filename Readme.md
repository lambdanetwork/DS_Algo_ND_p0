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
- In this code, we will loop all the calls and we will first check that call is made from (080):
  1. if it's telemarketer just store the "140" to answer
  2. if it's area code, it startwith "(", try to extract the areacode
  3. if it's mobile-prefix, it has "space", get the first 4 digit
- To answer question B, we will get number of call from (080) to (080) divide by total call made from (080)

### Task4:
- The time-complexity for this algorithm is **O(n)** excluding the built-in function `difference` which has unknown complexity 
- The hint to this question is telemarketer: 
  1. will not send nor receive text
  2. will make outgoing call but not incoming call

- To answer this question, we will create 2 sets:
  1. non_tele -> number that fill the requirement for telemarketer as stated above
  2. outgoing -> all outgoing number

- Use built-in function Set.difference() to get all tele number, by applying outgoing.difference(non_tele)