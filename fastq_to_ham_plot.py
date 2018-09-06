# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt
import seaborn as sns

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
	if len(str1) == len(str2):
		for i in range(len(str1)):
			if str1[i] != str2[i]:
				diffs = diffs +1
	return diffs

#Make some kind of plot that contains the data you've calculated.
def graph(diffs):
	sns.set_style('ticks')
	sns.set_palette("husl")
	sns.distplot(diffs,axlabel="Hamming Distance Frequency")
	sns.despine(offset=10, trim=True)
	plt.show()

orig_data = getSeqs(f)
#orig_data = {"#1":"AAGGTTNTC","#2":"ATGTTTNTC", "#3":"ATGTTTGTC"}
seq_data = list(orig_data.values())
output = list()
for j in range(len(seq_data)):
		for i in range((j+1),len(seq_data)):
			if seq_data[i] != seq_data[j]:
				output.append(hamDist(seq_data[j],seq_data[i]))
graph(output)

