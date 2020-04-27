"""Functions for the design tab."""

#PYQT
from PyQt5 import QtCore,QtGui

#CEToolkit
import CEToolkit

#Python
import os

def text_reader(file_path,text_edit):
    """Read the indicated .txt."""

    parent.ui.textEdit_design_image.clear()
    path = os.getcwd()+'\media\docs' + file_path
    f = open(path,'r');
    for x in f:
        text_edit.insertPlainText(x)

def initial_image(path_images):
        """Show the first image in the folder."""

        path = os.getcwd()+path_images
        dirs = os.listdir(path)
        path = os.getcwd()+path_images+dirs[0]
        parent.ui.label_design_image.setPixmap(QtGui.QPixmap(path))

def rnames_button():
    """Show design regular names."""

    parent.ui.label_design_image.setGeometry(QtCore.QRect(0, 0, 0, 0))
    CEToolkit.band_wraps_button = 0
    text_reader('\design/regular_names.txt',parent.ui.textEdit_design_image)

def pnames_button():
    """Show design production names."""
    
    parent.ui.label_design_image.setGeometry(QtCore.QRect(0, 0, 0, 0))
    parent.ui.label_design_image.setPixmap(QtGui.QPixmap(""))
    CEToolkit.band_wraps_button = 0
    text_reader('\design/production_names.txt',parent.ui.textEdit_design_image)

def parameters_button():
    """Show design parameters."""

    parent.ui.label_design_image.setGeometry(QtCore.QRect(450, 50, 550, 550))
    parent.ui.label_design_image.setPixmap(QtGui.QPixmap(""))
    CEToolkit.band_wraps_button = 0
    path_images = "/media/img/design/parameters/"
    initial_image(path_images)

def wraps_button():
    """Show wraps."""

    parent.ui.label_design_image.setGeometry(QtCore.QRect(450, 50, 550, 550))
    CEToolkit.contador_wraps = 0
    CEToolkit.band_wraps_button = 1
    path_images = "/media/img/design/wraps/"
    initial_image(path_images)

def folder_button():
    """Open database folder."""

    CEToolkit.band_wraps_button = 0
    parent.ui.textEdit_design_image.clear()
    parent.ui.label_design_image.setPixmap(QtGui.QPixmap(""))
    path = "./media/docs/design/4design"
    os.system(f'start {os.path.realpath(path)}')

def ceph_button():
    """Open ceph guide file"""

    CEToolkit.band_wraps_button = 0
    parent.ui.textEdit_design_image.clear()
    parent.ui.label_design_image.setPixmap(QtGui.QPixmap(""))
    path = "./media/docs/design/ceph_guide.xlsx"
    os.system(f'start {os.path.realpath(path)}')

def flags_button():
    """Show post-processign flags."""

    parent.ui.label_design_image.setGeometry(QtCore.QRect(450, 50, 550, 550))
    CEToolkit.band_wraps_button = 0
    path_images = "/media/img/design/flags/"
    initial_image(path_images)

def next():
    """Logic when user press Next button."""

    def next_image(path_file):
        path = os.getcwd()+path_file
        dirs = os.listdir(path)
        CEToolkit.contador_wraps += 1
        if CEToolkit.contador_wraps == len(dirs):
            CEToolkit.contador_wraps = 0
        path_image = path + dirs[CEToolkit.contador_wraps]
        parent.ui.label_design_image.setPixmap(QtGui.QPixmap(path_image))

    if CEToolkit.band_wraps_button == 1:
        path_file = "/media/img/design/wraps/"
        next_image(path_file)

def back():
    """Logic when user press back button."""

    def back_image(path_file):
        """Logic to show thw back image."""

        path = os.getcwd()+path_file
        dirs = os.listdir(path)
        CEToolkit.contador_wraps -= 1
        if CEToolkit.contador_wraps < 0:
            CEToolkit.contador_wraps = len(dirs) - 1
        path_image = path + dirs[CEToolkit.contador_wraps]
        parent.ui.label_design_image.setPixmap(QtGui.QPixmap(path_image))

    if CEToolkit.band_wraps_button == 1:
        path_file = "/media/img/design/wraps/"
        back_image(path_file)