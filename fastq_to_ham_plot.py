# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt

f = open('CTGATC.fastq', 'r')

def getSeqs(fastq_file):
	#Parse a FASTQ for sequence identities and corresponding sequence
	lines = fastq_file.read().splitlines()
	sequences = {}
	dict_key = 0
	i = 0
	while i < len(lines):
		if lines[i][0:6] == '@SN640':
			line_arr = lines[i].split(':')
			eleNum = len(line_arr)
			s1 = line_arr[eleNum - 1]
			s2 = lines[i+1]
			concat = s1 + s2
			sequences[dict_key] = concat
			dict_key = dict_key + 1
		i = i + 1
	return sequences

def hamDist(str1, str2):
   #Count the # of differences between equal length strings str1 and str2
   diffs = 0
   return diffs

#Make some kind of plot that contains the data you've calculated.
#plt.show()
