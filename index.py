print ("Introductory Bioinformatics Experiment")

print ("Available Functions: First input produces the first mRNA strand as well as it's conversion to a polypeptide strand. Second input produces a list of mRNA strands as a dictionary.")

#SFTPA1 genome taken from NCBI RefSeq
SFTPA1 = "GACTTGGAGGCAGAGACCCAAGGCTGGAGGCTCTGTGTGTGGGTGAGTTTAGCCCCATCCCCTAGGT\
GTTCTCCAGCTTGAGGATCGCAGGCAGAGAGGACCAGCCCAGCAGCCACAGGCCTGACCAAAGCCCAGGCTGGGAAGG\
AGGGCAACTCCCCATTTTCCACTGGGAGGTGTTTCACAGCACAGTCAACATAGGTGACCTGCAAAGATCCTCATGTTTG\
TTATTTTCTTTGGCCAGATCCATCCCTACAGGGTTCAGCAGGGCCTACAGGAGGGGCAGTGAGAGAACAGACCCCAAAA\
AGAAAGGGGACTCCATGACTGACCACCTTGAGGGGGGCCAGGCTGCGGGCCCCGTTCATCTTTTTTCATTCTCAGGTCG\
CTGATTTCTTGGAGCCTGAAAAGAAAGTAACACAGCAGGGATGAGGACAGATGGTGTGAGTCAGTGAGTGAGTGACCTG\
ACTAATAGCCTGGGAGGGACAGGGCAGGTTTTCTGCAGAGCACGGAAGATTCAGCTGAAGTCAGAGAGGTGAAGCCAGT\
TTCCCAGGGTAACATAGTGAGGCACTGAAAGAAAGGAGACTGCACTGGAGCCCAGGTCCCCGGGCTCCCCAGAGCTCCT\
TACTCTTCCTCCTCCTCAGCAGCCTGGAGACCCCACAACCTCCAGCCGGAGGCCTGAAGCATGAGGCCATGCCAGGTGC\
CAGGTGATGCTGGGAATTTTCCCGGGAGCTTCGGGTCTTCCCAGCACTCTGGTCTCGCCCGCCCTGCCTCTCGGGCTCT\
GCCCAGCTTCCTGAGTCCTGACAGAGCACAGTGGGGGAGATGTTGGCAGAGGTGGCAGATGGGCTCACGGCCATCCCTC\
CTGCAGGAGCAGCGACTGGACCCAGAGCCATGTGGCTGTGCCCTCTGGCCCTCAACCTCATCTTGATGGCAGCCTCTGG\
TGCTGTGTGCGAAGTGAAGGACGTTTGTGTTGGAAGCCCTGGTATCCCCGGCACTCCTGGATCCCACGGCCTGCCAGGC\
AGGGACGGGAGAGATGGTCTCAAAGGAGACCCTGGCCCTCCAGGTACTGTGCTGCAGACCCCACCCTCAGCTGAGGGAC\
ACAGACCCCTTTTCAGGAGGCCCATCTGTCCAGGCCCCTAGGCTGTGGGCCATAGTGAGCTGGGGGCTATAGTAAGCTG\
GGTGGGACTTCAGTCTGCAGGGCTGGTGGGTTCCTGGGGCCCTTATGATGGCGCATCCTGGAGAGTCTGTCCTCATAGT\
GCCCACGGAGTGATAGAGTGATAGCTGAGCCAGCCCTGGTGATAATGGGCATCGAGTCTCACTAGCTCCAACCAGTTGT\
GGGTGACAGATCCTACACATCCATGTCTCTTTTCTCTGCAGGCCCCATGGGTCCACCTGGAGAAATGCCATGTCCTCCT\
GGAAATGATGGGCTGCCTGGAGCCCCTGGTATCCCTGGAGAGTGTGGAGAGAAGGGGGAGCCTGGCGAGAGGGGCCCTC\
CAGGTGAGCAGGGTGGGGCAGGTGGGCAGTGGAAACATGGGCACAGCGACCCTGAAGTCAGTTACACGGGGATGATGGG\
GATCAGACAAACCCTACAGGTTCCCCAAGGGCATTTGGCTCAACCTAAGTAAGAGAGGATAAGCTTGAGGGAGAAAGCT\
GAGGTGTCTGGGGAGTGTGGTCACAATTCAGGGAAAGGCAGGTGTGGGAAGTCCTCCGTGCCTCATGACCACCGATGGG\
GACACACTGAGTCAGGTGTGGGATGAGGGACAGCACTGGGAGGCAGGGGAGGCATGTCCTGGGATGGAGGCCCTGGGGG\
CTGTCTGAAGGGTGAATGCGGACGAGGCATCCAGACAGACGGTGTGATCAGGAGCCCCACAGACAGAGGGGAACTTTGA\
AGCTCAGAGCGGTAAGCAAGTCCATCAGGGCAGTGCAGAGAGCATCATGCTTGCCCTTGGTGGAGGGTGCGGGAGAGGG\
ACTTGCCCCACAGAGGCGGGCAGACAGAACCCCTCGAGGGACAGAGCAGGAAAGAGGACAAGGGGTGGGGGTCTCAGCA\
GGGGCAAGGCTTCACTAAAGAATAGGGGACCACGGGGTGTGGAGACACACTGGAATCTTGTGGACCCTCTGAGCCTAGG\
GTCTGGGTGGCGCCTAACAGCAATGAAAGGGCAGAGTTCCAGGATTGCAGATGGCAAAACACCTGCGTGGCAGCAAGTG\
GGAGTCTTCACTGGCCTGCCCCTCCTTCTGTGTGGGGCACTCTCCACAGGGCTTCCAGCTCATCTAGATGAGGAGCTCC\
AAGCCACACTCCACGACTTTAGACATCAAATCCTGCAGACAAGGGGAGGTAAGGGGACCCCCTGGGCCTCACGGGGTAG\
GAGTTTCCCACAAATTCCCCTCATTCTCAGCACCAGCTTCTAGAACATAGAGATTACAAATAGGCATGCACATGCAGGT\
CTTGGGGAAAGGAATGACGCTTGCTTTTCTGATGTCTTTGAATGGCCCAGAGGAGACAGAAGCAGACACAATTCACTCC\
CCATTTCATAGGAAAGCAAGTTCTCCACCTGCCTTGCTTTCCACTGAATTCCAGGAAATTGCACCATTTCTGGCAATAA\
GTAATTGTTACTTAGGTGAATGAATAAATGGAGGAGAGTCTAAAAGTGAATTTAGAAAACTGCAATTGGAAGAGGAAGA\
GAAGACACAGAGAGAGGCAGAGATGGAGAGACTGGGGAGAATCTGGTAGCAGAGACCCCAGGTGAGGGAGGTGGCTTAG\
AGACAAAGTGGTCAGTGGCCTGACCCGGACTCCTCTGCTCTCAGCCCTCAGTCTGCAGGGCTCCATAATGACAGTAGGA\
GAGAAGGTCTTCTCCAGCAATGGGCAGTCCATCACTTTTGATGCCATTCAGGAGGCATGTGCCAGAGCAGGCGGCCGCA\
TTGCTGTCCCAAGGAATCCAGAGGAAAATGAGGCCATTGCAAGCTTCGTGAAGAAGTACAACACATATGCCTATGTAGG\
CCTGACTGAGGGTCCCAGCCCTGGAGACTTCCGCTACTCAGACGGGACCCCTGTAAACTACACCAACTGGTACCGAGGG\
GAGCCCGCAGGTCGGGGAAAAGAGCAGTGTGTGGAGATGTACACAGATGGGCAGTGGAATGACAGGAACTGCCTGTACT\
CCCGACTGACCATCTGTGAGTTCTGAGAGGCATTTAGGCCATGGGACAGGGAGGACGCTCTCTGGCCTTCGGCCTCCAT\
CCTGAGGCTCCACTTGGTCTGTGAGATGCTAGAACTCCCTTTCAACAGAATTCACTTGTGGCTATTGGGACTGGAGGCA\
CCCTTAGCCACTTCATTCCTCTGATGGGCCCTGACTCTTCCCCATAATCACTGACCAGCCTTGACACTCCCCTTGCAAA\
CTCTCCCAGCACTGCACCCCAGGCAGCCACTCTTAGCCTTGGCCTTCGACATGAGATGGAGCCCTCCTTATTCCCCATC\
TGGTCCAGTTCCTTCACTTACAGATGGCAGCAGTGAGGTCTTGGGGTAGAAGGACCCTCCAAAGTCACACAAAGTGCCT\
GCCTCCTGGTCCCCTCAGCTCTCTCTCTGCAACCCAGTGCCATCAGGATGAGCAATCCTGGCCAAGCATAATGACAGAG\
AGAGGCAGACTTCGGGGAAGCCCTGACTGTGCAGAGCTAAGGACACAGTGGAGATTCTCTGGCACTCTGAGGTCTCTGT\
GGCAGGCCTGGTCAGGCTCTCCATGAGGTTAGAAGGCCAGGTAGTGTTCCAGCAGGGTGGTGGCCAAGCCAACCCCATG\
ATTGATGTGTACGATTCACTCCTTTGAGTCTTTGAATGGCAACTCAGCCCCCTGACCTGAAGACAGCCAGCCTAGGCCT\
CTAGGGTGACCTAGAGCCGCCTTCAGATGTGACCCGAGTAACTTTCAACTGATGAACAAATCTGCACCCTACTTCAGAT\
TTCAGTGGGCATTCACACCACCCCCCACACCACTGGCTCTGCTTTCTCCTTTCATTAATCCATTCACCCAGATATTTCA\
TTAAAATTATCACGTGCCAGGTCTTAGGATATGTCGTGGGGTGGGCAAGGTAATCAGTGACAGTTGAAGATTTTTTTTT\
CCCAGAGCTTATGTCTTCATCTGTGAAATGGGAATAAGATACTTGTTGCTGTCACAGTTATTACCATCCCCCCAGCTAC\
CAAAATTACTACCAGAACTGTTACTATACACAGAGGCTATTGACTGAGCACCTATCATTTGCCAAGAACCTTGACAAGC\
ACTTCTAATACAGCATATTATGTACTATTCAATCTTTACACAATGTCACGGGACCAGTATTGTTTCCTCATTTTTTATA\
AGGACACTGAAGCTTGGAGGAGTTAAATGTTTTGAGTATTATTCCAGAGAGCAAGTGGCAGAGGCTGGATCCAAACCCA\
TCTTCCTGGACCTGAAGCTTATGCTTCCAGCCACCCCACTCCTGAGCTGAATAAAGATGATTTAAGCTTAATAAATCGT\
GAATGTGTTCACA"

# FASTA link for SFTPA1: https://www.ncbi.nlm.nih.gov/nuccore/NG_021189.1?from=5001&to=9505&report=fasta

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

# start codon
METcodon = "ATG"
stopcodon1 = "TAA"
stopcodon2 = "TAG"
stopcodon3 = "TGA"

position = 0
start_pos = SFTPA1.index(METcodon)
mRNA_excess = SFTPA1[start_pos:];
mRNA_excess.find("STOP")

first_mRNA_excess = SFTPA1[(SFTPA1.find(METcodon)):]
first_mRNA = first_mRNA_excess[:(3 + (first_mRNA_excess.find(stopcodon1 or stopcodon2 or stopcodon3)))]

#produces mRNA from start to stop
mRNA = []
def mRNA_producer (DNAseq, position):
    while position < len(DNAseq):
        if DNAseq[position:position+3] == "ATG":
            mRNA.append("START")
            position = position + 3
            while position <= len(DNAseq):
                if DNAseq[position:(position + 3)] == stopcodon1 or DNAseq[position:(position + 3)] == stopcodon2 or DNAseq[position:(position + 3)] == stopcodon3:
                    mRNA.append("STOP")
                    return mRNA
                elif position == len(DNAseq) - 2 or position == len(DNAseq) - 1 or position == len(DNAseq):
                    return "no stop codon"
                else:
                    mRNA.append(DNAseq[position:(position + 3)])
                    position = position + 3
            position = len(DNAseq)
        elif position == len(DNAseq) - 2:
            return "No ORF"
            position = len(DNAseq)
        else:
            position = position + 1

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
            return polypeptide
        else:
            polypeptide.append("What the hell went wrong?")

start_codons = []
def start_posns(DNAseq, position):
    while position <= len(DNAseq) - 2:
        if DNAseq[position:position+3] == "ATG":
            start_codons.append(position)
            position = position + 3
        elif position == len(DNAseq) - 2:
            return start_codons
        else:
            position = position + 1

## produce single (first) mRNA strand and its translation
DNAsequence = str(input("Input DNA sequence:"))
mRNAinput = mRNA_producer(DNAsequence, 0)
polypeptide_producer(mRNA)

## produces a dictionary of possible mRNA strands given that a strand starts
## with an AUG codon

def mRNA_producer2 (DNAseq, position, lst):
    while position < len(DNAseq):
        if DNAseq[position:position+3] == "ATG":
            lst.append("START")
            position = position + 3
            while position <= len(DNAseq):
                if DNAseq[position:(position + 3)] == (stopcodon1 or stopcodon2 or stopcodon3):
                    lst.append("STOP")
                    return lst
                elif position == len(DNAseq) - 2 or position == len(DNAseq) - 1 or position == len(DNAseq):
                    return "no stop codon"
                else:
                    lst.append(DNAseq[position:(position + 3)])
                    position = position + 3
            position = len(DNAseq)
        elif position == len(DNAseq) - 2:
            return "No ORF"
            position = len(DNAseq)
        else:
            position = position + 1
            
mRNAlst = []
def multiple_mRNA2(DNAseq, start_posns):
    count = 0  
    for posn in start_posns:
        count = count + 1
        mRNAlst.append (mRNA_producer2(DNAseq, posn, []))
    return mRNAlst

mRNAdic = {}
def form_dic(lst):
    count = 0
    for strand in lst:
        count = count + 1
        key = "mRNA" + str(count)
        mRNAdic[key] = strand
        if strand == "no stop codon":
            mRNAdic[key] = strand
            break
        else:
            mRNAdic[key] = strand
    return mRNAdic

DNAsequence = str(input("Input DNA sequence to produce multiple mRNA:"))
start_posns(DNAsequence, 0)
mRNAlst = []
mRNAlst.append(multiple_mRNA2(DNAsequence, start_codons))
form_dic(mRNAlst)
return mRNAdic

## next steps:
## length 
