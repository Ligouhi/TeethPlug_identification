# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(569, 410)
        self.files = QtWidgets.QPushButton(Form)
        self.files.setGeometry(QtCore.QRect(370, 20, 93, 28))
        self.files.setObjectName("files")
        self.model = QtWidgets.QWidget(Form)
        self.model.setGeometry(QtCore.QRect(29, 69, 521, 321))
        self.model.setObjectName("model")
        self.fileText = QtWidgets.QLineEdit(Form)
        self.fileText.setGeometry(QtCore.QRect(50, 20, 311, 31))
        self.fileText.setObjectName("fileText")
        self.predict = QtWidgets.QPushButton(Form)
        self.predict.setGeometry(QtCore.QRect(470, 20, 93, 28))
        self.predict.setObjectName("predict")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.files.setText(_translate("Form", "选择文件"))
        self.predict.setText(_translate("Form", "识别"))
