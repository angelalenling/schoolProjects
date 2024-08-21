// Names: Angela Lenling , Max Swanson
// x500s: lenli005 , swan3103

import java.util.*;

public class MyMaze {
    Cell[][] maze;
    int mazeRowsLength;
    int mazeColsLength;

    public MyMaze(int rows, int cols) { //creates new cell for each index given
        maze = new Cell[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                maze[i][j] = new Cell();
            }
        }
        mazeRowsLength = rows;
        mazeColsLength = cols;
    }
    public boolean isValidCell(int row, int col) {  // method checks if the indices of a cell are within the bounds of an array
        if (row >= 0 && row < mazeRowsLength && col >= 0 && col < mazeColsLength) {
            return true;
        } else {
            return false;
        }
    }
    public Cell getCell(int row, int col) { //method to get the cell object from the maze at the position of the integers that are given.
        if (!isValidCell(row,col)) {
            System.out.println("Cell does not exist within maze, returning cell at 0,0 instead.");
            return maze[0][0];
        }
        else{return maze[row][col];}
    }

    public static MyMaze makeMaze(int rows, int cols) {
        MyMaze newMaze = new MyMaze(rows, cols);
        Random rand = new Random();

        Stack<int[]> stack = new Stack<>(); //initializes Stack with int array objects
        int[] startIndx = {0, 0};
        stack.push(startIndx);  // adds start index to top of stack
        newMaze.getCell(0, 0).setVisited(true); // sets first index of maze as visited
        while (!stack.isEmpty()) {
            int[] currentIndx = stack.peek();   // checks top of stack and splits the indices of it into i and j
            int i = currentIndx[0];
            int j = currentIndx[1];
            ArrayList<int[]> neighborList = new ArrayList<>(); // Array list is created to hold the integer array of each neighbor to the currentIndx
            if (newMaze.isValidCell(i - 1, j)) {  // if the cell above the currentIndx is a valid cell that is unvisited, adds it to the neighborsList
                if (!newMaze.getCell(i - 1, j).getVisited()) {
                    neighborList.add(new int[]{i - 1, j});
                }
            }
            if (newMaze.isValidCell(i, j - 1)) { // if the cell left of the currentIndx is a valid cell that is unvisited, adds it to the neighborsList
                if (!newMaze.getCell(i, j - 1).getVisited()) {
                    neighborList.add(new int[]{i, j - 1});
                }
            }
            if (newMaze.isValidCell(i + 1, j)) { // if the cell below the currentIndx is a valid cell that is unvisited, adds it to the neighborsList
                if (!newMaze.getCell(i + 1, j).getVisited()) {
                    neighborList.add(new int[]{i + 1, j});
                }
            }
            if (newMaze.isValidCell(i, j + 1)) { // if the cell right of the currentIndx is a valid cell that is unvisited, adds it to the neighborsList
                if (!newMaze.getCell(i, j + 1).getVisited()) {
                    neighborList.add(new int[]{i, j + 1});
                }
            }
            if (!neighborList.isEmpty()) {  // if neighborsList is not empty, then it is not a dead end so we can choose a random direction from the valid neighboring cells
                int size = neighborList.size();
                int[] nextCell = neighborList.get(rand.nextInt(size)); //get random value from list method from https://www.baeldung.com/java-random-list-element
                int nextCellRow = nextCell[0];
                int nextCellCol = nextCell[1];
                stack.push(nextCell); // the new random cell is then pushed to the stack
                Cell cell = newMaze.getCell(nextCellRow, nextCellCol);
                cell.setVisited(true); // this cell is set as visited in the maze
                if (nextCellRow == i - 1) {  // if the cell was above the previous cell, then it removes the wall between those cells
                    newMaze.getCell(i - 1, j).setBottom(false);
                }
                if (nextCellCol == j - 1) { // if the cell was to the left of the previous cell, then it removes the wall between those cells
                    newMaze.getCell(i, j - 1).setRight(false);
                }
                if (nextCellRow == i + 1) { // if the cell was below the previous cell, then it removes the wall between those cells
                    newMaze.getCell(i, j).setBottom(false);
                }
                if (nextCellCol == j + 1) { // if the cell was to the right of the previous cell, then it removes the wall between those cells
                    newMaze.getCell(i, j).setRight(false);
                }
            } else {
                stack.pop(); // otherwise if neighborsList IS empty, then it was a dead end and the currentIndx is popped from the stack
            }
        }
        for (int i = 0; i < rows; i++) {   // resets all cells as not visited
            for (int j = 0; j < cols; j++) {
                newMaze.getCell(i, j).setVisited(false);

            }
        }
        return newMaze;
    }

    public void printMaze(boolean path) {  // print method designed from algorithm in write up
        String[][] printedMaze = new String[(mazeRowsLength * 2) + 1][(mazeColsLength * 2) + 1]; // creates larger array to hold strings
        for (int i = 0; i < mazeRowsLength; i++) {

            for (int j = 0; j < mazeColsLength; j++) {
                if (path == true) { // if we want to see the path of stars in the maze

                    if (getCell(i, j).getVisited()) {
                        printedMaze[(2 * i) + 1][(2 * j) + 1] = " * ";
                    }
                    else{printedMaze[(2 * i) + 1][(2 * j) + 1] = "   ";}
                }
                if (path == false) { // if we do not want to see the path of stars
                    printedMaze[(2 * i) + 1][(2 * j) + 1] = "   ";
                }

                if (getCell(i, j).getRight()) {
                    printedMaze[(2 * i) + 1][(2 * j) + 1 + 1] = "|";
                }
                if (!getCell(i, j).getRight()) {
                    printedMaze[(2 * i) + 1][(2 * j) + 1 + 1] = " ";
                }
                if (getCell(i, j).getBottom()) {
                    printedMaze[(2 * i) + 1 + 1][(2 * j) + 1] = "---";
                }
                if (!getCell(i, j).getBottom()) {
                    printedMaze[(2 * i) + 1 + 1][(2 * j) + 1] = "   ";
                }

                printedMaze[(2 * i) + 1 + 1][(2 * j) + 1 + 1] = "|";

            }
        }
        for (int i = 1; i < maze[0].length + 1; i++) { // prints top wall
            printedMaze[0][i] = "---|";
        }
        for (int i = 0; i < printedMaze.length; i++) { // prints left wall
            printedMaze[i][0] = "|";
        }
        printedMaze[1][0] = " "; // initial maze entry point
        printedMaze[printedMaze.length - 2][printedMaze[0].length - 1] = "   ";

        for (int i = 0; i < printedMaze.length; i++) {
            for (int j = 0; j < printedMaze[0].length; j++) {
                if (printedMaze[i][j] == null) {
                    System.out.print(" ");
                } else {
                    System.out.print(printedMaze[i][j]); // prints the array of strings to the terminal window
                }
            }
            System.out.println();

        }


    }

    /* TODO: Solve the maze using the algorithm found in the writeup. */
    public void solveMaze() {
        Random rand = new Random();
        Queue<int[]> queue = new LinkedList<>();
        int[] startIndex = {0, 0};
        queue.add(startIndex);
        while (!queue.isEmpty()) {
            int[] frontIndex = queue.poll(); // removes the front index from the queue
            getCell(frontIndex[0], frontIndex[1]).setVisited(true); // sets front cell with this index to visited
            if (frontIndex[0] == mazeRowsLength - 1 && frontIndex[1] == mazeColsLength - 1) {
                break; // maze is solved and is at the last index
            }
            int i = frontIndex[0];
            int j = frontIndex[1];
            if (isValidCell(i - 1, j)) { // if the cell above is valid, then progresses
                if (!getCell(i - 1, j).getBottom()) { // if no wall and unvisited then adds to the queue
                    if (!getCell(i - 1, j).getVisited()) {
                        queue.add(new int[]{i - 1, j});
                    }
                }
            }
            if (isValidCell(i, j - 1)) { // if the cell to the left is valid, then progresses
                if (!getCell(i, j - 1).getRight()) { // if no wall and unvisited then adds to the queue
                    if (!getCell(i, j - 1).getVisited()) {
                        queue.add(new int[]{i, j - 1});
                    }
                }
            }
            if (isValidCell(i + 1, j)) { // if the cell below is valid, then progresses
                if (!getCell(i, j).getBottom()) { // if no wall and unvisited then adds to the queue
                    if (!getCell(i + 1, j).getVisited()) {
                        queue.add(new int[]{i + 1, j});
                    }
                }
            }
            if (isValidCell(i, j + 1)) { // if the cell to the right is valid, then progresses
                if (!getCell(i, j).getRight()) { // if no wall and unvisited then adds to the queue
                    if (!getCell(i, j + 1).getVisited()) {
                        queue.add(new int[]{i, j + 1});
                    }
                }
            }
        }
    }


    public static void main(String[] args){
        /* Any testing can be put in this main function */
        MyMaze maze = makeMaze(5,5);
        maze.solveMaze();
        System.out.println();
//        MyMaze maze2 = makeMaze(10,10);
//        maze2.solveMaze();
//        System.out.println();
        maze.printMaze(true);
        System.out.println();
//        maze2.printMaze(true);


//        System.out.println("Testing isValidCell method: ");
//        System.out.println();
//        System.out.println("Expected val of maze.isValidCell(-1,0) is false");
//        System.out.println("Actual Value: ");
//        System.out.println(maze.isValidCell(-1,0)); // Expected: false
//        System.out.println();
//        System.out.println("Expected val of maze.isValidCell(1,3) is true");
//        System.out.println("Actual Value: ");
//        System.out.println(maze.isValidCell(1,3)); // Expected: true
//        System.out.println();
//        System.out.println("Expected val of maze.isValidCell(5,21) is false");
//        System.out.println("Actual Value: ");
//        System.out.println(maze.isValidCell(5,11)); // Expected: false
//        System.out.println();
//
//        System.out.println("Testing getCell method: ");
//        System.out.println();
//        System.out.println("Expected val of maze.getCell(0,0) is class Cell");
//        System.out.println("Actual Value: ");
//        System.out.println(maze.getCell(0,0).getClass()); // Expected: Cell
//        System.out.println();
//        System.out.println("Expected val of maze.getCell(1,4) is class Cell");
//        System.out.println("Actual Value: ");
//        System.out.println(maze.getCell(1,4).getClass());
//        System.out.println();
//        System.out.println("Expected val of maze.getCell(-1,4) is invalid cell, returning type at 0,0 instead");
//        System.out.println("Actual Value: ");
//        System.out.println(maze.getCell(-1,4).getClass());



    }
}
