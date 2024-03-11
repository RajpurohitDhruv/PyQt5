import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit, QApplication
from PyQt5.QtCore import QSize

class ClipBoardDemo(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(440,240))
        self.setWindowTitle("ClipBoard App Demo")

        self.textarea = QPlainTextEdit(self)
        self.textarea.setPlainText("You can perform editing here")
        self.textarea.move(10,10)
        self.textarea.resize(400,200)

        QApplication.clipboard().dataChanged.connect(self.textChanged)

    def textChanged(self):
        text = QApplication.clipboard().text()
        print(text)
        self.textarea.insertPlainText(text + "\n")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    widget = ClipBoardDemo()
    widget.show()
    sys.exit(app.exec_())
