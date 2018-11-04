import os, fnmatch
import sys

def statistics(f):
	numOfChar = 0
	numOfWord = 0
	numOfLines = 0
	for line in f:
		wordSplit = line.split()
		numOfLines += 1
		for word in wordSplit:
			numOfWord += 1
			for char in word:
				if char.isalpha():
					numOfChar += 1
	return [numOfChar,numOfWord,numOfLines]

def hasWildcard(file):
	if '*' in file or '?' in file:
		return True
	else:
		return False 

cmd = sys.argv

input_filename = cmd[1]
ouput_filename = cmd[2]

inputFileList = []
pattern = input_filename
for file in os.listdir('.'):
	if fnmatch.fnmatch(file,pattern):
		inputFileList.append(file)
	if '?' in pattern and file == ''.join(pattern.split('?')):
		inputFileList.append(file)
f1 = open(ouput_filename,"w")
if len(inputFileList) == 0 and hasWildcard(input_filename):
	f1.write('No matching!')
elif len(inputFileList) == 0 and not hasWildcard(input_filename):
	try:
		f = open(input_filename)
	except OSError:
		f1.write('Opening file {} failed!'.format(input_filename))
		print('Opening file {} failed!'.format(input_filename))
		exit(0)
else:
	for inputfile in inputFileList:
		try:
			f = open(inputfile)
		except OSError:
			f1.write('Opening file {} failed!'.format(inputfile))
		else:
			figures = statistics(f)
			if hasWildcard(input_filename):
				f1.write("Name of file: %s.\n"%inputfile)
			f1.write('Number of characters: %s.\n'%figures[0])
			f1.write('Number of words: %s.\n'%figures[1])
			f1.write('Number of lines: %s.\n'%figures[2])
			f.close()
f1.close()


