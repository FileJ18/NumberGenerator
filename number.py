import sys
import random
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox
)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont


class NumberGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number Generator")
        self.showMaximized()  # start fullscreen

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Instruction label
        self.label = QLabel("Enter how many digits the number should have:")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont("Arial", 20))
        layout.addWidget(self.label)

        # Input box
        self.input = QLineEdit()
        self.input.setPlaceholderText("e.g. 3 for hundreds")
        self.input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input.setFont(QFont("Arial", 24))
        layout.addWidget(self.input)

        # Generate button
        self.button = QPushButton("Generate")
        self.button.setFont(QFont("Arial", 20))
        self.button.clicked.connect(self.start_timer)
        layout.addWidget(self.button)

        # Status label
        self.status = QLabel("Idle.")
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status.setFont(QFont("Arial", 18))
        layout.addWidget(self.status)

        self.setLayout(layout)

        # Timer for delayed generation
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.show_number)

    def start_timer(self):
        try:
            digits = int(self.input.text())
            if digits <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.critical(self, "Error", "Enter a valid positive integer.")
            return

        self.digits = digits
        self.status.setText(f"Generating a {digits}-digit number...")
        self.button.setEnabled(False)

        # delay 1 second just for effect
        self.timer.start(1000)

    def show_number(self):
        low = 10 ** (self.digits - 1)
        high = (10 ** self.digits) - 1
        number = random.randint(low, high)

        msg = QMessageBox(self)
        msg.setWindowTitle("Generated Number")
        msg.setText(f"Your {self.digits}-digit number:\n\n{number}")
        msg.setFont(QFont("Arial", 22))
        msg.exec()

        self.status.setText("Done.")
        self.button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumberGenerator()
    window.show()
    sys.exit(app.exec())
