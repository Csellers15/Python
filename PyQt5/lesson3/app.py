import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()

    b = QtWidgets.QPushButton(w)
    l = QtWidgets.QLabel(w)

    b.setText("Push Me")
    l.setText("Look at me")
    w.setWindowTitle("PyQt5")

    b.move(100, 50)
    l.move(110,100)
    w.setGeometry(100, 100, 300, 200)

    w.show()
    sys.exit(app.exec_())

window()
