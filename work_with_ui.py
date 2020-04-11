
from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys

#pyuic5 mainwindow.ui -o mainwindow.py

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def resizeEvent(self, event):
        #print(event)
        x=self.size().width()
        y=self.size().height()

        self.ui.horizontalLayoutWidget.resize(x-100,y-100)

class GtOGLW(QtWidgets.QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

app = QtWidgets.QApplication([])
application = mywindow()
#application.ui.horizontalLayoutWidget.resize(600,600)
application.resize(700,700)
application.show()

sys.exit(app.exec())