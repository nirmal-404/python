import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(2800,300,500,500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6FDCf7;"
                            "font-weight:bold;"
                            "font-style: italic;"
                            "text-decoration: underline")

        # label.setAlignment(Qt.AlignTop)  # Vertically top
        # label.setAlignment(Qt.AlignBottom)  # Vertically bottom
        # label.setAlignment(Qt.AlignVCenter)  # Vertically center
        #
        # label.setAlignment(Qt.AlignRight)  # Horizontally right
        # label.setAlignment(Qt.AlignHCenter)  # Horizontally center
        # label.setAlignment(Qt.AlignLeft)  # Horizontally left

        # label.setAlignment(Qt.AlignCenter | Qt.AlignTop)   # center and top
        label.setAlignment(Qt.AlignCenter | Qt.AlignBottom)   # center and bottom
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)   # center and center
        label.setAlignment(Qt.AlignCenter)   # center and center




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()