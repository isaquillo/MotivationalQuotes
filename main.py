
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from gui.ui_main_window import Ui_MainWindow
import quotes
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButtonGetQuote.clicked.connect(self.get_quote)

    

    def get_quote(self):
        # Getting quote and its author
        quote, author, message = quotes.getQuote()
        if quote != False:
            translated_quote, message = quotes.translate_quote(quote=quote)
            if translated_quote != False:
                english_quote = '"' + quote + '"\n- ' + author + ' -'
                spanish_quote = '"' + translated_quote + '"\n- ' + author + ' -'
                # Setting quotes on textEdit fields
                self.textEditEnglishQuote.setText(english_quote)
                self.textEditSpanishQuote.setText(spanish_quote)
            else:
                QMessageBox.warning(self, "Error", message)
        else:
            QMessageBox.warning(self, "Error", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())