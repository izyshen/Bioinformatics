print ("Test Page")

testDNA = "ATGCAACGTATTGACCTTTTACTGTACTAA"

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


# for loops
## list of codons
##def lister (DNAseq, position):
##    while position < len(DNAseq) - 2: 
##        print (DNAseq[position:(position + 3)])
##        position = position + 3

def lister (DNAseq, position, curr_list):
    curr_list = ()
    while len(DNAseq) != 0:
        print curr_list.extend(DNAseq[position:(position + 3)])
        DNAseq[position+3:]
        
#this only lists each nucleotide.
#Want to list them as codons to implement translation
def codon_counter(DNAseq, position):
    number = 1
    for codon in DNAseq:
        print(number, codon)
        number = number + 1
        
def main_fcn():
    lister(testDNA, 0)
    codon_counter(lister(testDNA, 0), 0)


##def tripleAll(nums):
##    for val in nums:
##        print val*3
##n = int(input('Enter the number of times to repeat: '))
##for i in range(n):
##    print('This is repetitious!')

def numberList(items):
    number = 1
    for item in items:
        print(number, item)
        number = number + 1

def main():
    numberList(['red', 'orange', 'yellow', 'green'])
    print()
    numberList(['apples', 'pears', 'bananas'])


