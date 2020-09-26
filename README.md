# poll_sort
Small python program to sort polls for CSE 4471

Input: text files of format in this local folder. AKA:
presentation-title
name1
...
namex
vote in integer form 1
...
vote in integer form x

Output: 
Transposed matrix of results, average score, number of votes, number of votes < 2 (A's and A-'s) in the form of an xlsm doc.

To use install:
python3
pip3 install numpy
pip3 install xlsmwriter

to use replace:
names array with appropriate names
.txt docs with appropriately formatted poll results.
