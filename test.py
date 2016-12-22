print ("Test Page")

testDNA = "ATGATGCAACGTATTGACCTTTTACTGTACTAA"

# premature stop codon added in + len(DNAseq) not divisible by 3
testDNA2 = "CATGCAACGTATTGACCTTTTAAAAAAAAAAAAAAAAAAAAAAAAAACTGTACTATAASG"
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
        
## while loops
## requires function to have a stopcodon in frame to terminate    
def mRNA_producer (DNAseq, position):
    while position < len(DNAseq) - 2:
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
##        elif position == len(DNAseq) - 3 and DNAseq[position:] != METcodon:
##            print "No ORF"
##            position = len(DNAseq)
        else:
            position = position + 1
## something is only a coding ORF if it has 100+ amino acids

##testmRNA = mRNA_producer(testDNA, 0)
##print testmRNA


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
        
##def main_fcn():
##    lister(testDNA, 0)
##    codon_counter(lister(testDNA, 0), 0)
####
##
##def tripleAll(nums):
##    for val in nums:
##        print val*3
##        
############n = int(input('Enter the number of times to repeat: '))
############for i in range(n):
############    print('This is repetitious!')
############
############n = str(input('This is a test: '))
############for codon in range(n):
############    print codon#print codons using input
############    #learn for loops first
    
##
##def numberList(items):
##    number = 1
##    for item in items:
##        print(number, item)
##        number = number + 1

##def main():
##    numberList(['red', 'orange', 'yellow', 'green'])
##    print()
##    numberList(['apples', 'pears', 'bananas'])
polypep = []

def poly_producer(position, mRNAseq):
    while position < len(mRNAseq):
        if mRNAseq[position:position+3] == "ATG":
            polypep.append("START")
            position = position+3
        elif mRNAseq[position:position+3] == "TGG":
            polypep.append("Trp")
            position = position+3
        else:
            print "rest"

numbers = "0123"
list = []

def test(numbers, position):
    while position < len(numbers):
        if position == len(numbers) - 1:
            list.append("last")
            endlist = list
            print endlist
            position = len(numbers)
        elif numbers[position:position+1] == "0":
            list.append("zeroth")
            position = position + 1
        elif numbers[position:position+1] == "1":
            list.append("first")
            position = position + 1
        elif numbers[position:position+1] == "2":
            list.append("second")
            position = position + 1
## turn this into a polypeptide seq

## print mRNA codons as a list
mRNA = []
##def mRNA_list(DNAseq, position):
##    while position < len(DNAseq) - 2:
##        if DNAseq[position:position+3] == "ATG":
##            mRNA.append("START")
##            position = position + 3
##        elif DNAseq[position:position+3] == stopcodon1:
##            mRNA.append("STOP")
##            print mRNA
##            position = len(DNAseq)
##        else:
##            mRNA.append(DNAseq[position:position+3])
##            position = position + 3
            
def mRNA_producer (DNAseq, position):
    while position < len(DNAseq) - 2:
        if DNAseq[position:position+3] == "ATG":
            print "START"
            position = position + 3
            while position < len(DNAseq) - 2:
##                if DNAseq[position:(position + 3)] == METcodon:
##                    while position < len(DNAseq):
                if DNAseq[position:(position + 3)] == (stopcodon1 or stopcodon2 or stopcodon3):
                    print "STOP"
                    position = len(DNAseq)
                else:
                    print DNAseq[position:(position + 3)]
                    position = position + 3
            position = len(DNAseq)
##        elif position == len(DNAseq) - 3 and DNAseq[position:] != METcodon:
##            print "No ORF"
##            position = len(DNAseq)
        else:
            position = position + 1

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
print mRNA_producer2(testDNA2, 0)            
            
polypeptide = []

def polypeptide_producer(mRNAseq, position):
    while position < len(mRNAseq):
        if mRNAseq[position:(position+1)] == ['TTT'] or mRNAseq[position:(position+1)] == "TTC":
            polypeptide.append('Phe')
            position = position + 1
        elif mRNAseq[0:3] == ['START']:
            polypeptide.append('START')
            position = position + 1            
        elif mRNAseq[position:(position+1)] == "ATG":
            polypeptide.append("MET")
            position = position + 1            
        elif mRNAseq[position:(position+1)] == "TTA" or mRNAseq[position:(position+1)] == "TTG" or mRNAseq[position:(position+1)] == "CTT" or mRNAseq[position:(position+1)] == "CTC" or mRNAseq[position:(position+1)] == "CTA" or mRNAseq[position:(position+1)] == "CTG":
            polypeptide.append("Leu")
            position = position + 1    
        elif mRNAseq[position:(position+1)] == "ATT" or mRNAseq[position:(position+1)] == "ATC" or mRNAseq[position:(position+1)] == "ATA":
            polypeptide.append ("Ile")
            position = position + 1
        elif mRNAseq[position:(position+1)] == "GTT" or mRNAseq[position:(position+1)] == "GTC" or mRNAseq[position:(position+1)] == "GTA" or mRNAseq[position:(position+1)] == "GTG":
            polypeptide.append ("Val")
            position = position + 1     
        elif mRNAseq[position:(position+1)] == "TCT" or mRNAseq[position:(position+1)] == "TCC" or mRNAseq[position:(position+1)] == "TCA" or mRNAseq[position:(position+1)] == "TCG" or mRNAseq[position:(position+1)] == "AGT" or mRNAseq[position:(position+1)] == "AGC":
            polypeptide.append ("Ser")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "CCT" or mRNAseq[position:(position+1)] == "CCC" or mRNAseq[position:(position+1)] == "CCA" or mRNAseq[position:(position+1)] == "CCG":
            polypeptide.append ("Pro")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "ACT" or mRNAseq[position:(position+1)] == "ACC" or mRNAseq[position:(position+1)] == "ACA" or mRNAseq[position:(position+1)] == "ACG":
            polypeptide.append ("Thr")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "GCT" or mRNAseq[position:(position+1)] == "GCC" or mRNAseq[position:(position+1)] == "GCA" or mRNAseq[position:(position+1)] == "GCG":
            polypeptide.append ("Ala")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "TAT" or mRNAseq[position:(position+1)] == "TAC":
            polypeptide.append ("Tyr")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "CAT" or mRNAseq[position:(position+1)] == "CAC":
            polypeptide.append ("His")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "CAA" or mRNAseq[position:(position+1)] == "CAG":
            polypeptide.append ("Gln")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "AAT" or mRNAseq[position:(position+1)] == "AAC":
            polypeptide.append ("Asn")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "AAA" or mRNAseq[position:(position+1)] == "AAG":
            polypeptide.append ("Lys")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "GAT" or mRNAseq[position:(position+1)] == "GAC":
            polypeptide.append ("Asp")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "GAA" or mRNAseq[position:(position+1)] == "GAG":
            polypeptide.append ("Glu")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "TGT" or mRNAseq[position:(position+1)] == "TGC":
            polypeptide.append ("Cys")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "TGG":
            polypeptide.append ("Trp")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "CGT" or mRNAseq[position:(position+1)] == "CGC" or mRNAseq[position:(position+1)] == "CGA" or mRNAseq[position:(position+1)] == "CGG" or mRNAseq[position:(position+1)] == "AGA" or mRNAseq[position:(position+1)] == "AGG":
            polypeptide.append ("Arg")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "GGT" or mRNAseq[position:(position+1)] == "GGC" or mRNAseq[position:(position+1)] == "GGA" or mRNAseq[position:(position+1)] == "GGG":
            polypeptide.append ("Gly")
            position = position + 1 
        elif mRNAseq[position:(position+1)] == "TAA" or mRNAseq[position:(position+1)] == "TAG" or mRNAseq[position:(position+1)] == "UGA":
            polypeptide.append ("STOP")
            print polypeptide
            position = len(mRNAseq)
        else:
            polypeptide.append("What the hell went wrong?")
            print polypeptide
            position = len(mRNAseq)
            
list = ["dog", "cat", "fish"]
def numberList(seq):
    number = 1
    for codon in seq:
        print(number. codon)
        number = number + 1

##def polypep_prod(mRNAseq, position):
##    for codon in mRNAseq:
