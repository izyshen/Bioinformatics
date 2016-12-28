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
        

## something is only a coding ORF if it has 100+ amino acids

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

## print mRNA codons as a list
mRNA = []

def mRNA_producer (DNAseq, position):
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

##def polypep_prod(mRNAseq, position):
##    for codon in mRNAseq:
##mRNA = mRNA_producer(testDNA, 0)
##print mRNA

DNAsequence = str(raw_input("Input DNA sequence:"))
mRNAinput = mRNA_producer(DNAsequence, 0)
polypeptide_producer(mRNA, 0)

#polypeptide_result = polypeptide_producer(mRNAinput, 0)
##print polypeptide_result
