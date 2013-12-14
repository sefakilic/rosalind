# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/dbpr/
"""

import sys
sys.path.append('../../')
from rosalind_utils import *
from Bio import ExPASy
from Bio import SwissProt

def dbpr():
    uniprot_id = open("rosalind_dbpr.txt").read().strip()
    handle = ExPASy.get_sprot_raw(uniprot_id)
    record = SwissProt.read(handle)

    # return the list of biological functions
    for ref in record.cross_references:
        if ref[0] == 'GO' and ref[2].startswith('P:'):
            print ref[2][2:]

    
