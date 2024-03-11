from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setupUI()

    def setupUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.label = QLabel("0")
        self.label.setAlignment(QtCore.Qt.AlignRight)
        layout.addWidget(self.label)

        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        buttons = [
            ("C", "clear"),
            ("/", "divide"),
            ("*", "multiply"),
            ("7", "seven"),
            ("8", "eight"),
            ("9", "nine"),
            ("-", "minus"),
            ("4", "four"),
            ("5", "five"),
            ("6", "six"),
            ("+", "plus"),
            ("1", "one"),
            ("2", "two"),
            ("3", "three"),
            ("+/-", "plusminus"),
            ("0", "zero"),
            (".", "decimal"),
            ("=", "equal"),
        ]

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, (text, name) in zip(positions, buttons):
            if text == "":
                continue
            button = QPushButton(text)
            button.setObjectName(name)
            grid_layout.addWidget(button, *position)

        # Connect buttons to slots
        for button in central_widget.findChildren(QPushButton):
            button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == "C":
            self.label.setText("0")
        elif text == "=":
            expression = self.label.text()
            try:
                result = eval(expression)
                self.label.setText(str(result))
            except Exception as e:
                self.label.setText("Error")
        elif text == "+/-":
            if self.label.text().startswith("-"):
                self.label.setText(self.label.text()[1:])
            else:
                self.label.setText("-" + self.label.text())
        else:
            current_text = self.label.text()
            if current_text == "0":
                self.label.setText(text)
            else:
                self.label.setText(current_text + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CalculatorWindow()
    widget.show()
    sys.exit(app.exec_())
