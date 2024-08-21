package com.example.cdfgraph;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.chart.CategoryAxis;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.scene.layout.StackPane;
import javafx.geometry.Insets;
import java.util.Scanner;

import java.io.File;
import java.io.IOException;
/**
 * <h1>CDF graph</h1>
 * The CDF program receives data from a file and graphs the OLS and cumulative probability lines.
 *
 * @author  Angela Lenling Lenli005
 * @version 1.0
 * @since   2023-12-14
 */

public class CDF extends Application {
    /**
     * This method is used obtain data from a file and create the stage for the graph.
     * @param stage This is the first parameter to start method
     * @exception IOException On input error.
     * @throws IOException On input error.
     * @see IOException
     */
    @Override
    public void start(Stage stage) throws IOException{
        //Defining the x an y axes
        NumberAxis xAxis = new NumberAxis();
        NumberAxis yAxis = new NumberAxis();
        //Setting labels for the axes
        xAxis.setLabel("Wind Speed Squared");
        yAxis.setLabel("Cumulative Probability");
        //Creating a line chart
        LineChart<Number, Number> linechart = new LineChart<Number, Number>(xAxis, yAxis);
        XYChart.Series series1 = new XYChart.Series();
        XYChart.Series series2 = new XYChart.Series();
//        String path = "C:" + File.separator + "Users" + File.separator + "angie" + File.separator +
//                "OneDrive" + File.separator + "Desktop" + File.separator + "CSCI2081" +
//                File.separator + "HW5" + File.separator + "src" + File.separator + "cumProbability.txt";
      File f = new File("cumProbability.txt");
//        File f = new File(path);
        Scanner s = new Scanner(f);
        double interval = 1;
        double K = 0.0;
        for(int i = 0; i < 201; i++) {
            String[] data = s.nextLine().split(",");
            if (i == 0) {
                interval = Double.parseDouble(data[1]);
            }
            if (i == 1){
                K = Double.parseDouble(data[1]);
            }else if (i > 0) {
                double xCoor = (Double.parseDouble(data[0]) * interval);
                series1.getData().add(new XYChart.Data(xCoor, Double.parseDouble(data[1])));
                double prob = Math.exp(-K * Math.pow((xCoor), 1));
                series2.getData().add(new XYChart.Data(xCoor, prob));

            }
        }




        series1.setName("Cumulative Probabilities per Interval");
        series2.setName("OLS");

        linechart.getData().addAll(series1, series2);
        StackPane pane = new StackPane(linechart);
        pane.setPadding(new Insets(15, 15, 15, 15));
        pane.setStyle("-fx-background-color: BEIGE");
        Scene scene = new Scene(pane, 595, 350);
        stage.setTitle("CDF");
        stage.setScene(scene);
        stage.show();
    }
    /**
     * This is the main method which makes use of launch method.
     * @param args Unused.
     */
    public static void main(String[] args) {
        launch();
    }
}