def donut_costs(num_donuts, member):
    '''
    Purpose: determines total cost of donuts for a customer based on membership status
    Parameter(s): num_donuts = how many donuts the customer purchases, member = True for yes or False for no
    Return Value: total cost in cents
    '''
    x = int(num_donuts)
    y = member
    if x>0 and y==True:
        if x == 1:
            return(x*(85))
        elif x<10:
            return(x*(75))
        else:
            return(x*(65))
    if x>0 and y==False:
        if x == 1:
            return(x*90)
        elif x<10:
            return(x*80)
        else:
            return(x*70)


def choose_three(text, optionA, optionB, optionC):
    '''
    Purpose: Asks user to select A, B, or C and provides selected choice
    Parameter(s): text (prompt), optionA, optionB, optionC
    Return Value: choice of letter (A, B, or C)
    '''
    print(text, '\n')

    print("A.", optionA)
    print("B.", optionB)
    print("C.", optionC)
    choice_of_A_B_C = input("Choose A, B, or C: ")
    while choice_of_A_B_C != "A" and choice_of_A_B_C != "B" and choice_of_A_B_C != "C":
        print ("Invalid option, try again.")
        choice_of_A_B_C = input("Choose A, B, or C: ")
    else: 
        return choice_of_A_B_C 

def adventure():
    '''
    Purpose: Asks user to select A, B, or C and provides selected choice
    Parameter(s): None
    Return Value: True or False based on letter choices.
    '''
    dinner_choice = choose_three('You are at the grocery store. You are trying to make dinner.', 'Make spahetti', 'Make a sandwhich', 'Make cereal')
    if dinner_choice == 'B':
       print('Bad choice. Nothing will be as good as Jimmy Johns.')
       return False
    if dinner_choice == 'A':
        type_sauce = choose_three('Mamma mia! Italian always hits the spot. What kind of sauce will you buy?', 'Alfredo Sauce', 'Vodka Sauce', 'Marinara')
        if type_sauce == 'A':
            print('The best sauce out there, now make sure you buy fettuccine.')
            return True
        if type_sauce == 'B':
            print('Great sauce, enjoy your dinner.')
            return True
        if type_sauce == 'C':
            type_meat = choose_three('You need some protein with that. What will you buy?', 'Meatballs', 'Eggs', 'Fish')
            if type_meat == 'A':
                print('Classy. Enjoy your spaghetti and meatballs.')
                return True
            if type_meat == 'C':
                print('That is a little weird. You should probably not be cooking.')
                return False
            if type_meat == 'B':
                print('Already thinking about breakfast? You must be hungry. You should just get fast food on the way home.')
                return False
    if dinner_choice == 'C':
        type_cereal = choose_three('I like your vibe. What kind of cereal will you get?', 'Raisin Bran', 'Cinnamon Toast Crunch','Lucky Charms')
        if type_cereal == 'A':
            print('Are you 70? No dinner for you.')
            return False
        if type_cereal == 'C':
            print('Good choice, now have fun picking out all the marshmallows.')
            return True
        if type_cereal == 'B':
            milk_choice = choose_three('Cinnamon Toast Crunch is way better with milk. Choose one.', 'Almond milk', 'Whole milk', 'I do not eat cereal with milk')
            if milk_choice == 'A':
                print('Good choice, almond milk all the way. Enjoy your dinner.')
                return True
            if milk_choice == 'B': 
                print(r'Oof. About 68% of the world is lactose intolerant... not great odds for you.') 
                return False
            if milk_choice == 'C':
                print('Cereal milk is the best part. You are nuts and do not deserve cereal anymore.')
                return False














if __name__=='__main__':
    print(donut_costs(1, True)) # Should output 85
    print(donut_costs(2, True)) # Should output 150
    print(donut_costs(10, True)) # Should output 650
    print(donut_costs(15, True)) # Should output 975
    print(donut_costs(1, False)) # Should output 90
    print(donut_costs(2, False)) # Should output 160
    print(donut_costs(10, False)) # Should output 700
    print(donut_costs(15, False)) # Should output 1050
    print(choose_three("Choose an ice cream flavor.", "Vanilla", "Chocolate", "Strawberry")) # Should output 
          #Choose an ice cream flavor
          #A. Vanilla
          #B. Chocolate
          #C. Strawberry
          #Choose A, B, or C: A
          #A 
    print(adventure())