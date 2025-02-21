from PySide6.QtWidgets import QApplication, QMainWindow
from Frame.frm_main import Ui_frm_main


class Frm_main(QMainWindow, Ui_frm_main):
  def __init__(self):
    super().__init__()
    self.setupUi(self)


app = QApplication()
frm_main = Frm_main()
frm_main.show()
app.exec()