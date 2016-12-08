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

if (SFTPA1[position:(position+3)]) == METcodon:
    print ("ORF")
#    for i in range (len SFTPA1):
#        print (SFTPA1[i])
#    print (SFTPA1[position:(position+3)])
else:
    print ("keep looking")


start_pos = SFTPA1.index(METcodon)
mRNA_excess = SFTPA1[start_pos:];
mRNA_excess.find("STOP")
##while position < len(mRNA_excess) - 2 and mRNA_excess[position:(position+3)] != (stopcodon1 or stopcodon2 or stopcodon3) :
##    print (mRNA_excess[position:(position+3)])
##    position = position + 3

first_mRNA_excess = SFTPA1[(SFTPA1.find(METcodon)):]
first_mRNA = first_mRNA_excess[:(3 + (first_mRNA_excess.find(stopcodon1 or stopcodon2 or stopcodon3)))]
while position < len(first_mRNA) - 2:
    if first_mRNA[position:(position+3)] == "TTT" or first_mRNA[position:(position + 3)] == "TTC":
        print ("Phe")
        position = position + 3    
    if first_mRNA[position:(position+3)] == "TTA" or first_mRNA[position:(position+3)] == "TTG" or first_mRNA[position:(position+3)] == "CTT" or first_mRNA[position:(position+3)] == "CTC" or first_mRNA[position:(position+3)] == "CTA" or first_mRNA[position:(position+3)] == "CTG":
        print ("Leu")
        position = position + 3    
    if first_mRNA[position:(position+3)] == "ATT" or first_mRNA[position:(position+3)] == "ATC" or first_mRNA[position:(position+3)] == "ATA":
        print ("Ile")
        position = position + 3
    if first_mRNA[position:(position+3)] == "ATG":
        print ("START")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "GTT" or first_mRNA[position:(position+3)] == "GTC" or first_mRNA[position:(position+3)] == "GTA" or first_mRNA[position:(position+3)] == "GTG":
        print ("Val")
        position = position + 3     
    if first_mRNA[position:(position+3)] == "TCT" or first_mRNA[position:(position+3)] == "TCC" or first_mRNA[position:(position+3)] == "TCA" or first_mRNA[position:(position+3)] == "TCG" or first_mRNA[position:(position+3)] == "AGT" or first_mRNA[position:(position+3)] == "AGC":
        print ("Ser")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "CCT" or first_mRNA[position:(position+3)] == "CCC" or first_mRNA[position:(position+3)] == "CCA" or first_mRNA[position:(position+3)] == "CCG":
        print ("Pro")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "ACT" or first_mRNA[position:(position+3)] == "ACC" or first_mRNA[position:(position+3)] == "ACA" or first_mRNA[position:(position+3)] == "ACG":
        print ("Thr")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "GCT" or first_mRNA[position:(position+3)] == "GCC" or first_mRNA[position:(position+3)] == "GCA" or first_mRNA[position:(position+3)] == "GCG":
        print ("Ala")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "TAT" or first_mRNA[position:(position+3)] == "TAC":
        print ("Tyr")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "CAT" or first_mRNA[position:(position+3)] == "CAC":
        print ("His")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "CAA" or first_mRNA[position:(position+3)] == "CAG":
        print ("Gln")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "AAT" or first_mRNA[position:(position+3)] == "AAC":
        print ("Asn")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "AAA" or first_mRNA[position:(position+3)] == "AAG":
        print ("Lys")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "GAT" or first_mRNA[position:(position+3)] == "GAC":
        print ("Asp")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "GAA" or first_mRNA[position:(position+3)] == "GAG":
        print ("Glu")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "TGT" or first_mRNA[position:(position+3)] == "TGC":
        print ("Cys")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "TGG":
        print ("Trp")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "CGT" or first_mRNA[position:(position+3)] == "CGC" or first_mRNA[position:(position+3)] == "CGA" or first_mRNA[position:(position+3)] == "CGG" or first_mRNA[position:(position+3)] == "AGA" or first_mRNA[position:(position+3)] == "AGG":
        print ("Arg")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "GGT" or first_mRNA[position:(position+3)] == "GGC" or first_mRNA[position:(position+3)] == "GGA" or first_mRNA[position:(position+3)] == "GGG":
        print ("Gly")
        position = position + 3 
    if first_mRNA[position:(position+3)] == "TAA" or first_mRNA[position:(position+3)] == "TAG" or first_mRNA[position:(position+3)] == "UGA":
        print ("STOP")
        position = position + 3


############# only first MET should say start, MET can be in seq otherwise as
############# a regular AA
        ### stop codon not found
##def translation(mRNAseq):
##    position = 0;
##    while position < len(mRNAseq) - 2:
##        if mRNAseq[position:(position+3)] == ("TTT" or "TTC"):
##            print ("Phe")
##            position = position + 3    
##        if mRNAseq[position:(position+3)] == "TTA" or "TTG" or "CTT" or "CTC" or "CTA" or "CTG":
##            print ("Leu")
##            position = position + 3    
##        if mRNAseq[position:(position+3)] == "ATT" or "ATC" or "ATA":
##            print ("Ile")
##            position = position + 3
##        if mRNAseq[position:(position+3)] == "ATG":
##            print ("START")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "GTT" or "GTC" or "GTA" or "GTG":
##            print ("Val")
##            position = position + 3     
##        if mRNAseq[position:(position+3)] == "TCT" or "TCC" or "TCA" or "TCG" or "AGT" or "AGC":
##            print ("Ser")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "CCT" or "CCC" or "CCA" or "CCG":
##            print ("Pro")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "ACT" or "ACC" or "ACA" or "ACG":
##            print ("Thr")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "GCT" or "GCC" or "GCA" or "GCG":
##            print ("Ala")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "TAT" or "TAC":
##            print ("Tyr")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "CAT" or "CAC":
##            print ("His")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "CAA" or "CAG":
##            print ("Gln")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "AAT" or "AAC":
##            print ("Asn")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "AAA" or "AAG":
##            print ("Lys")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "GAT" or "GAC":
##            print ("Asp")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "GAA" or "GAG":
##            print ("Glu")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "TGT" or "TGC":
##            print ("Cys")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "TGG":
##            print ("Trp")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "CGT" or "CGC" or "CGA" or "CGG" or "AGA" or "AGG":
##            print ("Arg")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "GGT" or "GGC" or "GGA" or "GGG":
##            print ("Gly")
##            position = position + 3 
##        if mRNAseq[position:(position+3)] == "TAA" or "TAG" or "UGA":
##            print ("STOP")
##            position = position + 3        
    
##    
##    if first_mRNA[position:(position+3)] == ("TTT" or "TTC"):
##        print ("Phe")
##    if first_mRNA[position:(position+3)] == "TTA" or "TTG" or "CTT" or "CTC" or "CTA" or "CTG":
##        print ("Leu")
##    if first_mRNA[position:(position+3)] == "ATT" or "ATC" or "ATA":
##        print ("Ile")
##    if first_mRNA[position:(position+3)] == "ATG":
##        print ("START")
##    if first_mRNA[position:(position+3)] == "GTT" or "GTC" or "GTA" or "GTG":
##        print ("Val")
##    if first_mRNA[position:(position+3)] == "TCT" or "TCC" or "TCA" or "TCG" or "AGT" or "AGC":
##        print ("Ser")
##    if first_mRNA[position:(position+3)] == "CCT" or "CCC" or "CCA" or "CCG":
##        print ("Pro")
##    if first_mRNA[position:(position+3)] == "ACT" or "ACC" or "ACA" or "ACG":
##        print ("Thr")
##    if first_mRNA[position:(position+3)] == "GCT" or "GCC" or "GCA" or "GCG":
##        print ("Ala")
##    if first_mRNA[position:(position+3)] == "TAT" or "TAC":
##        print ("Tyr")
##    if first_mRNA[position:(position+3)] == "CAT" or "CAC":
##        print ("His")
##    if first_mRNA[position:(position+3)] == "CAA" or "CAG":
##        print ("Gln")
##    if first_mRNA[position:(position+3)] == "AAT" or "AAC":
##        print ("Asn")
##    if first_mRNA[position:(position+3)] == "AAA" or "AAG":
##        print ("Lys")
##    if first_mRNA[position:(position+3)] == "GAT" or "GAC":
##        print ("Asp")
##    if first_mRNA[position:(position+3)] == "GAA" or "GAG":
##        print ("Glu")
##    if first_mRNA[position:(position+3)] == "TGT" or "TGC":
##        print ("Cys")
##    if first_mRNA[position:(position+3)] == "TGG":
##        print ("Trp")
##    if first_mRNA[position:(position+3)] == "CGT" or "CGC" or "CGA" or "CGG" or "AGA" or "AGG":
##        print ("Arg")
##    if first_mRNA[position:(position+3)] == "GGT" or "GGC" or "GGA" or "GGG":
##        print ("Gly")
##    if first_mRNA[position:(position+3)] == "TAA" or "TAG" or "UGA":
##        print ("STOP")
    
##number_AA = ((len(first_mRNA))/3)
##aa1 = (first_mRNA[0:3])
##aa2 = (first_mRNA[3:6])
##print (aa1)
##print (aa2)

##first_mRNA_excess = SFTPA1[(SFTPA1.find(METcodon)):]
##first_mRNA = first_mRNA_excess[:(3 + (first_mRNA_excess.find(stopcodon1 or stopcodon2 or stopcodon3)))]
##while position < len(first_mRNA) - 2:
##    print (first_mRNA[position:(position+3)])
##    position = position + 3

##def mRNA_strand(mRNA):
##    while position < len(mRNA) - 2:
##        if mRNA[position:(position+3)] == ("TTT" or "TTC"):
##            print ("Phe")
##            position = position + 3
##            return
##        if mRNA[position:(position+3)] == "TTA" or "TTG" or "CTT" or "CTC" or "CTA" or "CTG":
##            print ("Leu")
##            position = position + 3    
##        if mRNA[position:(position+3)] == "ATT" or "ATC" or "ATA":
##            print ("Ile")
##            position = position + 3
##        if mRNA[position:(position+3)] == "ATG":
##            print ("START")
##            position = position + 3    
##        if mRNA[position:(position+3)] == "GTT" or "GTC" or "GTA" or "GTG":
##            print ("Val")
##            position = position + 3     
##        if mRNA[position:(position+3)] == "TCT" or "TCC" or "TCA" or "TCG" or "AGT" or "AGC":
##            print ("Ser")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "CCT" or "CCC" or "CCA" or "CCG":
##            print ("Pro")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "ACT" or "ACC" or "ACA" or "ACG":
##            print ("Thr")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "GCT" or "GCC" or "GCA" or "GCG":
##            print ("Ala")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "TAT" or "TAC":
##            print ("Tyr")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "CAT" or "CAC":
##            print ("His")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "CAA" or "CAG":
##            print ("Gln")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "AAT" or "AAC":
##            print ("Asn")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "AAA" or "AAG":
##            print ("Lys")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "GAT" or "GAC":
##            print ("Asp")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "GAA" or "GAG":
##            print ("Glu")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "TGT" or "TGC":
##            print ("Cys")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "TGG":
##            print ("Trp")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "CGT" or "CGC" or "CGA" or "CGG" or "AGA" or "AGG":
##            print ("Arg")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "GGT" or "GGC" or "GGA" or "GGG":
##            print ("Gly")
##            position = position + 3 
##        if mRNA[position:(position+3)] == "TAA" or "TAG" or "UGA":
##            print ("STOP")
##            position = position + 3             



# n.remove(item)
    
# def add_function(x,y):
    # return x + y
# print add_function (m, n)


# produce polypeptide seq
# can't do methylations and phosphorylation
# look for polyAsignal,
# hydrophobic/phillic regions
