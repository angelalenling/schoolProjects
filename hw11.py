def collatz(n):
    '''
    Purpose: takes number and creates collatz sequence from the number to 1, then returns sum of these numbers
    Parameter(s): n = single positive integer
    Return Value: sum of numbers in collatz sequence from n to 1
    '''
    if n == 1:
        return n 
    elif n % 2 == 0:
        return n + collatz(n//2)
    elif n % 2 != 0:
        return n + collatz((3*n)+1)
    
def two_es(lines):
    '''
    Purpose: checks each line in each doc for 'ee' and determines if file is decoy or not
    Parameter(s): lines = list of strings representing each line of a doc
    Return Value: boolean value (True = file is target, False = decoy)
    '''
    if len(lines) == 0:
        return False
    elif len(lines) != 0:
       if lines[0].count('e') != 2:
           return two_es(lines[1:])
    return True


import os
def get_targets(path):
    '''
    Purpose: provides list of paths to files that are targets
    Parameter(s): path = directory to search through
    Return Value: list of paths
    '''
    directories = []
    for file in os.listdir(path): 
        if os.path.isfile(path+'/'+file):
            if file.endswith('.txt'):
                f = open(path+'/'+file, "r")
                if (two_es((f.readlines()))) == True:
                    directories.append(path+'/'+file)
        else:
            directories += get_targets(path+'/'+file) 
    return directories





# if __name__ == '__main__':
    # print(collatz(5))#36
    # print(collatz(1))#1
    # print(collatz(123))#6390
    # print(two_es(['One line\n', 'Two lines\n', 'Three lines\n']))#True
    # print(two_es(['here is a line\n', 'Another linE, starting with A\n', 'One MorE linE']))#False
    # print(two_es([]))#False
    # print(two_es(['More examples\n', 'Here there are two lines that work\n', 'This is one of them\n', 'This is not\n', 'Excellent']))#True
    # print(get_targets('docs1'))
    # print(get_targets('docs2'))
    # print(get_targets('docs3/North_America'))

