#!/usr/bin/env python
import crypt
import hashlib
import os 
import sys
from sys import argv

PASSWD_DICT = argv[1]  # path to password dictionary
SHADOW_LOC = argv[2] # path to shadow file

def main():


	if os.access(SHADOW_LOC, os.F_OK): #Make sure Shadow file exists.
		shadowRead = open(SHADOW_LOC, mode='r')
		for line in shadowRead.readlines(): #Make sure user exists
			line = line.strip() #Remove blank space
			line = line.replace("\n","").split(":")
			if line[1] not in ['x','*','!']:
				user = line[0].strip()
				cryptPass = line[1].strip()
				#print "cryptPass ", cryptPass
				#print "line ", line
				crack_hash(cryptPass, user)
				shadowRead.readlines()
			line = shadowRead.readlines()
	else: # Alert if shadow file does not exist
		print "Shadow file does not exist at ", SHADOW_LOC			
def crack_hash(cryptPass, user):
	if os.access(PASSWD_DICT, os.F_OK): #Make sure password dictionary file exists
		print "\nPassword Dictionary: ", PASSWD_DICT
		passDict = open(PASSWD_DICT, 'r')
		ctype = cryptPass.split("$")[1]
		#print "ctype: ", ctype
		passFound = False
		salt = cryptPass.split("$")[2]
		#print "salt: ", salt
		insalt = "$" + ctype + "$" + salt + "$"
		#print "insalt: ", insalt
		print "\n Cracking password for: ", user
		for word in passDict.readlines():
			word = word.replace('\n','')
			word = word.replace('\t','')
			#print "WORD: ", word
			cWord = crypt.crypt(word, insalt)
			#print "cWord: ", cWord , " cryptPass: ", cryptPass
			if (cWord == cryptPass):
				passFound == True
				print "\nUsername", user
				print "Password", word
				return True
		if (passFound == False):
			print "Password not in dictionary file", PASSWD_DICT	
			return False
	else:
		print "Password Dictionary does not exist!"
		
if __name__ == '__main__':
	main()			