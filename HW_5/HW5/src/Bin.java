/**
 * <h1>Bin</h1>
 * The Bin program contains a constructor for a bin that holds interval data, counts, and cumulative probabilities.
 * It also contains methods to manipulate and obtain this data.
 *
 *
 * @author  Angela Lenling Lenli005
 * @version 1.0
 * @since   2023-12-14
 */

public class Bin {
    double interval;
    int count;
    double cumProbability;
    /**
     * This method is used to create a Bin object.
     *
     *
     * @param interval This is the first parameter to Bin method
     * @param count  This is the second parameter to Bin method
     * @param cumProbability This is the third parameter to Bin method
     */
    public Bin(double interval, int count, double cumProbability){
        this.interval = interval;
        this.count = count;
        this.cumProbability = cumProbability;
    }
    /**
     * This method is used to get the interval from the bin object.
     * @return double This returns the interval.
     */
    public double getInterval(){return interval;}
    /**
     * This method is used to get the count from the bin object.
     * @return double This returns the count.
     */
    public int getCount(){return count;}
    /**
     * This method is used to get the cumulative probability from the bin object.
     * @return double This returns the cumProbability.
     */
    public double getCumProbability() {return cumProbability;}
    /**
     * This method is used to set the count for each bin object.
     * @param count This is the first parameter to setCount method
     */
    public void setCount(int count) {this.count = count;}
    /**
     * This method is used to set the cumulative probability for each bin object.
     * @param cumProbability This is the first parameter to setCumProbability method
     */
    public void setCumProbability(double cumProbability) {this.cumProbability = cumProbability;}
}
