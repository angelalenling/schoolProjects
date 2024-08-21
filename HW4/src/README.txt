Lenli005 with partner Swan3103

MyMaze has 3 main attributes. Cell[][] maze which holds the Cell array for the maze , mazeRowsLength and mazeColsLength which keep track of the lengths of rows and columns for later use.

The method MyMaze creates the maze of Cell objects for a size given by the user.

The method isValidCell takes an int row and int col and checks the dimensions of the maze to make sure the cell is within the bounds.
 
The method getCell takes an int row and int col and returns the Cell associated with those indices from the maze. This allows the functions from the Cell class to be used at all times on certain indices correlating to cells within the maze. 

The method makeMaze takes in int rows and int cols and creates a new MyMaze object. Then a stack is created to keep track of indices.
The first index is 0,0 and it is added to the stack and the corresponding cell is set as visited. Then until the stack is empty, the top of the stack is retrieved and an arraylist of the neighboring cells is created. The cells that are valid and unvisited are chosen from at random and then the new random cell is pushed to the stack and the wall between the old and new cell is removed. If there are no valid and unvisited neighboring cells, then it is a dead end and the stack's top element is popped. This continues until the entire maze is created and the stack is empty. All 	cells are then reset to unvisited before the maze is returned.

The method printMaze takes in a boolean path that determines whether the stars are printed with the solved path or not. A larger string array is created and filled with walls corresponding to how they were set in the makeMaze method. The start and end points are left open. If path is true then a star is printed if the method solveMaze sets a point to visited. 

The method solveMaze takes in nothing and creates a queue with start index of 0 and performs similarly to the makeMaze method. Each unvisited and unblocked cell (by walls) is added to the queue and while the queue is not empty and each cell is marked as visited. This continues until the end index is reached which means the maze is solved.  

The Main method of MyMaze creates a MyMaze object called "maze" with 5 rows and 20 columns and 10 rows and 10 columns. solveMaze is then called on the maze, and the maze is printed with print flag as false to show the maze with the path set by *s. 

The Glassbox tests of the methods isValidCell and getCell are shown. The expected return value for three different branch tests of isValidCell are displayed, with false, true, and false expected for the individual tests respectivley to check the bounds of input.
getCell is also tested with different branches and the expected return values and actual values are printed to the screen checking the bounds of input.


The Cell Class contains methods to set each Cell object as visited and to set a right and bottom wall. It also has getter methods for each of these that return booleans of each. 


