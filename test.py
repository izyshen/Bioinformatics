print ("Test Page")

testDNA = "ATGATGCAACGTATTGACCTTTTACTGTACTAA"

# premature stop codon added in + len(DNAseq) not divisible by 3
testDNA2 = "CATGCAACGTATGTCCTTTTCAAAAAAAAAAAAAAAAAAAAAAAAATGTACTACCTAASG"
# offstart
testDNA3 = "CATGCAATGA"
# len(DNAseq) not divisible by 3, excess after stop codon
testDNA4 = "ATGCATCCTTAAHCWWEtGESDLGKGJLDSKFN"
# first stop codon not in frame
testDNA5 = "ATGATAACCTAA"
# no start codon
testDNA6 = "GATCGATCTA"
#start codon 3 off
testDNA7 = "TTTATG"

METcodon = "ATG"
stopcodon1 = "TAA"
stopcodon2 = "TAG"
stopcodon3 = "TGA"

## print mRNA codons as a list  
## list produced inside fcn, for production of polycistronic mRNA strands
##mRNA = []
##def mRNA_producer (DNAseq, position):
##    while position < len(DNAseq):
##        if DNAseq[position:position+3] == "ATG":
##            mRNA.append("START")
##            position = position + 3
##            while position <= len(DNAseq):
##                if DNAseq[position:(position + 3)] == stopcodon1 or DNAseq[position:(position + 3)] == stopcodon2 or DNAseq[position:(position + 3)] == stopcodon3:
##                    mRNA.append("STOP")
##                    print mRNA
##                    break
##                elif position == len(DNAseq) - 2 or position == len(DNAseq) - 1 or position == len(DNAseq):
##                    print "no stop codon"
##                    break
##                else:
##                    mRNA.append(DNAseq[position:(position + 3)])
##                    position = position + 3
##            position = len(DNAseq)
##        elif position == len(DNAseq) - 2:
##            print "No ORF"
##            position = len(DNAseq)
##        else:
##            position = position + 1

def mRNA_producer2 (DNAseq, position, lst):
    while position < len(DNAseq):
        if DNAseq[position:position+3] == "ATG":
            lst.append("START")
            position = position + 3
            while position <= len(DNAseq):
                if DNAseq[position:(position + 3)] == (stopcodon1 or stopcodon2 or stopcodon3):
                    lst.append("STOP")
                    print (lst)
                    break
                elif position == len(DNAseq) - 2 or position == len(DNAseq) - 1 or position == len(DNAseq):
                    print ("no stop codon")
                    break
                else:
                    lst.append(DNAseq[position:(position + 3)])
                    position = position + 3
            position = len(DNAseq)
        elif position == len(DNAseq) - 2:
            print ("No ORF")
            position = len(DNAseq)
        else:
            position = position + 1

start_codons = []
def start_posns(DNAseq, position):
    while position <= len(DNAseq) - 2:
        if DNAseq[position:position+3] == "ATG":
            start_codons.append(position)
            position = position + 3
        elif position == len(DNAseq) - 2:
            print (start_codons)
            break
        else:
            position = position + 1

##def start_posns(DNAseq, position, lst):
##    while position <= len(DNAseq) - 2:
##        if DNAseq[position:position+3] == "ATG":
##            lst.append(position)
##            position = position + 3
##        elif position == len(DNAseq) - 2:
##            print lst
##            break
##        else:
##            position = position + 1

## prints mRNA
def multiple_mRNA2(DNAseq, start_posns, lst):
    count = 0
    for posn in start_posns:
        lst = []
        count = count + 1
        print ("mRNA" + (str(count)) + ":"), 
        mRNA_producer2(DNAseq, posn, lst)


def mRNA_producer3 (DNAseq, position, lst):
    while position < len(DNAseq):
        if DNAseq[position:position+3] == "ATG":
            lst.append("START")
            position = position + 3
            while position <= len(DNAseq):
                if DNAseq[position:(position + 3)] == (stopcodon1 or stopcodon2 or stopcodon3):
                    lst.append("STOP")
                    return lst
                    break
                elif position == len(DNAseq) - 2 or position == len(DNAseq) - 1 or position == len(DNAseq):
                    return "no stop codon"
                    break
                else:
                    lst.append(DNAseq[position:(position + 3)])
                    position = position + 3
            position = len(DNAseq)
        elif position == len(DNAseq) - 2:
            return "No ORF"
            position = len(DNAseq)
        else:
            position = position + 1

            
def multiple_mRNA3(DNAseq, start_posns, lst):
    count = 0
    mRNAlst = []
    for posn in start_posns:
        lst = []
        count = count + 1
##        mRNAlst.append ("mRNA" + (str(count)) + ":")
        mRNAlst.append (mRNA_producer3(DNAseq, posn, lst))
    print (mRNAlst)

mRNAlst = []
def multiple_mRNA4(DNAseq, start_posns):
    count = 0
    for posn in start_posns:
        count = count + 1
        mRNAlst.append("mRNA" + (str(count)) + ":")
        mRNAlst.append (mRNA_producer3(DNAseq, posn, lst))
    print (mRNAlst)

chair = [1, 10, 45]
##make a dictionary with this, key and value
##see what's longer than 100 AA

##DNAsequence = str(raw_input("Input DNA sequence to produce multiple mRNA: "))
##start_codons = start_posns(DNAsequence, 0, [])
##multiple_mRNA2(DNAsequence, start_codons, [])

##DNAsequence = str(raw_input("Input DNA sequence to produce multiple mRNA: "))
##start_codons = start_posns(DNAsequence, 0, [])
##multiple_mRNA3(DNAsequence, start_codons, [])



# Dictionary

##def mRNAcounter(DNA):
##    count = 0
    
##for item in start_codons:
##

mRNAdic = {}
DNAsequence = str(input("Input DNA sequence to produce multiple mRNA: "))
start_posns(DNAsequence, 0)
mRNAlst = multiple_mRNA3(DNAsequence, start_codons, [])


##mRNA1 = mRNAlst[0:1]
##print (mRNA1)
##mRNAdic['mRNA1'] = mRNA1

##for posn in start_codons:
##    mRNAdic = dict([mRNA_counter, mRNA]) #need mRNA_counter fcn
##    dict([("mRNA1", mRNA1), ("mRNA2", mRNA2), ("mRNA3", mRNA3)])
    
