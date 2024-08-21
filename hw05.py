def greater_by_one_for(a_string):
    '''
    Purpose: returns string with all # betw 0 and 8 replaced with digit one value higher, 9s replaced with 0
    Parameter(s): a_string, string of digits
    Return Value: string of altered digits 
    '''
    integer_list = []
    added_int_list = []
    new_str = ''
    for element in a_string:
        element = int(element)
        integer_list.append(element)
        num = 0 
    for num in integer_list:
        if num >= 0 and num <= 8:
            num = num + 1 
            added_int_list.append(num)
        elif num == 9:
            num = 0
            added_int_list.append(num)
        else:
            added_int_list.append(num)
    for val in added_int_list:
        val = str(val)
        new_str += val
    return new_str
            
   
def greater_by_one_while(a_string):
    '''
    Purpose: returns string with all # betw 0 and 8 replaced with digit one value higher, 9s replaced with 0
    Parameter(s): a_string, string of digits
    Return Value: string of altered digits 
    '''
    
    n = 0
    lengthstring = len(a_string)
    new_string = ''
   
    while n<lengthstring:
        num_n = int(a_string[n])
        if 0<=num_n<=8:
            num_n = num_n + 1 
        elif num_n == 9:
            num_n = 0
        else: 
            num_n = num_n
        # int_of_a_string.append(str(num_n))
        new_string += str(num_n)
        n = n + 1
    return new_string
    

def count_of_sums(lower, upper, sum_val):
    '''
    Purpose: represents all possible ways to sum two ints between upper and lower to get sum_val
    Parameter(s): lower(inclusive bottom of searchable range), upper(inclusive upper end of searchable range), sum_val(integer sum checking against)
    Return Value: int representing all possible ways
    '''
    i = lower
    x = lower
    count = 0
    while x <= upper:
        while i <= upper:
            if x + i == sum_val:
                count = count + 1
                i = i + 1
            elif x + i != sum_val: 
                i = i + 1
        x = x + 1
        i = lower
    return count



def character_search(string_a, string_b, string_c):
    '''
    Purpose: provides all characters in string_a and string_b but not in string_c
    Parameter(s): string_a, string_b, string_c (all string objects)
    Return Value: string of characters in string_a and string_b but not in string_c
    '''
    i = 0
    j = 0
    in_a_and_b = ''
    while j < len(string_b):
            while i < len(string_a):
                while string_a[i] == string_b[j] and string_a[i] not in string_c:
                    in_a_and_b = in_a_and_b + str(string_a[i])
                    i += 1
                else:
                    i += 1
            i = 0
            j += 1
    return in_a_and_b

   
if __name__=='__main__':
    print(greater_by_one_for("")) # Should output ''
    print(greater_by_one_for("123")) # Should output '234'
    print(greater_by_one_while("234")) # Should output '345'
    print(greater_by_one_for("93023")) # Should output '04134'
    print(greater_by_one_while("93023")) # Should output '04134'
    print(count_of_sums(2, 10, 8)) # Should output 5
    print(count_of_sums(0, 15, 15)) # Should output 16
    print(count_of_sums(-4, 8, 6)) # Should output 11
    print(count_of_sums(5, 8, 30)) # Should output 0
    print(character_search("ABCDEFGHI", "ABCD", "abCd")) # Should output 'ABD'
    print(character_search("cats dog", "cats", "a")) # Should output 'cts'
    print(character_search("cats dog", "rats", "a")) # Should output 'ts'
    print(character_search("cats dog", "cats ", "cats")) # Should output ''

