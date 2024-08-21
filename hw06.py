def list_difference(numlist1, numlist2):
    '''
    Purpose: finds the difference between alist and blist for each index without mutating either list 
    Parameter(s): numlist1, numlist2 (list of numeric values of same length)
    Return Value: new list with difference between respective items
    '''
    diff_lists = []
    n = 0
    for i in numlist1:
        while n < len(numlist1) and numlist1 != []:
            diff_lists.append(numlist1[n] - numlist2[n])
            n = n + 1
    return diff_lists
    


def larger_decrement(numlist,n):
    '''
    Purpose: if list has # larger than n, mutate list by decreasing the largest item in list by 1, if two elements tied
             for largest, only decrease first one
    Parameter(s): numlist(list of integers), n (integer)
    Return Value: boolean value True, or if no numbers larger than n, False
    '''
    i = 0
    j = 0
    k = 0
    largest_num = 0
    for val in numlist:
        if val > n and j ==0:
            j = j + 1
            while k < len(numlist):
                if numlist[i] > largest_num:
                    largest_num = numlist[i]
                    i = i + 1
                    k = k + 1
                else:
                    i = i + 1
                    k = k + 1
            numlist[numlist.index(largest_num)] = largest_num - 1
            return True
        else:
            j = 0
    if j == 0:
        return False
        


def word_mix(wordlist1, wordlist2):
    '''
    Purpose: concatenates alternating strings from each list starting with wordlist1, inserting a space between strings. If lists are
             uneven, continue concatenating strings from the list with more items. Final string should not have space at end. 
    Parameter(s): wordlist1, wordlist2: two lists that contain strings
    Return Value: string of concatenated lists. 
    '''
    n = 0
    new_list = ''
    if len(wordlist1) > len(wordlist2):
        while n < len(wordlist2):
            new_list += str(wordlist1[n]) + ' '
            new_list += str(wordlist2[n]) + ' '
            n = n + 1 
        while n < (len(wordlist1) - 1):
            new_list += str(wordlist1[n]) + ' '
            n = n + 1
        while n < len(wordlist1):
            new_list += str(wordlist1[n])
            n = n + 1
    elif len(wordlist1) < len(wordlist2):
        while n < len(wordlist1):
            new_list += str(wordlist1[n]) + ' '
            new_list += str(wordlist2[n]) + ' '
            n = n + 1 
        while n < (len(wordlist2) - 1):
            new_list += str(wordlist2[n]) + ' '
            n = n + 1
        while n < len(wordlist2):
            new_list += str(wordlist2[n])
            n = n + 1
    else:
        while n < len(wordlist1)-1:
            new_list += str(wordlist1[n]) + ' '
            new_list += str(wordlist2[n]) + ' '
            n = n + 1 
        while n < len(wordlist1):
            new_list += str(wordlist2[n])
            n = n + 1
    return new_list





  








if __name__ == '__main__':
    print(list_difference([0,1,1,2], [3,5,8,13])) # outputs [-3, -4, -7, -11]
    alist = [5,6,7]
    blist = [2,2,2]
    print(list_difference(alist, blist)) # outputs [3, 4, 5]
    print(list_difference([],[])) # outputs []
    alist = [5, 20, 74, 81, 0, 81, 3]
    print(larger_decrement(alist, 50))
    print(alist)
    blist = [1, 3, 5]
    print(larger_decrement(blist, 6))
    print(blist)
    print(word_mix(['the','brown'],['quick','fox'])) # outputs 'the quick brown fox'
    print(word_mix(['the','brown','jumped','over'], ['quick','fox'])) # outputs 'the quick brown fox jumped over'

