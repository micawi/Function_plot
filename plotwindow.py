import matplotlib.pyplot as plot;
from PyQt5.QtWidgets import QWidget;
from numpy import linspace;


class PlotWindow(QWidget):

    varStr: str;
    fnc: str;
    xValues: list;
    yValues: list;

    def __init__(self, var: str, fnc: str, min: int, max: int, inc: float):
        super().__init__();
        self.varStr = var;
        self.fnc = fnc;
        self.min = min;
        self.max = max;

        numValues: int = int((max - min)/inc);

        self.xValues = linspace(min, max, numValues);
        self.yValues = [];

        for x in self.xValues:
            currFnc: str = self.fnc.replace(self.varStr, str(x));
            currVal: float = eval(currFnc);
            self.yValues.append(currVal);
        
        plot.plot(self.xValues, self.yValues);
        plot.xlabel(self.varStr);
        plot.ylabel("Function value");
        plot.show();

        self.show();
                