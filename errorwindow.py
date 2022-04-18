from PyQt5.QtWidgets import QMessageBox;
from PyQt5.QtGui import QFont;


class ErrorWindow(QMessageBox):

    xSize: int;
    ySize: int;
    font: str;
    fontSize: int;
    errMsg: str;

    def __init__(self, errType: str, font: str, fontSize: int):
        super().__init__();
        self.xSize = 100;
        self.ySize = 100;
        self.font = font;
        self.fontSize = fontSize;
        self.setFixedSize(self.xSize, self.ySize);
        self.setFont(QFont(font, fontSize));
        self.setWindowTitle("ERROR");

        if(errType == "falsevar"):
            self.errMsg = "Variable not used in function!";
            self.setText(self.errMsg);
        elif(errType == "falserange"):
            self.errMsg = "Invalid range!";
            self.setText(self.errMsg);
        elif(errType == "falseinc"):
            self.errMsg = "Invalid increment!";
            self.setText(self.errMsg);
        else:
            self.errMsg = "Invalid function!";
            self.setText(self.errMsg);
        
        self.show();