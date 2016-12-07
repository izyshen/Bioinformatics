print ("Test Page")

DNAseq = "ATGCGTATTGACCTTTTACTGTACTAA"

position = 0

while position < len(DNAseq) - 2:
    if DNAseq[position:(position + 3)] == "ATG":
        print "START"
        position = position + 3
    if DNAseq[position:(position + 3)] == "CGT" or DNAseq[position:(position + 3)] == "ATT":
        print "Arg"
        position = position + 3
    else: 
        print DNAseq[position:(position + 3)]
        position = position + 3
    
