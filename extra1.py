import crypt
import hashlib
import os
import sys
from sys import argv

PASSWD_DICT = argv[1]  # path to password dictionary
SHADOW_LOC = argv[2]  # path to shadow file


def main():

	if os.access(SHADOW_LOC, os.F_OK):  # Make sure Shadow file exists.
		shadowRead = open(SHADOW_LOC, mode='r')
		for line in shadowRead.readlines():
			user = line[0].strip()
			cryptPass = line[1].strip()
			crack_hash(cryptPass, user)
	else: # Alert if shadow file does not exist
		print("Shadow file does not exist at ", SHADOW_LOC)			

def crack_hash(cryptPass, user):
	if os.access(PASSWD_DICT, os.F_OK): #Make sure password dictionary file exists
		print("\nPassword Dictionary: ", PASSWD_DICT)
		passDict = open(PASSWD_DICT, 'r')
		ctype = cryptPass.split("$")[1]	
		passFound = False
		salt = cryptPass.split("$")[2]
		insalt = "$" + ctype + "$" + salt + "$"
		print("\n Cracking password for: ", user)
		for word in passDict.readlines():
			word.strip()
			word.strip('\n')
			cWord = crypt.crypt(word, insalt)
			if (cWord == cryptPass):
				passFound == True
				print("\nFound passwd for user ",user,": " , word)
				
		return
	else:
		print("Password Dictionary does not exist!")
		sys.exit()
		
if __name__ == '__main__':
	main()			
