print ("Test Page")

DNA = "ATGCAACGTATTGACCTTTTACTGTACTAA"

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
    
def mRNA_producer (DNAseq, position):
    while position < len(DNAseq) - 2:
        if DNAseq[position:(position + 3)] == "ATG":
            print DNAseq[position:]
            position = len(DNAseq)
        if position == len(DNAseq) - 3 and DNAseq[position:] != "ATG":
            print "No ORF"
            position = len(DNAseq)
        else: position = position + 1
                             
