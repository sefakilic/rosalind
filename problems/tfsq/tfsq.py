# -*- coding: utf-8 -*-

"""
http://rosalind.info/problems/tfsq/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

def tfsq():
    handle = open("rosalind_tfsq.txt")
    records = SeqIO.parse(handle, "fastq")
    output_handle = open("rosalind_out.txt", 'w')
    SeqIO.write(records, output_handle, "fasta")
    
