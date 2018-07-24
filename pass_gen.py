"""
30-05-2018
Created by Souvik
"""

import random
import sys
import string

#constants
easyConst = 'e'
mediumConst = 'm'
difficultConst = 'd'
intList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolList = ['!', '@', '#', '$', '%', '^', '&', '*']

def main(userResponse):
        #userResponse = input("You are about to generate password\nEasy - press " + easyConst + "\nMedium - press " + mediumConst + "\nDifficult - press " + difficultConst + "\n")
        len = lengthGen(userResponse)
        return(passGen(len, userResponse))

def lengthGen(userResponse):
	if userResponse == easyConst:
		len = random.choice([5, 6])
	elif userResponse == mediumConst:
		len = random.randrange(7, 9 + 1)
	elif userResponse == difficultConst:
		len = random.randrange(10, 14 + 1)
	else:
		print("Invalid input")
		sys.exit()
	return(len)

def passGen(len, userResponse):
	if userResponse == easyConst:
		password = ""
		for i in range(len):
			password += random.choice(list(string.ascii_letters[:26]))
		return(password)
	elif userResponse == mediumConst:
		password = ""
		myList = list(range(len))
		pos1 = random.choice(myList)
		for i in range(len):
			if i == pos1:
				password += random.choice(list(string.ascii_letters[26:]))			# atleast one upper case
			else:
				password += random.choice(list(string.ascii_letters))
		return(password)
	elif userResponse == difficultConst:
		password = ""
		myList = list(range(len))
		pos1 = random.choice(myList)
		myList.remove(pos1)
		pos2 = random.choice(myList)
		myList.remove(pos2)
		pos3 = random.choice(myList)
		for i in range(len):
			if i == pos1:
				password += random.choice(list(string.ascii_letters[26:]))			# atleast one upper case
			elif i == pos2:
				password += random.choice(intList)						# atleast one number
			elif i == pos3:
				password += random.choice(symbolList)					        # atleast one symbol
			else:
				password += random.choice(list(string.ascii_letters) + intList + symbolList)
		return(password)
