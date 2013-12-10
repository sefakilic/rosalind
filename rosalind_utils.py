from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import generic_dna
from Bio.Alphabet import generic_rna

GENCODE = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}


def reverse_complement(seq):
    """Given a DNA sequence, return its reverse complement"""
    return Seq(seq).reverse_complement().tostring()

def translate(rna_seq):
    """Translate RNA sequence to amino acid sequence"""
    mrna = Seq(rna_seq, generic_rna)
    return mrna.translate().tostring()
    

def read_fasta(fasta_file):
    """Read fasta file and return the list of records, consisting of
    description and sequence"""
    handle = open(fasta_file)
    records = list(SeqIO.parse(handle, "fasta"))
    handle.close()
    return [(rec.description, rec.seq.tostring()) for rec in records]

def gc_content(seq):
    """GC content of the sequence"""
    return float(seq.count('C') + seq.count('G')) / len(seq)

def fac(n):
    if n <= 1:
        return 1
    return n * fac(n-1)

def choose(n,k):
    return fac(n) / fac(n-k) / fac(k)

def perm(n,k):
    return fac(n) / fac(n-k)

