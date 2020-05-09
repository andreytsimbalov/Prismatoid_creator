
from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys

#pyuic5 mainwindow.ui -o mainwindow.py
#pyuic5 untitled.ui -o untitled.py
#pyuic5 test_first_wind.ui -o test_first_wind.py

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def resizeEvent(self, event):
        x=self.size().width()
        y=self.size().height()

        self.ui.verticalLayoutWidget.resize(x-50,y-50)


def main():

    app = QtWidgets.QApplication([])
    application = mywindow()
    application.resize(800,850)
    application.show()
    application.ui.lineEdit.setText(str(application.ui.openGLWidget.textString))

    sys.exit(app.exec())

if __name__=="__main__":
    main()