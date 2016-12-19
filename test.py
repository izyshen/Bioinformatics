print ("Test Page")

testDNA = "ATGATGCAACGTATTGACCTTTTACTGTACTAA"

# premature stop codon added in + len(DNAseq) not divisible by 3
testDNA2 = "CATGCAACGTATTGACCTTTTAAAAAAAAAAAAAAAAAAAAAAAAAACTGTACTATAASG"

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
        
## while loops
## requires function to have a stopcodon in frame to terminate    
def mRNA_producer (DNAseq, position):
    if DNAseq[0:3] == "ATG":
        print "START"
        position = position + 3
        while position < len(DNAseq) - 2:
            if DNAseq[position:(position + 3)] == METcodon:
                while position < len(DNAseq):
                    if DNAseq[position:(position + 3)] == (stopcodon1 or stopcodon2 or stopcodon3):
                        print "STOP"
                        position = len(DNAseq)
                    else:
                        print DNAseq[position:(position + 3)]
                        position = position + 3
                position = len(DNAseq)
    elif position == len(DNAseq) - 3 and DNAseq[position:] != METcodon:
        print "No ORF"
        position = len(DNAseq)
    else:
        position = position + 1

def polypeptide_producer (DNAseq, position):
    mRNAseq = mRNA_producer(DNAseq, 0)
    while position < len(mRNAseq):
        if mRNAseq[position:(position+3)] == "TTT" or mRNAseq[position:(position + 3)] == "TTC":
            print ("Phe")
            position = position + 3    
        if mRNAseq[position:(position+3)] == "TTA" or mRNAseq[position:(position+3)] == "TTG" or mRNAseq[position:(position+3)] == "CTT" or mRNAseq[position:(position+3)] == "CTC" or mRNAseq[position:(position+3)] == "CTA" or mRNAseq[position:(position+3)] == "CTG":
            print ("Leu")
            position = position + 3    
        if mRNAseq[position:(position+3)] == "ATT" or mRNAseq[position:(position+3)] == "ATC" or mRNAseq[position:(position+3)] == "ATA":
            print ("Ile")
            position = position + 3
        if mRNAseq[position:(position+3)] == "ATG":
            if mRNAseq[position:(position+3)] == mRNAseq[0:3]:
                print ("START")
                position = position + 3 
            else:
                print "MET"
                position = position + 3 
        if mRNAseq[position:(position+3)] == "GTT" or mRNAseq[position:(position+3)] == "GTC" or mRNAseq[position:(position+3)] == "GTA" or mRNAseq[position:(position+3)] == "GTG":
            print ("Val")
            position = position + 3     
        if mRNAseq[position:(position+3)] == "TCT" or mRNAseq[position:(position+3)] == "TCC" or mRNAseq[position:(position+3)] == "TCA" or mRNAseq[position:(position+3)] == "TCG" or mRNAseq[position:(position+3)] == "AGT" or mRNAseq[position:(position+3)] == "AGC":
            print ("Ser")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "CCT" or mRNAseq[position:(position+3)] == "CCC" or mRNAseq[position:(position+3)] == "CCA" or mRNAseq[position:(position+3)] == "CCG":
            print ("Pro")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "ACT" or mRNAseq[position:(position+3)] == "ACC" or mRNAseq[position:(position+3)] == "ACA" or mRNAseq[position:(position+3)] == "ACG":
            print ("Thr")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "GCT" or mRNAseq[position:(position+3)] == "GCC" or mRNAseq[position:(position+3)] == "GCA" or mRNAseq[position:(position+3)] == "GCG":
            print ("Ala")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "TAT" or mRNAseq[position:(position+3)] == "TAC":
            print ("Tyr")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "CAT" or mRNAseq[position:(position+3)] == "CAC":
            print ("His")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "CAA" or mRNAseq[position:(position+3)] == "CAG":
            print ("Gln")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "AAT" or mRNAseq[position:(position+3)] == "AAC":
            print ("Asn")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "AAA" or mRNAseq[position:(position+3)] == "AAG":
            print ("Lys")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "GAT" or mRNAseq[position:(position+3)] == "GAC":
            print ("Asp")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "GAA" or mRNAseq[position:(position+3)] == "GAG":
            print ("Glu")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "TGT" or mRNAseq[position:(position+3)] == "TGC":
            print ("Cys")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "TGG":
            print ("Trp")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "CGT" or mRNAseq[position:(position+3)] == "CGC" or mRNAseq[position:(position+3)] == "CGA" or mRNAseq[position:(position+3)] == "CGG" or mRNAseq[position:(position+3)] == "AGA" or mRNAseq[position:(position+3)] == "AGG":
            print ("Arg")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "GGT" or mRNAseq[position:(position+3)] == "GGC" or mRNAseq[position:(position+3)] == "GGA" or mRNAseq[position:(position+3)] == "GGG":
            print ("Gly")
            position = position + 3 
        if mRNAseq[position:(position+3)] == "TAA" or mRNAseq[position:(position+3)] == "TAG" or mRNAseq[position:(position+3)] == "UGA":
            print ("STOP")
            position = position + 3

# for loops
## list of codons
##def lister (, position):
##    while position < len(DNAseq) - 2: 
##        print (DNAseq[position:(position + 3)])
##        position = position + 3

def lister (DNAseq, position):
    curr_list = ("start")
    while len(DNAseq) != 0:
        print curr_list.extend(DNAseq[position:(position + 3)])
        position = position+3
        
#this only lists each nucleotide.
#Want to list them as codons to implement translation
def codon_counter(DNAseq, position):
    codon = DNAseq[position:position+3]
    for codon in DNAseq:
        print(codon[position:position+3])
        position = position + 3
                  

##def main_fcn():
##    lister(testDNA, 0)
##    codon_counter(lister(testDNA, 0), 0)
##
##
##def tripleAll(nums):
##    for val in nums:
##        print val*3
##        
##n = int(input('Enter the number of times to repeat: '))
##for i in range(n):
##    print('This is repetitious!')
##
##def numberList(items):
##    number = 1
##    for item in items:
##        print(number, item)
##        number = number + 1
##
##def main():
##    numberList(['red', 'orange', 'yellow', 'green'])
##    print()
##    numberList(['apples', 'pears', 'bananas'])


