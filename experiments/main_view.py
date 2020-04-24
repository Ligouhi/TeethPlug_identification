import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from view import Ui_Form
import my_test
from my_test import p
from PyQt5.QtWidgets import QMessageBox
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MyFigure(FigureCanvas):
    def __init__(self,width=5, height=4):
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=100)

        #第二步：在父类中激活Figure窗口
        super(MyFigure,self).__init__(self.fig) #此句必不可少，否则不能显示图形
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.ax = self.fig.add_subplot(111)
    #第四步：就是画图，【可以在此类中画，也可以在其它类中画】


class Main_view(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Main_view, self).__init__(parent)
        self.setupUi(self)
        self.files.clicked.connect(self.getfile)
        self.fileText
        self.predict.clicked.connect(self.prefile)
        self.path = ""
        self.data = []
        # 画图
        self.F = MyFigure(width=3, height=2)
        self.gridlayout = QGridLayout(self.model)  # 继承容器groupBox
        self.gridlayout.addWidget(self.F, 0, 1)
        self.F.ax.remove()

    def plott(self):

        v = self.data.numpy()


        self.ax3d = self.F.fig.gca(projection='3d')

        self.Surf = self.ax3d.scatter(v[:, 0], v[:, 1], v[:, 2], cmap='r')
        print("画图")


        # ax.scatter(v[:, 0], v[:, 1], v[:, 2], s=1)
        # ax.set_xlabel('X')
        # ax.set_ylabel('Y')
        # ax.set_zlabel('Z')

        matplotlib.pyplot.show()
    def prefile(self):
        if self.path:
            res,self.data = p(self.path)
            # print("得到数据")
            my_test.plot(self.data)
            Main_view.plott(self)

            # print(res)
            if res == 1:
                QMessageBox.information(self, "结果", "存在嵌塞", QMessageBox.Yes)
            elif res == 0:
                QMessageBox.information(self, "结果", "无嵌塞", QMessageBox.Yes )
        else:
            QMessageBox.information(self, "无文件", "请选择文件", QMessageBox.Yes | QMessageBox.No)



    def getfile(self):

        # get_directory_path = QFileDialog.getExistingDirectory(self,
        #                                                       "选取指定文件夹",
        #                                                       "C:/")
        # self.filePathlineEdit.setText(str(get_directory_path))

        get_filename_path, ok = QFileDialog.getOpenFileName(self,
                                                            "选取单个文件",
                                                            "D:/github/dataset")

        if ok:
            self.fileText.setText(str(get_filename_path))
            self.path = str(get_filename_path)

        # get_filenames_path, ok = QFileDialog.getOpenFileNames(self,
        #                                                       "选取多个文件",
        #                                                       "C:/",
        #                                                       "All Files (*)")
        # if ok:
        #     self.filePathlineEdit.setText(str(' '.join(get_filenames_path)))

    # self.le.setPixmap(QPixmap(fname))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_view()
    ex.show()
    sys.exit(app.exec_())