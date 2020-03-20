"""Functions for the report tab"""

#PYQT
from PyQt5 import QtCore,QtGui

#CEToolkit
import CEToolkit

#Python
import os

def text_reader(file_path,text_edit):
    """read the indacated .txt"""

    parent.ui.textEdit_report_image.clear()
    path=os.getcwd()+'\media\docs' + file_path
    f = open(path,'r');
    for x in f:
        text_edit.insertPlainText(x)

def initial_image(path_images):
        """show the first image in the folder"""

        path = os.getcwd()+path_images
        dirs = os.listdir(path)
        path = os.getcwd()+path_images+dirs[0]
        parent.ui.label_report_image.setPixmap(QtGui.QPixmap(path))

def comments_button():
    """Show design regular names"""

    parent.ui.label_report_image.setGeometry(QtCore.QRect(0, 0, 0, 0))
    CEToolkit.contador_report = 0
    CEToolkit.band_teeth_button = 0
    parent.ui.label_report_image.setPixmap(QtGui.QPixmap(""))
    text_reader('/report/standard_comments.txt',parent.ui.textEdit_report_image)

def parameters_button():
    """Show report parameters."""
    
    parent.ui.label_report_image.setGeometry(QtCore.QRect(450, 50, 550, 550))
    CEToolkit.contador_report = 0
    CEToolkit.band_teeth_button = 0
    path_images = "/media/img/report/parameters/"
    initial_image(path_images)

def teeth_button():
    """show teeth numeration."""

    parent.ui.label_report_image.setGeometry(QtCore.QRect(450, 50, 550, 550))
    CEToolkit.band_teeth_button = 1
    path_images = "/media/img/report/teeth/"
    initial_image(path_images)

def colors_button():
    """show report colors."""

    parent.ui.label_report_image.setGeometry(QtCore.QRect(450, 50, 550, 550))
    CEToolkit.contador_report = 0
    CEToolkit.band_teeth_button = 0
    path_images = "/media/img/report/colors/"
    initial_image(path_images)

def next():
    """logic when user press  button"""

    def next_image(path_file):
        path = os.getcwd()+path_file
        dirs = os.listdir(path)
        CEToolkit.contador_report += 1
        if CEToolkit.contador_report == len(dirs):
            CEToolkit.contador_report = 0
        path_image = path + dirs[CEToolkit.contador_report]
        parent.ui.label_report_image.setPixmap(QtGui.QPixmap(path_image))

    if CEToolkit.band_teeth_button == 1:
        path_file = "/media/img/report/teeth/"
        next_image(path_file)

def back():
    """logic when user press back button"""

    def back_image(path_file):
        """logic to show the back image"""

        path = os.getcwd()+path_file
        dirs = os.listdir(path)
        CEToolkit.contador_report -= 1
        if CEToolkit.contador_report < 0:
            CEToolkit.contador_report = len(dirs) - 1
        path_image = path + dirs[CEToolkit.contador_report]
        parent.ui.label_report_image.setPixmap(QtGui.QPixmap(path_image))

    if CEToolkit.band_teeth_button == 1:
        path_file = "/media/img/report/teeth/"
        back_image(path_file)

