
import java.util.*;
import java.io.*;
/**
 * <h1>WindData</h1>
 * The WindData program receives data from a file specified, organizes the data,
 * and prompts the user for an interval, and prompts the user to compute probabilities based on the data.
 * It then outputs a file with the data for each interval.
 *
 *
 * @author  Angela Lenling Lenli005
 * @version 1.0
 * @since   2023-12-14
 */

public class WindData {
    /**
     * This method is used to obtain  a filename containing wind data.
     * @return String This returns the file name from user.
     * @exception IOException On input error.
     * @see IOException
     */
    public String getFileString() throws IOException {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter file name: ");
        String fileName = s.nextLine();
        return fileName;
    }
    /**
     * This method is used get a valid interval from the user.
     * @return double This returns the interval specified by the user.
     */
    public static double getUserDefinedInterval(){
        Scanner scnr = new Scanner(System.in);
        double userDefinedInterval;
        do{
            System.out.println("Enter the desired width of each interval (between 50 and 100mph^2): ");

            while(!scnr.hasNextDouble()){
                System.out.println("Error: please enter a valid number.");
                scnr.next();
            }
            userDefinedInterval = scnr.nextDouble();
            if(userDefinedInterval < 50 || userDefinedInterval > 100){
                System.out.println("Error: please enter a number between 50 and 100mph^2");
            }
        }
        while(userDefinedInterval < 50 || userDefinedInterval > 100);
        return userDefinedInterval;
    }

    /**
     * This is the main method which makes use of getFileString and getUserDefinedInterval methods.
     * It calculates cumulative probabilities and K value for each interval and writes them to a new file.
     *
     * @param args User input on file name, interval, and probabilities based on wind data.
     * @exception IOException On input error.
     * @see IOException
     */
    public static void main(String[] args) throws IOException {
        ArrayList<Double> windValues;
        double userDefinedInterval;
        double numWindValues;
        windValues = new ArrayList<>(9000);  //initializes arraylist of size 9000 and type Double
        System.out.println("What is the file name?");
        WindData data = new WindData();
        File windFile = new File(data.getFileString());
        Scanner s = new Scanner(windFile);
        for(int i = 1; i<=7 && s.hasNextLine(); i++){
            s.nextLine();
        }
        while (s.hasNextLine()) {
            String[] line = s.nextLine().split(",");
            if (line[5].matches("\\d*\\.?\\d+")){ // checks if wind speed is only digits and decimals (from stack overflow)
            windValues.add(Double.parseDouble(line[5]));
            }
            else{
                System.out.println("Wind speed from " + line[0] + " is: " + line[5] + " which is not a floating point number.");
            }
        }
        userDefinedInterval = getUserDefinedInterval();
        numWindValues = windValues.size();
        Bin [] histogram = new Bin[200];
        for (int i = 0; i < 200; i++){
            histogram[i] = new Bin(i * userDefinedInterval, 0, 0);
        }
        for (int i = 0; i < numWindValues; i++) {
            for (int j = 0; j < 200; j++) {
                if (((Math.pow((windValues.get(i)),2)) >= histogram[j].getInterval()) && ((Math.pow((windValues.get(i)),2)) < histogram[j+1].getInterval())){
                    histogram[j].setCount(histogram[j].getCount() + 1);
                    break;
                }
            }
        }
        double Cumulative_P = 1.0;
        for (int j = 0; j < 200; j++) {
            Cumulative_P = Cumulative_P - histogram[j].getCount() / numWindValues;
            if (Cumulative_P < 0.0) {
                break;
            }
            histogram[j].setCumProbability(Cumulative_P);
        }
        double Num = 0.0;
        double Den = 0.0;
        for (int j = 0; j < 200; j++) {
            if (histogram[j].getCumProbability() <= 0.01) {
                break;
            }
            Num = Num - Math.log(histogram[j].getCumProbability());
            Den = Den + histogram[j+1].getInterval();
        }
        double K = Num/Den;


        File fout = new File("cumProbability.txt");
        FileOutputStream fos = new FileOutputStream(fout);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));
        bw.write("Interval size," + userDefinedInterval);
        bw.newLine();
        bw.write("K, " + K);
        bw.newLine();
        for(int j = 0; j < 200; j++){
            bw.write(j + "," + histogram[j].getCumProbability());
            bw.newLine();
        }
        bw.close();

        String input;
        Scanner inputScan = new Scanner(System.in);

        do{
            System.out.println("Enter 'less' or 'greaterEq' if you would like to compute a probability, or 'q' to quit:");
            input = inputScan.nextLine();

            if(input.equals("less") || input.equals("greaterEq")){
                while(true){
                    System.out.println("Enter wind speed: ");
                    String numberString = inputScan.nextLine();

                    try{
                        double windSpeed = Double.parseDouble(numberString);

                        if (input.equals("less")){
                            double prob = 1.0 - Math.exp(-K * (Math.pow(windSpeed, 2)));
                            System.out.println("Probability of wind speed < " + windSpeed + " is " + prob);
                        } else if (input.equals("greaterEq")) {
                            double prob = Math.exp(-K * (Math.pow(windSpeed, 2)));
                            System.out.println("Probability of wind speed >= " + windSpeed + " is " + prob);
                        }
                        break;
                    } catch(NumberFormatException e){
                        System.out.println("Invalid input. Please enter a valid number.");
                    }
                }
            } else if (!input.equals("q")){
                System.out.println("Invalid input. Enter 'less', 'greaterEq', or 'q' to quit:");
            }
        }
        while(!input.equals("q"));
    }
}
