class Complex:
    '''
    Purpose: models complex number 
    Instance variables: self.real = real number, self.imag = imaginary number
    Methods: get methods get the number, set methods set a new number, __str__ gives result
    as a string, __add__ adds two numbers with imaginary components, __mul__ multiplies two numbers with imaginary components,
    __eq__ checks if two numbers are equivalent.
    '''
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def get_real(self):
         return self.real
    def get_imag(self):
         return self.imag
    def set_real(self, new_real):
         self.real = new_real
    def set_imag(self, new_imag):
         self.imag = new_imag
    def __str__(self):
          return (str(self.real) + " + " + str(self.imag) + 'i' )
    def __add__(self,other):
         newreal = (self.real + other.real)
         newimag = (self.imag + other.imag)
         return Complex(newreal,newimag)
    def __mul__(self,other):
         mulreal = ((self.real*other.real) - (self.imag*other.imag))
         mulimag = ((self.real*other.imag)+(self.imag*other.real))
         return Complex(mulreal,mulimag)

    def __eq__(self,other):
         if self.real == other.real and self.imag == other.imag:
              return True
         else:
              return False
         
class Decision:
     '''
     Purpose: represents each decision point
     Instance variables: self.prompt = prompt provided, self.options = empty list of options to be added,
     self.results = result from the options
     Methods: add_options adds options to the list, run() runs the program with associated prompts and 
     decisions from user input to obtain result.
     '''

     def __init__(self,prompt):
          self.prompt = prompt
          self.options = []
          self.results = []
     def add_option(self, option, result):
          self.options.append(option)
          self.results.append(result)
     def run(self):
          if self.options == []:
               return "No options available."
          else: 
               print()
               print(self.prompt)
               print()
               for opt in self.options:
                    print((str(self.options.index(opt)))+'. '+opt)
                    num = len(self.options)-1
               
               
     
               while True:
                    choice = input("Enter a number between 0 and "+str(num)+": ")
                    if choice.isdigit() and int(choice) >=0 and int(choice) <= num:
                         result_choice = self.results[int(choice)]
                         if type(result_choice) == str:
                              return(result_choice)
                         else:
                              return result_choice.run()
                         
                    else:
                         print("Invalid choice, try again.")
               
import csv
class Flowchart:
     '''
     Purpose: opens file and adds all prompts and options to a list for user input.
     Instance variables: self.decisions = empty list to be added to from file.
     Methods: __init__ opens file and adds each decision/prompt to list, start(self) runs the program with first index of self.decisions.
     '''

     def __init__(self,filename):
          self.decisions = []
          with open(filename, 'r') as file:
               text = csv.reader(file)
               for row in text:
                    if row[0] == 'Decision':
                         decision = Decision(row[2])

                         self.decisions.append(decision)
                    elif row[0] == 'Ending':
                         self.decisions[int(row[1])].add_option(row[2], row[3])
                    elif row[0] == 'Path':
                         source = self.decisions[int(row[1])]
                         destination = self.decisions[int(row[3])]
                         source.add_option(row[2],destination)
     def start(self):
          return self.decisions[0].run()
     


     







# if __name__ == '__main__':
#      # courses = Flowchart('next_course.csv')
#      # print(courses.start())
#      dragon = Flowchart('story1.csv')
#      print(dragon.start())


#     x = Complex(2.7, 3)
#     print(x.real) #2.7
#     print(x.imag) #3
#     print(x.get_real()) #2.7
#     print(x.get_imag()) #3
#     x.set_real(8)
#     print(x) #8 + 3i
#     x.set_imag(-4.5)
#     print(str(x) == '8 + -4.5i') #True

#     print()
#     x = Complex(1.5, 4)
#     y = Complex(-2, 0)
#     print(x+y) #-0.5 + 4i
#     print(x) #1.5 + 4i
#     print(y) #-2 + 0i
#     z = Complex(0, -1.5)
#     print(z+y+x) #-0.5 + 2.5i

#     print()
#     x = Complex(6, 3)
#     z = Complex(0, -2.5)
#     print(x*z) #7.5 + -15.0i
#     y = Complex(-4, 2)
#     print(x*y) #-30 + 0i
#     print(x*(y+z)) #-22.5 + -15.0i
#     print(x*y*z) #0.0 + 75.0i

#     print()
#     print(Complex(4, 2) == Complex(4, 3)) #False
#     print(Complex(2, 6) == Complex(4, 6)) #False
#     print(Complex(3, 5) == Complex(3, 5)) #True
#     x = Complex(6, 3)
#     y = Complex(-4, 2)
#     z = Complex(0, -2.5)
#     print(x*y+x*z == x*(y+z)) #True

