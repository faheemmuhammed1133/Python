# hello.py

''''"""Simple Hello, World example with PyQt6."""

import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
app = QApplication([])

# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle("pushApp")
window.setGeometry(600, 200, 580, 580)
helloMsg = QLabel("<h1><\n>FOOTBALL!<\n></h1>", parent=window)
helloMsg.move(200, 300)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())

# python3 1.py to run'''

# f_layout.py

"""Form layout example."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QWidget,
)


app = QApplication([])
window = QWidget()
window.setWindowTitle("QFormLayout")
window.setGeometry(10,10,500,500)

layout = QFormLayout()
layout.name=QLineEdit("piyush")
layout.addRow("Name:", layout.name.text())
layout.addRow("Age:", QLineEdit())
layout.addRow("Job:", QLineEdit())
layout.addRow("Hobbies:", QLineEdit())
window.setLayout(layout)

window.show()
sys.exit(app.exec())
# file read and write
