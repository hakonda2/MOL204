#!/usr/bin/python

filename="MySequences.fasta"

file=open(filename,'r')

for line in file:
	line=line.strip()
	if ">" in line:
		header=line
	elif (len(line)==0):
		continue
	else:
		seqlen=len(line)
		print(header + "\t" + str(seqlen))

