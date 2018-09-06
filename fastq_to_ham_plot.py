# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

#import matplotlib.pyplot as plt

f = open(CTGATC.fastq)
def getSeqs(fastq_file):
	#Parse a FASTQ for sequence identities and corresponding sequences
	seqences = {}
	return sequences

def hamDist(str1, str2):
   #Count the # of differences between equal length strings str1 and str2
	diffs = 0
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			diffs = diffs +1
	return diffs

orig_data = getSeqs(f)
#orig_data = {"#1":"AAGGTTNTC","#2":"ATGTTTNTC", "#3":"ATGTTTGTC"}
seq_data = list(orig_data.values())
output = list()
for j in range(len(seq_data)):
		for i in range((j+1),len(seq_data)):
			if seq_data[i] != seq_data[j]:
				output.append(hamDist(seq_data[j],seq_data[i]))

#print(output)

#Make some kind of plot that contains the data you've calculated.
#plt.show()
