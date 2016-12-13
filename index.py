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


##if (SFTPA1[position:(position+3)]) == METcodon:
##    print ("ORF" + SFTPA1[position:])
###    for i in range (len SFTPA1):
###        print (SFTPA1[i])
###    print (SFTPA1[position:(position+3)])
##else:
##    position = position + 1

first_mRNA_excess = SFTPA1[(SFTPA1.find(METcodon)):]
first_mRNA = first_mRNA_excess[:(3 + (first_mRNA_excess.find(stopcodon1 or stopcodon2 or stopcodon3)))]
print (first_mRNA)

#produces entire mRNA
##def mRNA_producer (DNAseq, position):
##while position < len(mRNA_excess) - 2 and mRNA_excess[position:(position+3)] != (stopcodon1 or stopcodon2 or stopcodon3) :
##    if (mRNA_excess[position:(position + 3)]) == (
##    print (mRNA_excess[position:(position+3)])
##    position = position + 3
    
#produces entire mRNA
def mRNA_start (DNAseq, position):
    DNAseq[(DNAseq.find(METcodon)):]
def mRNA_producer (mRNA_start, position):
    print (mRNA_start[:(3 + (mRNA_start.find(stopcodon1 or stopcodon2 or stopcodon3)))])
    
    
##    while position < len(DNAseq) - 2:
##        if (DNAseq[position:(position + 3)]) == METcodon:
##            print "START"
##            position = position + 3
##        else: mRNA_producer (DNAseq, position+3)

##only half of polypeptide produced 
def polypeptide_producer (DNAseq, position):
    while position < len(DNAseq):
        if DNAseq[position:(position+3)] == "TTT" or DNAseq[position:(position + 3)] == "TTC":
            print ("Phe")
            position = position + 3    
        if DNAseq[position:(position+3)] == "TTA" or DNAseq[position:(position+3)] == "TTG" or DNAseq[position:(position+3)] == "CTT" or DNAseq[position:(position+3)] == "CTC" or DNAseq[position:(position+3)] == "CTA" or DNAseq[position:(position+3)] == "CTG":
            print ("Leu")
            position = position + 3    
        if DNAseq[position:(position+3)] == "ATT" or DNAseq[position:(position+3)] == "ATC" or DNAseq[position:(position+3)] == "ATA":
            print ("Ile")
            position = position + 3
        if DNAseq[position:(position+3)] == "ATG":
            print ("START")
            position = position + 3 
        if DNAseq[position:(position+3)] == "GTT" or DNAseq[position:(position+3)] == "GTC" or DNAseq[position:(position+3)] == "GTA" or DNAseq[position:(position+3)] == "GTG":
            print ("Val")
            position = position + 3     
        if DNAseq[position:(position+3)] == "TCT" or DNAseq[position:(position+3)] == "TCC" or DNAseq[position:(position+3)] == "TCA" or DNAseq[position:(position+3)] == "TCG" or DNAseq[position:(position+3)] == "AGT" or DNAseq[position:(position+3)] == "AGC":
            print ("Ser")
            position = position + 3 
        if DNAseq[position:(position+3)] == "CCT" or DNAseq[position:(position+3)] == "CCC" or DNAseq[position:(position+3)] == "CCA" or DNAseq[position:(position+3)] == "CCG":
            print ("Pro")
            position = position + 3 
        if DNAseq[position:(position+3)] == "ACT" or DNAseq[position:(position+3)] == "ACC" or DNAseq[position:(position+3)] == "ACA" or DNAseq[position:(position+3)] == "ACG":
            print ("Thr")
            position = position + 3 
        if DNAseq[position:(position+3)] == "GCT" or DNAseq[position:(position+3)] == "GCC" or DNAseq[position:(position+3)] == "GCA" or DNAseq[position:(position+3)] == "GCG":
            print ("Ala")
            position = position + 3 
        if DNAseq[position:(position+3)] == "TAT" or DNAseq[position:(position+3)] == "TAC":
            print ("Tyr")
            position = position + 3 
        if DNAseq[position:(position+3)] == "CAT" or DNAseq[position:(position+3)] == "CAC":
            print ("His")
            position = position + 3 
        if DNAseq[position:(position+3)] == "CAA" or DNAseq[position:(position+3)] == "CAG":
            print ("Gln")
            position = position + 3 
        if DNAseq[position:(position+3)] == "AAT" or DNAseq[position:(position+3)] == "AAC":
            print ("Asn")
            position = position + 3 
        if DNAseq[position:(position+3)] == "AAA" or DNAseq[position:(position+3)] == "AAG":
            print ("Lys")
            position = position + 3 
        if DNAseq[position:(position+3)] == "GAT" or DNAseq[position:(position+3)] == "GAC":
            print ("Asp")
            position = position + 3 
        if DNAseq[position:(position+3)] == "GAA" or DNAseq[position:(position+3)] == "GAG":
            print ("Glu")
            position = position + 3 
        if DNAseq[position:(position+3)] == "TGT" or DNAseq[position:(position+3)] == "TGC":
            print ("Cys")
            position = position + 3 
        if DNAseq[position:(position+3)] == "TGG":
            print ("Trp")
            position = position + 3 
        if DNAseq[position:(position+3)] == "CGT" or DNAseq[position:(position+3)] == "CGC" or DNAseq[position:(position+3)] == "CGA" or DNAseq[position:(position+3)] == "CGG" or DNAseq[position:(position+3)] == "AGA" or DNAseq[position:(position+3)] == "AGG":
            print ("Arg")
            position = position + 3 
        if DNAseq[position:(position+3)] == "GGT" or DNAseq[position:(position+3)] == "GGC" or DNAseq[position:(position+3)] == "GGA" or DNAseq[position:(position+3)] == "GGG":
            print ("Gly")
            position = position + 3 
        if DNAseq[position:(position+3)] == "TAA" or DNAseq[position:(position+3)] == "TAG" or DNAseq[position:(position+3)] == "UGA":
            print ("STOP")
            position = position + 3


##number_AA = ((len(first_mRNA))/3)
##aa1 = (first_mRNA[0:3])
##aa2 = (first_mRNA[3:6])
##print (aa1)
##print (aa2)

# n.remove(item)
    
# def add_function(x,y):
    # return x + y
# print add_function (m, n)
