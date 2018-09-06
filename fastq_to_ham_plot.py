# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt
import seaborn as sns

f = open(CTGATC.fastq)

def getSeqs(fastq_file):
	#Parse a FASTQ for sequence identities and corresponding sequences
	seqences = {}
	return sequences

def hamDist(str1, str2):
   #Count the # of differences between equal length strings str1 and str2
   diffs = 0
   return diffs

#Make some kind of plot that contains the data you've calculated.
def graph(diffs):
	sns.set_style('ticks')
	sns.set_palette("husl")
	sns.distplot(diffs,axlabel="Hamming Distance Frequency")
	sns.despine(offset=10, trim=True)
	plt.show()
