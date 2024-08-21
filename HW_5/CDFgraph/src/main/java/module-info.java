module com.example.cdfgraph {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;

    opens com.example.cdfgraph to javafx.fxml;
    exports com.example.cdfgraph;
}