from PyQt5.QtWidgets import QGridLayout, QPushButton, QLineEdit, QLabel, QComboBox;
from PyQt5.QtGui import QFont;
from PyQt5.QtWidgets import QApplication, QWidget;

appVersion: str = "v1.0";

class MainWindow(QWidget):

    xSize: int;
    ySize: int;
    grid: QGridLayout;
    varLabel: QLabel;
    varSelect: QComboBox;
    functionLabel: QLabel;
    functionLine: QLineEdit;
    rangeLabel1: QLabel;
    rangeLabel2: QLabel;
    rangeLine1: QLineEdit;
    rangeLine2: QLineEdit;
    plotButton: QPushButton;
    
    def __init__(self, app: QApplication):
        super().__init__();
        self.xSize = 350;
        self.ySize = 350;
        self.setWindowTitle("Function plotter " + appVersion);
        self.setFixedSize(self.xSize, self.ySize);
        self.setFont(QFont("Times", 10));

        self.grid = QGridLayout(self);

        self.varLabel = QLabel();
        self.varLabel.setText("Select variable to use: ");
        self.grid.addWidget(self.varLabel);

        self.varSelect = QComboBox();
        self.varSelect.addItem("x");
        self.varSelect.addItem("y");
        self.varSelect.addItem("z");
        self.varSelect.addItem("t");
        self.grid.addWidget(self.varSelect, 0, 1);

        self.functionLabel = QLabel();
        self.functionLabel.setText("Enter function: ");
        self.grid.addWidget(self.functionLabel, 1, 0);

        self.functionLine = QLineEdit();
        self.functionLine.setPlaceholderText("Enter function here...");
        self.grid.addWidget(self.functionLine, 1, 1, 1, 3);

        self.rangeLabel1 = QLabel();
        self.rangeLabel1.setText("Plot in range: ");
        self.grid.addWidget(self.rangeLabel1, 2, 0);

        self.rangeLine1 = QLineEdit();
        self.rangeLine1.setPlaceholderText("min");
        self.grid.addWidget(self.rangeLine1, 2, 1);

        self.rangeLabel2 = QLabel();
        self.rangeLabel2.setText(" - ");
        self.grid.addWidget(self.rangeLabel2, 2, 2);

        self.rangeLine2 = QLineEdit();
        self.rangeLine2.setPlaceholderText("max");
        self.grid.addWidget(self.rangeLine2, 2, 3);

        self.plotButton = QPushButton("PLOT FUNCTION");
        self.grid.addWidget(self.plotButton, 3, 0, 1, 4);

        self.show();
