# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------

# ====imports====
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)

import matplotlib.pyplot as plt

import numpy as np
import random
import re

import warnings
warnings.filterwarnings("ignore")

class main(QMainWindow):

    """class constructor initalize necessary elemnts
    
    Parameters
    ----------
    
    Returns
    -------
    
    """
    def __init__(self):

        # inintializing qt window
        QMainWindow.__init__(self)

        loadUi("gui.ui", self)

        self.setWindowTitle("Function Plotter")

        self.plot.clicked.connect(self.takeInput)

        self.toolbar = NavigationToolbar(self.MplWidget.canvas, self)

        self.toolbar.setStyleSheet("background-color:White;")

        self.setWindowIcon(QIcon('icon.ico'))

        self.addToolBar(self.toolbar)

        # inintializing vars
        self.min = 0
        self.max = 10
        pattern =  r"(?:[0-9-+*^/() ]|x|abs|sqrt|exp|ln|log|pi|e|(sin|cos|tan)h?)+"
        self.pat = re.compile(pattern)
        self.expression=""


    """taking user inputs and validates them
    
    Parameters
    ----------
    self
    
    Returns
    -------
    None
    
    """
    def takeInput(self):
        # reading min
        if self.notNumber(self.minInput.text()):
            self.errMsg("Please Enter the Minimum Value (Must be a Number)")
            return
        self.min = float(self.minInput.text())
        # reading max
        if self.notNumber(self.maxInput.text()):
            self.errMsg("Please Enter the Maximum Value (Must be a Number)")
            return
        self.max = float(self.maxInput.text())
        if self.min > self.max:
            self.errMsg("Min cannot be larger than Max")
            return
        # reading expression
        self.expression = self.functionInput.text().replace("^", "**")
        if re.fullmatch(self.pat, self.expression) == None:
             self.errMsg("Some thing is wrong with your expression please check it again!")
             return
        # lower case
        self.expression = self.expression.lower()
        self.update_graph()
        return


    """Graphing the function enterd by the user if it passed validation
    
    Parameters
    ----------
    self
    
    Returns
    -------
    None
    
    """
    def update_graph(self):
        x = np.arange(self.min, self.max, 0.1)
        # catch exceptions in case it passed our pattern by mistake
        try:
            y = eval(self.expression)
            # if linear create the Y array
            if not(isinstance(y,np.ndarray)):
                y = np.ones(x.size)*y
            # show any errors
        except SyntaxError as err:
            self.errMsg("Please Check Your Syntax")
            return None
        except NameError as err:
            self.errMsg(str(err)+", only variable 'x' is allowed")
            return None
        except:
            self.errMsg("Something Went Wrong Can't Evaluate Your Expression")
            return None      
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(x, y)
        self.MplWidget.canvas.axes.set_title("f(x) = "+self.functionInput.text())
        self.MplWidget.canvas.draw()
        return plt.plot(x, y)

    # ====validation====
    """validating user input number
    
    Parameters
    ----------
    self
    x : str
    Returns
    -------
    boolean
        True if numeric
        False if otherwise
    """

    def notNumber(self,x):
        try:
            a = float(x)
        except (TypeError, ValueError):
            return True
        else:
            return False

    """showing error messages
    
    Parameters
    ----------
    self
    msg : str
    Returns
    -------
    None
    
    """
    def errMsg(self, msg):
        msgBox = QMessageBox()
        msgBox.warning(self, "Error", msg)
        return

# ====math functions====

"""Math Functions
    
Parameters
----------
x : ndarray

Returns
-------
The corresponding right values
    
"""


def cos(x):
    return np.cos(x)


def sin(x):
    return np.sin(x)


def tan(x):
    return np.tan(x)


def cosh(x):
    return np.cosh(x)


def sinh(x):
    return np.sinh(x)


def tanh(x):
    return np.tanh(x)


def ln(x):
    return np.log(x)


def log(x):
    return np.log10(x)


def exp(x):
    return np.exp(x)


def sqrt(x):
    return np.sqrt(x)

# ====constants====

e = np.e
pi = np.pi

# ====main program====
app = QApplication([])
window = main()
window.show()
app.exec_()

