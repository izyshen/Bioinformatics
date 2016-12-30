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
        
## something is only a coding ORF if it has 100+ amino acids

def lister (DNAseq, position):
    curr_list = ("start")
    while len(DNAseq) != 0:
        print curr_list.extend(DNAseq[position:(position + 3)])
        position = position+3

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
            
## list produced inside fcn, for production of polycistronic mRNA strands
def mRNA_producer2 (DNAseq, position):
    mRNA = []
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
            
# using for loop
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

def multiple_mRNA(DNAseq, start_posns):
    count = 0
    for posn in start_posns:
        count = count + 1
        mRNA_producer2(DNAseq, posn)
        print "mRNA" + (str(count)) + ":" + (str(mRNA))

##make a dictionary with this
##see what's longer than 100 AA
        
DNAsequence = str(raw_input("Input DNA sequence:"))
mRNAinput = mRNA_producer(DNAsequence, 0)
polypeptide_producer(mRNA)

DNAsequence = str(raw_input("Input DNA sequence to produce multiple mRNA: "))
start = start_posns(DNAsequence, 0)
multiple_mRNA(DNAsequence, start)

