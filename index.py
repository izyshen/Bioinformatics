print ("Introductory Bioinformatics Experiment")

#SFTPA1 genome taken from NCBI RefSeq
SFTPA1 = "GACTTGGAGGCAGAGACCCAAGGCTGGAGGCTCTGTGTGTGGGTGAGTTTAGCCCCATCCCCTAGGTGTTCTCCAGCTTGAGGATCGCAGGCAGAGAGGACCAGCCCAGCAGCCACAGGCCTGACCAAAGCCCAGGCTGGGAAGGAGGGCAACTCCCCATTTTCCACTGGGAGGTGTTTCACAGCACAGTCAACATAGGTGACCTGCAAAGATCCTCATGTTTGTTATTTTCTTTGGCCAGATCCATCCCTACAGGGTTCAGCAGGGCCTACAGGAGGGGCAGTGAGAGAACAGACCCCAAAAAGAAAGGGGACTCCATGACTGACCACCTTGAGGGGGGCCAGGCTGCGGGCCCCGTTCATCTTTTTTCATTCTCAGGTCGCTGATTTCTTGGAGCCTGAAAAGAAAGTAACACAGCAGGGATGAGGACAGATGGTGTGAGTCAGTGAGTGAGTGACCTGACTAATAGCCTGGGAGGGACAGGGCAGGTTTTCTGCAGAGCACGGAAGATTCAGCTGAAGTCAGAGAGGTGAAGCCAGTTTCCCAGGGTAACATAGTGAGGCACTGAAAGAAAGGAGACTGCACTGGAGCCCAGGTCCCCGGGCTCCCCAGAGCTCCTTACTCTTCCTCCTCCTCAGCAGCCTGGAGACCCCACAACCTCCAGCCGGAGGCCTGAAGCATGAGGCCATGCCAGGTGCCAGGTGATGCTGGGAATTTTCCCGGGAGCTTCGGGTCTTCCCAGCACTCTGGTCTCGCCCGCCCTGCCTCTCGGGCTCTGCCCAGCTTCCTGAGTCCTGACAGAGCACAGTGGGGGAGATGTTGGCAGAGGTGGCAGATGGGCTCACGGCCATCCCTCCTGCAGGAGCAGCGACTGGACCCAGAGCCATGTGGCTGTGCCCTCTGGCCCTCAACCTCATCTTGATGGCAGCCTCTGGTGCTGTGTGCGAAGTGAAGGACGTTTGTGTTGGAAGCCCTGGTATCCCCGGCACTCCTGGATCCCACGGCCTGCCAGGCAGGGACGGGAGAGATGGTCTCAAAGGAGACCCTGGCCCTCCAGGTACTGTGCTGCAGACCCCACCCTCAGCTGAGGGACACAGACCCCTTTTCAGGAGGCCCATCTGTCCAGGCCCCTAGGCTGTGGGCCATAGTGAGCTGGGGGCTATAGTAAGCTGGGTGGGACTTCAGTCTGCAGGGCTGGTGGGTTCCTGGGGCCCTTATGATGGCGCATCCTGGAGAGTCTGTCCTCATAGTGCCCACGGAGTGATAGAGTGATAGCTGAGCCAGCCCTGGTGATAATGGGCATCGAGTCTCACTAGCTCCAACCAGTTGTGGGTGACAGATCCTACACATCCATGTCTCTTTTCTCTGCAGGCCCCATGGGTCCACCTGGAGAAATGCCATGTCCTCCTGGAAATGATGGGCTGCCTGGAGCCCCTGGTATCCCTGGAGAGTGTGGAGAGAAGGGGGAGCCTGGCGAGAGGGGCCCTCCAGGTGAGCAGGGTGGGGCAGGTGGGCAGTGGAAACATGGGCACAGCGACCCTGAAGTCAGTTACACGGGGATGATGGGGATCAGACAAACCCTACAGGTTCCCCAAGGGCATTTGGCTCAACCTAAGTAAGAGAGGATAAGCTTGAGGGAGAAAGCTGAGGTGTCTGGGGAGTGTGGTCACAATTCAGGGAAAGGCAGGTGTGGGAAGTCCTCCGTGCCTCATGACCACCGATGGGGACACACTGAGTCAGGTGTGGGATGAGGGACAGCACTGGGAGGCAGGGGAGGCATGTCCTGGGATGGAGGCCCTGGGGGCTGTCTGAAGGGTGAATGCGGACGAGGCATCCAGACAGACGGTGTGATCAGGAGCCCCACAGACAGAGGGGAACTTTGAAGCTCAGAGCGGTAAGCAAGTCCATCAGGGCAGTGCAGAGAGCATCATGCTTGCCCTTGGTGGAGGGTGCGGGAGAGGGACTTGCCCCACAGAGGCGGGCAGACAGAACCCCTCGAGGGACAGAGCAGGAAAGAGGACAAGGGGTGGGGGTCTCAGCAGGGGCAAGGCTTCACTAAAGAATAGGGGACCACGGGGTGTGGAGACACACTGGAATCTTGTGGACCCTCTGAGCCTAGGGTCTGGGTGGCGCCTAACAGCAATGAAAGGGCAGAGTTCCAGGATTGCAGATGGCAAAACACCTGCGTGGCAGCAAGTGGGAGTCTTCACTGGCCTGCCCCTCCTTCTGTGTGGGGCACTCTCCACAGGGCTTCCAGCTCATCTAGATGAGGAGCTCCAAGCCACACTCCACGACTTTAGACATCAAATCCTGCAGACAAGGGGAGGTAAGGGGACCCCCTGGGCCTCACGGGGTAGGAGTTTCCCACAAATTCCCCTCATTCTCAGCACCAGCTTCTAGAACATAGAGATTACAAATAGGCATGCACATGCAGGTCTTGGGGAAAGGAATGACGCTTGCTTTTCTGATGTCTTTGAATGGCCCAGAGGAGACAGAAGCAGACACAATTCACTCCCCATTTCATAGGAAAGCAAGTTCTCCACCTGCCTTGCTTTCCACTGAATTCCAGGAAATTGCACCATTTCTGGCAATAAGTAATTGTTACTTAGGTGAATGAATAAATGGAGGAGAGTCTAAAAGTGAATTTAGAAAACTGCAATTGGAAGAGGAAGAGAAGACACAGAGAGAGGCAGAGATGGAGAGACTGGGGAGAATCTGGTAGCAGAGACCCCAGGTGAGGGAGGTGGCTTAGAGACAAAGTGGTCAGTGGCCTGACCCGGACTCCTCTGCTCTCAGCCCTCAGTCTGCAGGGCTCCATAATGACAGTAGGAGAGAAGGTCTTCTCCAGCAATGGGCAGTCCATCACTTTTGATGCCATTCAGGAGGCATGTGCCAGAGCAGGCGGCCGCATTGCTGTCCCAAGGAATCCAGAGGAAAATGAGGCCATTGCAAGCTTCGTGAAGAAGTACAACACATATGCCTATGTAGGCCTGACTGAGGGTCCCAGCCCTGGAGACTTCCGCTACTCAGACGGGACCCCTGTAAACTACACCAACTGGTACCGAGGGGAGCCCGCAGGTCGGGGAAAAGAGCAGTGTGTGGAGATGTACACAGATGGGCAGTGGAATGACAGGAACTGCCTGTACTCCCGACTGACCATCTGTGAGTTCTGAGAGGCATTTAGGCCATGGGACAGGGAGGACGCTCTCTGGCCTTCGGCCTCCATCCTGAGGCTCCACTTGGTCTGTGAGATGCTAGAACTCCCTTTCAACAGAATTCACTTGTGGCTATTGGGACTGGAGGCACCCTTAGCCACTTCATTCCTCTGATGGGCCCTGACTCTTCCCCATAATCACTGACCAGCCTTGACACTCCCCTTGCAAACTCTCCCAGCACTGCACCCCAGGCAGCCACTCTTAGCCTTGGCCTTCGACATGAGATGGAGCCCTCCTTATTCCCCATCTGGTCCAGTTCCTTCACTTACAGATGGCAGCAGTGAGGTCTTGGGGTAGAAGGACCCTCCAAAGTCACACAAAGTGCCTGCCTCCTGGTCCCCTCAGCTCTCTCTCTGCAACCCAGTGCCATCAGGATGAGCAATCCTGGCCAAGCATAATGACAGAGAGAGGCAGACTTCGGGGAAGCCCTGACTGTGCAGAGCTAAGGACACAGTGGAGATTCTCTGGCACTCTGAGGTCTCTGTGGCAGGCCTGGTCAGGCTCTCCATGAGGTTAGAAGGCCAGGTAGTGTTCCAGCAGGGTGGTGGCCAAGCCAACCCCATGATTGATGTGTACGATTCACTCCTTTGAGTCTTTGAATGGCAACTCAGCCCCCTGACCTGAAGACAGCCAGCCTAGGCCTCTAGGGTGACCTAGAGCCGCCTTCAGATGTGACCCGAGTAACTTTCAACTGATGAACAAATCTGCACCCTACTTCAGATTTCAGTGGGCATTCACACCACCCCCCACACCACTGGCTCTGCTTTCTCCTTTCATTAATCCATTCACCCAGATATTTCATTAAAATTATCACGTGCCAGGTCTTAGGATATGTCGTGGGGTGGGCAAGGTAATCAGTGACAGTTGAAGATTTTTTTTTCCCAGAGCTTATGTCTTCATCTGTGAAATGGGAATAAGATACTTGTTGCTGTCACAGTTATTACCATCCCCCCAGCTACCAAAATTACTACCAGAACTGTTACTATACACAGAGGCTATTGACTGAGCACCTATCATTTGCCAAGAACCTTGACAAGCACTTCTAATACAGCATATTATGTACTATTCAATCTTTACACAATGTCACGGGACCAGTATTGTTTCCTCATTTTTTATAAGGACACTGAAGCTTGGAGGAGTTAAATGTTTTGAGTATTATTCCAGAGAGCAAGTGGCAGAGGCTGGATCCAAACCCATCTTCCTGGACCTGAAGCTTATGCTTCCAGCCACCCCACTCCTGAGCTGAATAAAGATGATTTAAGCTTAATAAATCGTGAATGTGTTCACA"

# FASTA link for SFTPA1: https://www.ncbi.nlm.nih.gov/nuccore/NG_021189.1?from=5001&to=9505&report=fasta
# start codon
METcodon = "ATG"
stopcodon1 = "TAA"
stopcodon2 = "TAG"
stopcodon3 = "TGA"

position = 0
start_pos = SFTPA1.index(METcodon)
mRNA_excess = SFTPA1[start_pos:];
mRNA_excess.find("STOP")

first_mRNA_excess = SFTPA1[(SFTPA1.find(METcodon)):]
first_mRNA = first_mRNA_excess[:(3 + (first_mRNA_excess.find(stopcodon1 or stopcodon2 or stopcodon3)))]
print (first_mRNA)

#produces entire mRNA
##def mRNA_producer (DNAseq, position):
##while position < len(mRNA_excess) - 2 and mRNA_excess[position:(position+3)] != (stopcodon1 or stopcodon2 or stopcodon3) :
##    if (mRNA_excess[position:(position + 3)]) == (
##    print (mRNA_excess[position:(position+3)])
##    position = position + 3
    
#produces mRNA from start
def mRNA_start (DNAseq, position):
    DNAseq[(DNAseq.find(METcodon)):]
#produces mRNA from start to stop
def mRNA_producer (DNAseq, position):
    if DNAseq[0:3]:
            print "START"
            position = position + 3
            while position < len(DNAseq) - 2:
                if DNAseq[position:(position + 3)] == METcodon:
                    while position < len(DNAseq):
                        if DNAseq[position:(position + 3)] == stopcodon1 or DNAseq[position:(position + 3)] == stopcodon2 or DNAseq[position:(position + 3)] == stopcodon3:
                            print "STOP"
                            position = len(DNAseq)
                        else: print DNAseq[position:(position + 3)]
                        position = position + 3
                    position = len(DNAseq)
                elif position == len(DNAseq) - 3 and DNAseq[position:] != METcodon:
                    print "No ORF"
                    position = len(DNAseq)
                else: position = position + 1

#produces mRNA from start to stop as a list

mRNA = []

def mRNA_producer2 (DNAseq, position):
    while position < len(DNAseq):
        if DNAseq[position:position+3] == "ATG":
            mRNA.append("START")
            position = position + 3
            while position < len(DNAseq) - 2:
                if DNAseq[position:(position + 3)] == stopcodon1 or DNAseq[position:(position + 3)] == stopcodon2 or DNAseq[position:(position + 3)] == stopcodon3:
                    mRNA.append("STOP")
                    print mRNA
                    position = len(DNAseq)
                else:
                    mRNA.append(DNAseq[position:(position + 3)])
                    position = position + 3
            position = len(DNAseq)
        elif position == len(DNAseq) - 2:
            print "No ORF"
            position = len(DNAseq)
        else:
            position = position + 1

polypeptide = []

def polypeptide_producer(mRNAseq, position):
    while position < len(mRNAseq):
        if mRNAseq[position:(position+1)] == ['TTT'] or mRNAseq[position:(position+1)] == ['TTC']:
            polypeptide.append("Phe")
            position = position + 1
        elif mRNAseq[position:(position+1)] == ['START']:
            polypeptide.append("START")
            position = position + 1            
        elif mRNAseq[position:(position+1)] == ['ATG']:
            polypeptide.append("MET")
            position = position + 1            
        elif mRNAseq[position:(position+1)] == ['TTA'] or mRNAseq[position:(position+1)] == ['TTG'] or mRNAseq[position:(position+1)] == ['CTT'] or mRNAseq[position:(position+1)] == ['CTC'] or mRNAseq[position:(position+1)] == ['CTA'] or mRNAseq[position:(position+1)] == ['CTG']:
            polypeptide.append("Leu")
            position = position + 1    
        elif mRNAseq[position:(position+1)] == ['ATT'] or mRNAseq[position:(position+1)] == ['ATC'] or mRNAseq[position:(position+1)] == ['ATA']:
            polypeptide.append ("Ile")
            position = position + 1
        elif mRNAseq[position:(position+1)] == ['GTT'] or mRNAseq[position:(position+1)] == ['GTC'] or mRNAseq[position:(position+1)] == ['GTA'] or mRNAseq[position:(position+1)] == ['GTG']:
            polypeptide.append ("Val")
            position = position + 1     
        elif mRNAseq[position:(position+1)] == ['TCT'] or mRNAseq[position:(position+1)] == ['TCC'] or mRNAseq[position:(position+1)] == ['TCA'] or mRNAseq[position:(position+1)] == ['TCG'] or mRNAseq[position:(position+1)] == ['AGT'] or mRNAseq[position:(position+1)] == ['AGC']:
            polypeptide.append ("Ser")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['CCT'] or mRNAseq[position:(position+1)] == ['CCC'] or mRNAseq[position:(position+1)] == ['CCA'] or mRNAseq[position:(position+1)] == ['CCG']:
            polypeptide.append ("Pro")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['ACT'] or mRNAseq[position:(position+1)] == ['ACC'] or mRNAseq[position:(position+1)] == ['ACA'] or mRNAseq[position:(position+1)] == ['ACG']:
            polypeptide.append ("Thr")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['GCT'] or mRNAseq[position:(position+1)] == ['GCC'] or mRNAseq[position:(position+1)] == ['GCA'] or mRNAseq[position:(position+1)] == ['GCG']:
            polypeptide.append ("Ala")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['TAT'] or mRNAseq[position:(position+1)] == ['TAC']:
            polypeptide.append ("Tyr")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['CAT'] or mRNAseq[position:(position+1)] == ['CAC']:
            polypeptide.append ("His")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['CAA'] or mRNAseq[position:(position+1)] == ['CAG']:
            polypeptide.append ("Gln")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['AAT'] or mRNAseq[position:(position+1)] == ['AAC']:
            polypeptide.append ("Asn")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['AAA'] or mRNAseq[position:(position+1)] == ['AAG']:
            polypeptide.append ("Lys")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['GAT'] or mRNAseq[position:(position+1)] == ['GAC']:
            polypeptide.append ("Asp")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['GAA'] or mRNAseq[position:(position+1)] == ['GAG']:
            polypeptide.append ("Glu")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['TGT'] or mRNAseq[position:(position+1)] == ['TGC']:
            polypeptide.append ("Cys")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['TGG']:
            polypeptide.append ("Trp")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['CGT'] or mRNAseq[position:(position+1)] == ['CGC'] or mRNAseq[position:(position+1)] == ['CGA'] or mRNAseq[position:(position+1)] == ['CGG'] or mRNAseq[position:(position+1)] == ['AGA'] or mRNAseq[position:(position+1)] == ['AGG']:
            polypeptide.append ("Arg")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['GGT'] or mRNAseq[position:(position+1)] == ['GGC'] or mRNAseq[position:(position+1)] == ['GGA'] or mRNAseq[position:(position+1)] == ['GGG']:
            polypeptide.append ("Gly")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == ['STOP']:
            polypeptide.append ("STOP")
            print polypeptide
            position = len(mRNAseq)
        else:
            polypeptide.append("What the hell went wrong?")
            print polypeptide
            position = len(mRNAseq)




##number_AA = ((len(first_mRNA))/3)
##aa1 = (first_mRNA[0:3])
##aa2 = (first_mRNA[3:6])
##print (aa1)
##print (aa2)

# n.remove(item)
    
# def add_function(x,y):
    # return x + y
# print add_function (m, n)
