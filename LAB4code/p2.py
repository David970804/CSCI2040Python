import sys
import fnmatch
cmd = sys.argv


def inline (keyphrase, line):
	lowerLine = line.lower()
	splitline = lowerLine.split()
	for i in range(len(splitline)):
		if splitline[i]==keyphrase[0].lower():
			count=0
			for j in range(len(keyphrase)):
				if splitline[i+j]==keyphrase[j].lower():
					count += 1
			if count == len(keyphrase):
				return True
	return False

filename = cmd[-1]
keyphrase = cmd[1:-1]
pattern = '*.*'
if keyphrase == [] or not fnmatch.fnmatch(filename,pattern):
	print('Not enough arguments!')
else:
	try:
		f=open(filename)
	except OSError:
		print('File does not exist!')
		exit(0)
	else:
		sentences=[]
		for line in f.readlines():
			if inline(keyphrase,line):
				print(line)
				sentences.append(line)
		if sentences==[]:
			print('No match!')
		f.close()
