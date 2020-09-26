#Python Program to sort 4471 polls

#IMPORTANT
#To read input, must be given as text file with the title at the tipe, then one name per line followed by one number per line
#Also must make sure every student's name will match exactly.
#Note text files must have no extra space at the end

#TODO: for some reason it prints transposed. 

#Example
#presentation1
#Bob
#Steve
#1
#2
#Where bob gave 1 and steve 2

#####################################

#Installation in terminal
#pip3 install python3
#pip3 install xlsxwriter
#pip3 install numpy

#run program
#cd to local directory 
#python3 poll_sorting.py

#REQUIRES
#updated list of exact lowercase student names. AKA take their username on piazza and put it in the name array
#appropriately formatted text files in the local directory (or given with path if you want them in their own folder like I have)
#updated list of text files in files array

#TEXT FILE FORMATTING
#name the file whatever you like and update this file's files array to match
#Inside each file:
#presentation name
#name1
#name2
#name...
#namex
#vote for student 1
#vote for student 2
#...
#vote for student x

#OUTPUT
#outputs an xlms doc you can open with a fileviewer of your choice

import xlsxwriter
#import pandas as pd
#import matplotlib.pyplot as plt 
import numpy as np 


def read_names(lines):
	names = []
	while not lines[0].isdigit(): 
		n = lines.pop(0)
		names.append(n)
	return names
		
def read_vals(lines):
	vals = []
	while len(lines) > 0:
		n = lines.pop(0)
		vals.append(n)
	return vals

def fill_column(file, column):
	#Get names and values, in order, from file
	f = open(file)
	lines = f.read().splitlines()
	column_name = lines.pop(0)
	names = read_names(lines)
	vals = np.array(read_vals(lines))
	#let us know if there are not the same number of values and names in a text file
	if len(vals) != len(names):
		print("text file size error in")
		print(column_name)
	#Place column name inside array
	X[0,column] = column_name
	#Place vals into 2-D array
	i = 0
	for val in vals:
		name = names[i]
		row = np.where(X[:,0] == name.lower())
		X[row, column] = val
		i = i + 1

#let x be the pd.dataframe we are filling all data into
# instantiate X as a students + 1 x presentations + 1 matrix
X = np.zeros((95, 46),dtype=np.dtype('U100'))

#lsit of student names. "axis, "name1", ..., "nameN", "averages: "
names = [
	'axis','anden acitelli','austin anderson','shayan','hadeel atala',
	'will bartlett','brenden boswell','sean bower','ali brugh','eric robert bulgrin','diana carl',
	'chi','zach','drew delap','alex demos','chris','kazuma ervin',
	'joseph feltz','brian fissel','rylee fraser','william frasher','caleb goddard','jason guo',
	'rayan hamza','pragya handa','nicholas harvey','zhizhou he','jared holderby','justin holderby',
	'amy','jiantang huang','kyle hustek','gary isufi','michael izzo','konrad kappel',
	'ben keltos','brenden kemmerling','shakia khan','dylan klingensmith','sanja','kelly kuang',
	'jacob han leblanc','jia-hsin lin','lyle londraville','andrew lubinger','zachary mack','philip massouh',
	'grace mckenzie','saahil mehta','jeffrey lee messinger','sean michaels','sara miskus','vannaroth ngoc',
	'hans ooms','derek opdycke','lufei ouyang','yufei pan','raleigh potluri','james',
	'shamik raje','sean riley','michael rizzoni','emily robinson','joey rosa','abhishek salandri',
	'ralph sanders','ryan schneider','noah sediqe','brian seeds','parshva shah','gabriel shams',
	'zilin shao','nicholas shiffer','charlie song','brooke speas','evan standerwick','sam',
	'aditya tewary','natalie thomas','eli vosniak','jared walker','meghan walther','adam wang',
	'cat wang','deepak warrier','jack weiner','trevor white','alex williams','emily wise',
	'fengze wu','chenwei','xin xu','anthony yeretzian','andy zawada','averages: '
]
X[:,0] = names

column = 1 #global var signifiying which column is next to be filled


#Input the well formatted txt files to be read
files = [
'polltxt/DataPrivacy.txt', 'polltxt/Encryption.txt', 'polltxt/IIS.txt', 'polltxt/LegacySystems.txt', 'polltxt/MDRKS.txt',
'polltxt/socialEngineering.txt', 'polltxt/HardwareLevelExploits.txt', 'polltxt/IOTB.txt', 'polltxt/ITWMFA.txt', 'polltxt/MBAOR.txt',
'polltxt/WhiteHH.txt', 'polltxt/SE-B.txt', 'polltxt/CyberWarfare.txt', 'polltxt/SEDS.txt', 'polltxt/NationalSecurityThreats.txt', 'polltxt/Steganography.txt',
'polltxt/Privacy.txt', 'polltxt/Deepfake.txt', 'polltxt/ContainerSecurity.txt', 'polltxt/xssAttacks.txt', 'polltxt/DatabaseSecurity.txt', 'polltxt/CryptoCurrency.txt',
'polltxt/PhishingASE.txt', 'polltxt/GameCheating.txt', 'polltxt/OnlineTransactionSecurity.txt', 'polltxt/PasswordManagers.txt', 'polltxt/THFIS.txt',
'polltxt/ASOMP.txt', 'polltxt/NRIIA.txt', 'polltxt/DDoSAttacks.txt', 'polltxt/UnsafeTech.txt', 'polltxt/SmartphoneSecurity.txt', 'polltxt/CDPI.txt',
'polltxt/ReverseEng.txt', 'polltxt/CloudSecurity.txt', 'polltxt/Steg1245.txt', 'polltxt/PhysicalEncryptionDevices.txt', 
'polltxt/GarminRansomwareAttack.txt', 'polltxt/CPASS.txt', 'polltxt/Blockchain.txt', 'polltxt/SideChannel.txt'
]

#for every presentation, file, put in matrix
for file in files:
	fill_column(file, column)
	column = column + 1

#name last two rows
X[0,42] = 'A/A- percentage'
X[0,43] = 'Number of votes'

# add a column for each student's vote total
for row in range(1,95):
	votes = 0
	for col in range(1, 41):
		#if slot has valid vote, add to total
		if X[row,col].isdigit():
			votes = votes + 1
	X[row,43] = votes

# add a column for each student's % of A's given
for row in range(1,95):
	aVotes = 0
	for col in range(1,41):
		if X[row,col].isdigit() and int(X[row,col]) <= 2:
			#if we find an a, increase A count
			aVotes = aVotes + 1
	votes = int(X[row, 43]) #retrieve the already caluclated votes per this student
	if votes > 0:
		X[row, 42] = str(np.ceil(aVotes/votes * 100)) + '%'
	else:
		X[row,42] = 'Didn\'t vote'

# add a row for each presentations poll average 
for col in range(1,42):
	sumOfVals = 0
	votes = 0
	for row in range(1,95):
		if X[row,col].isdigit():
			votes = votes + 1
			sumOfVals = sumOfVals + int(X[row,col])
	if votes > 0:
		X[94, col] = sumOfVals/votes

#WHY DOES THIS PRINT TRANSPOSED? Unclear.
#print to excel sheet
#df = pd.DataFrame(X).T
#df.to_excel(excel_writer = "C:/Users/trevorwarthman/Desktop")
workbook = xlsxwriter.Workbook('polls-printout.xlsx')
worksheet = workbook.add_worksheet()

row = 0

for col, data in enumerate(X):
	worksheet.write_column(row,col,data)

workbook.close()
