print ("Test Page")

DNA = "ATGCAACGTATTGACCTTTTACTGTACTAA"

# premature stop codon added in + DNAseq not divisible by 3
DNA2 = "CATGCAACGTATTGACCTTTTAAAAAAAAAAAAAAAAAAAAAAAAAACTGTACTATAASG"

METcodon = "ATG"
stopcodon1 = "TAA"
stopcodon2 = "TAG"
stopcodon3 = "TGA"
##position = 0

##while position < len(DNAseq) - 2:
##    if DNAseq[position:(position + 3)] == "ATG":
##        print "START"
##        position = position + 3
##    if DNAseq[position:(position + 3)] == "CGT" or DNAseq[position:(position + 3)] == "ATT":
##        print "Arg"
##        position = position + 3
##    else: 
##        print DNAseq[position:(position + 3)]
##        position = position + 3

## requires function to have a stopcodon in frame to terminate    
def mRNA_producer (DNAseq, position):
    while position < len(DNAseq) - 2:
        if DNAseq[position:(position + 3)] == METcodon:
            while position < len(DNAseq):
                if DNAseq[position:(position + 3)] == (stopcodon1 or stopcodon2 or stopcodon3):
                    print "STOP"
                    position = len(DNAseq)
                else: print DNAseq[position:(position + 3)]
                position = position + 3
            position = len(DNAseq)
        if position == len(DNAseq) - 3 and DNAseq[position:] != METcodon:
            print "No ORF"
            position = len(DNAseq)
        else: position = position + 1
