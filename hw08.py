def durdle_match(guess, target):
    '''
    Purpose: player inputs a guess for the target word and function returns string of G, Y, or B based on each letter
    Parameter(s): (guess,target) players guess and target word that the player is attempting to guess, both lowercase strings
    Return Value: string if same length as target with letters G, Y, B with associated meanings:
                    G: This letter in the guess appears in the same location in the target string
                    Y: This letter in the guess appears in the target string in another location
                    B: This letter in the guess does not appear in the target string
    '''
    durdle = ''
    for n in range(len(guess)):
        if guess[n] == target[n]:
            durdle += 'G'
        elif guess[n] in target:
            durdle += 'Y'
        else:
            durdle += 'B'
    return durdle

def durdle_game(target):
    '''
    Purpose: user inputs words to guess target, and function determines durdle_match of word and if guess is valid or not. If guessed the number of guesses is returned.
    Parameter(s): target, string that will be the target to guess
    Return Value: returns amount of guesses
    '''
    guesses = 0
    print('Welcome to Durdle! The target word has', str(len(target)), 'letters.')
    b = 0
    while b == 0: 
        guess = input('Enter a guess:')
        if len(guess) == len(target) and guess.islower() == True and guess.isalpha() and ' ' not in guess:
            print(' '*13, durdle_match(guess, target))
            if 'Y' in durdle_match(guess, target) or 'B' in durdle_match(guess, target):
                guesses += 1
            if 'Y' not in durdle_match(guess, target) and 'B' not in durdle_match(guess, target):
                guesses += 1
                print('Congratulations, you got it in', guesses, 'guesses!')
                b = 1
        else:
            print("Invalid guess.")
    return guesses


def get_genes(dna_string):
    '''
    Purpose: separates dna_string into segments of DNA between (but not including) start and stop codons
    Parameter(s): dna_string, string of uppercase DNA sequence
    Return Value: list of strings of separate genes between (but not including) start and stop codons
    '''
    start_codon = 'ATG'
    stop_codon = 'TAG', 'TAA', 'TGA'
    dna = dna_string
    genes_list = []
    while start_codon in dna:
        indx_start = dna.index(start_codon)
        dna = dna[indx_start + 3:]
        stop_codon_loc = []
        if 'TAG' in dna:
            stop_codon_loc.append(dna.index('TAG'))
        if 'TGA' in dna:
            stop_codon_loc.append(dna.index('TGA'))
        if 'TAA' in dna:
            stop_codon_loc.append(dna.index('TAA'))
        first_stop_codindx = (min((stop_codon_loc)))  
        genes_list.append(dna[0:first_stop_codindx])
        dna = dna[first_stop_codindx + 3:]
    return genes_list

# if __name__ == '__main__':
    # print(durdle_match('quick', 'perky')) #BBBBY 
    # print(durdle_match('test','deft')) #YGBG
    # print(durdle_match('wizard','zicron')) #BGYBYB
    # print(durdle_match('parry','perky')) #GBGYG
    # print(durdle_match('guessing','guessing')) #'GGGGGGGG'
    # print(durdle_game('parameter'))
    # print(get_genes("TCATGTGCCCAATTCTGACCTACGATGGCCCAATAGCG"))
    # print(get_genes('ATTGCGCTACGCATC'))
    # print(get_genes('CATGTGTGAC'))
    # print(get_genes('ATGGTATCGTAAGATGGGGGTAGATATGTGA'))



