#! /usr/bin/env python


import os
import glob
import sys
from Bio import AlignIO
import re



for alignment_file in glob.glob('*.fasta'):
	# print "BEGINNING WITH NEW ALIGNMENT FILE!!!!!"
	gene_name = alignment_file.split('_')
	gene = gene_name[0]
	print gene

	alignment = AlignIO.read(alignment_file, 'fasta')

	for record in alignment:
		name = record.name
		#name_split = name.split('_')
		#print name_split

		search_term = r'mtj\w[^_]*'

		position = re.search(search_term, name)

		start = position.start()
		end=position.end()

		new_name = name[start:end]

		record.id = new_name
		record.name = new_name
		record.description = new_name + '_'+ gene

	outfile_name = 'modified' + alignment_file
	AlignIO.write(alignment, outfile_name, 'fasta')
