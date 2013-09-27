import sys
import string

dict_words_counts = {}

file_to_count = open(sys.argv[1])

for line in file_to_count:
	line_list = line.split()
	for word in line_list: 
		word = string.strip(word, ",.?/;:\'\"[]{}-()&%$#!`")
		word = word.lower()
		dict_words_counts[word] = dict_words_counts.get(word, 0) + 1

unsorted_list = dict_words_counts.items()
for i in range(len(unsorted_list)): 
	unsorted_list[i] = unsorted_list[i][::-1]

sorted_list = sorted(unsorted_list)

for i in range(len(sorted_list)):
	print sorted_list[i][1], sorted_list[i][0]

#quicksort 