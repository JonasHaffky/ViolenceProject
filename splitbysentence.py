#!/usr/bin/python3

import sys, getopt
from nltk.tokenize import sent_tokenize

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print ('splitbysentence.py -i <inputfile> -o <outputfile>')
		sys.exit(1)

	for opt, arg in opts:
		if opt == '-h':
			print ('splitbysentence.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	if (len(sys.argv)==1):
		print ('splitbysentence.py -i <inputfile> -o <outputfile>')
		sys.exit(1)

	fileInput = open(inputfile)
	fileOutput = open(outputfile,"a")

	data = fileInput.read()
	newdata = sent_tokenize(data)

	fileOutput.write('')
	for sentence in newdata:
		fileOutput.write(sentence + '\n')

if __name__ == "__main__":
	main(sys.argv[1:])
