#! /usr/bin/env python

from Bio.Nexus import Nexus
import os
import glob
import sys

file_list=[]

for nexus_file in glob.glob('*.nex'):
	file_list.append(nexus_file)
# print file_list

# file_list = ['modifiedaligned_ITS.nex', 'modifiedaligned_matK.nex', 'modifiedaligned_rbcL', 'modifiedaligned_trnL-trnF.nex']
#, 'aligned_ITS.nexus', 'aligned_matK.nexus', 'aligned_psbA-trnH.nexus', 'aligned_rbcL.nexus', 'aligned_trnL-trnF.nexus']


nexi =  [(fname, Nexus.Nexus(fname)) for fname in file_list]
# print nexi
combined = Nexus.combine(nexi)
# print combined
combined.write_nexus_data(filename=open('alligned_nuclear.nex', 'w'))



