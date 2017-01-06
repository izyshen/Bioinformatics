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
##def mRNA_producer (DNAseq, position):
##    if DNAseq[0:3]:
##            print "START"
##            position = position + 3
##            while position < len(DNAseq) - 2:
##                if DNAseq[position:(position + 3)] == METcodon:
##                    while position < len(DNAseq):
##                        if DNAseq[position:(position + 3)] == stopcodon1 or DNAseq[position:(position + 3)] == stopcodon2 or DNAseq[position:(position + 3)] == stopcodon3:
##                            print "STOP"
##                            position = len(DNAseq)
##                        else: print DNAseq[position:(position + 3)]
##                        position = position + 3
##                    position = len(DNAseq)
##                elif position == len(DNAseq) - 3 and DNAseq[position:] != METcodon:
##                    print "No ORF"
##                    position = len(DNAseq)
##                else: position = position + 1

#produces mRNA from start to stop as a list
mRNA = []
def mRNA_producer (DNAseq, position):
    while position < len(DNAseq):
        if DNAseq[position:position+3] == "ATG":
            mRNA.append("START")
            position = position + 3
            while position <= len(DNAseq):
                if DNAseq[position:(position + 3)] == stopcodon1 or DNAseq[position:(position + 3)] == stopcodon2 or DNAseq[position:(position + 3)] == stopcodon3:
                    mRNA.append("STOP")
                    print mRNA
                    break
                elif position == len(DNAseq) - 2 or position == len(DNAseq) - 1 or position == len(DNAseq):
                    print "no stop codon"
                    break
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
def polypeptide_producer(mRNAseq):
    for codon in mRNAseq:
        if codon == 'TTT' or codon == 'TTC':
            polypeptide.append("Phe")
        elif codon == 'START':
            polypeptide.append("START")       
        elif codon == 'ATG':
            polypeptide.append("MET")        
        elif codon == 'TTA' or codon == 'TTG' or codon == 'CTT' or codon == 'CTC' or codon == 'CTA' or codon == 'CTG':
            polypeptide.append("Leu")  
        elif codon == 'ATT' or codon == 'ATC' or codon == 'ATA':
            polypeptide.append ("Ile")
        elif codon == 'GTT' or codon == 'GTC' or codon == 'GTA' or codon == 'GTG':
            polypeptide.append ("Val") 
        elif codon == 'TCT' or codon == 'TCC' or codon == 'TCA' or codon == 'TCG' or codon == 'AGT' or codon == 'AGC':
            polypeptide.append ("Ser")
        elif codon == 'CCT' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
            polypeptide.append ("Pro")
        elif codon == 'ACT' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
            polypeptide.append ("Thr")
        elif codon == 'GCT' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
            polypeptide.append ("Ala")
        elif codon == 'TAT' or codon == 'TAC':
            polypeptide.append ("Tyr")
        elif codon == 'CAT' or codon == 'CAC':
            polypeptide.append ("His")
        elif codon == 'CAA' or codon == 'CAG':
            polypeptide.append ("Gln")
        elif codon == 'AAT' or codon == 'AAC':
            polypeptide.append ("Asn")
        elif codon == 'AAA' or codon == 'AAG':
            polypeptide.append ("Lys")
        elif codon == 'GAT' or codon == 'GAC':
            polypeptide.append ("Asp")
        elif codon == 'GAA' or codon == 'GAG':
            polypeptide.append ("Glu")
        elif codon == 'TGT' or codon == 'TGC':
            polypeptide.append ("Cys")
        elif codon == 'TGG':
            polypeptide.append ("Trp")
        elif codon == 'CGT' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
            polypeptide.append ("Arg")
        elif codon == 'GGT' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
            polypeptide.append ("Gly")
        elif codon == 'STOP':
            polypeptide.append ("STOP")
            print polypeptide
        else:
            polypeptide.append("What the hell went wrong?")

start_codons = []
def start_posns(DNAseq, position):
    while position <= len(DNAseq) - 2:
        if DNAseq[position:position+3] == "ATG":
            start_codons.append(position)
            position = position + 3
        elif position == len(DNAseq) - 2:
            print start_codons
            break
        else:
            position = position + 1

## produce single (first) mRNA strand
DNAsequence = str(raw_input("Input DNA sequence:"))
mRNAinput = mRNA_producer(DNAsequence, 0)
polypeptide_producer(mRNA)

