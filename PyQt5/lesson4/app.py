import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()

    b = QtWidgets.QPushButton(w)
    l = QtWidgets.QLabel(w)

    h_box = QtWidgets.QHBoxLayout()
    v_box = QtWidgets.QVBoxLayout()

    b.setText("Push Me")
    l.setText("Look at me")
    w.setWindowTitle("PyQt5")

    h_box.addStretch()
    h_box.addWidget(l)
    h_box.addStretch()

    v_box.addWidget(b)
    v_box.addWidget(l)
    v_box.addLayout(h_box)
    w.setLayout(v_box)


    w.show()
    sys.exit(app.exec_())

window()
