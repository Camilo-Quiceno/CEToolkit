"""Functions for the segmentation tab"""

#PYQT
from PyQt5 import QtCore,QtGui

#CEToolkit
import CEToolkit

#Python
import os

def text_reader(file_path,text_edit):
    """read the indacated .txt"""

    path=os.getcwd()+'\media\docs' + file_path
    f = open(path,'r');
    for x in f:
        text_edit.insertPlainText(x)

def initial_image(path_images):
    """show the first image in the folder"""
    path = os.getcwd()+path_images
    dirs = os.listdir(path)
    path = os.getcwd()+path_images+dirs[0]
    parent.ui.label_segmentation_image.setPixmap(QtGui.QPixmap(path))

def combobox_change():
    """reset the tab to names."""
    names_button()
    CEToolkit.contador_framework_orthognatic = 0

def names_button():
    """show the correct names, depend on the combo box."""

    parent.ui.label_segmentation_image.setGeometry(QtCore.QRect(0, 0, 0, 0))
    CEToolkit.contador_framework_orthognatic = 0
    CEToolkit.band_framework_button = 0
    parent.ui.label_segmentation_image.setPixmap(QtGui.QPixmap(""))
    parent.ui.textEdit_segmentation_image.clear()
    text_reader('\segmentation\stlnames.txt', parent.ui.textEdit_segmentation_image)
        
def framework_button():
    """show the correct framework images, depends on the combobox"""

    parent.ui.label_segmentation_image.setGeometry(QtCore.QRect(450, 50, 550, 550))
    CEToolkit.band_framework_button = 1
    parent.ui.textEdit_segmentation_image.setPlainText("")

    if parent.ui.comboBox_segmentation_surgery.currentIndex() == 0:
        path_images = "/media/img/segmentation/orthognatic/framework/"
        initial_image(path_images)

    if parent.ui.comboBox_segmentation_surgery.currentIndex() == 1:
        path_images = "/media/img/segmentation/grafts/framework/"
        initial_image(path_images)

    if parent.ui.comboBox_segmentation_surgery.currentIndex() == 2:
        path_images = "/media/img/segmentation/mandible_reconstruction/framework/"
        initial_image(path_images)
    
    if parent.ui.comboBox_segmentation_surgery.currentIndex() == 3:
        path_images = "/media/img/segmentation/midface_reconstruction/framework/"
        initial_image(path_images)
    
    if parent.ui.comboBox_segmentation_surgery.currentIndex() == 4:
        path_images = "/media/img/segmentation/psi/framework/"
        initial_image(path_images)
        
    if parent.ui.comboBox_segmentation_surgery.currentIndex() == 5:
        path_images = "/media/img/segmentation/craniofacial_distraction/framework/"
        initial_image(path_images)
    
    if parent.ui.comboBox_segmentation_surgery.currentIndex() == 6:
        path_images = "/media/img/segmentation/cranial_vault_reconstruction/framework/"
        initial_image(path_images)

    if parent.ui.comboBox_segmentation_surgery.currentIndex() == 7:
        path_images = "/media/img/segmentation/midface_aesthetic/framework/"
        initial_image(path_images)

def objects_button():
    """show object list."""

    parent.ui.label_segmentation_image.setGeometry(QtCore.QRect(0, 0, 0, 0))
    CEToolkit.contador_framework_orthognatic = 0
    CEToolkit.band_framework_button = 0
    parent.ui.textEdit_segmentation_image.clear()
    parent.ui.label_segmentation_image.setPixmap(QtGui.QPixmap(""))
    text_reader('\segmentation\objects_list.txt', parent.ui.textEdit_segmentation_image)

def preplanning_folder_button():
    """show preplanning folders."""

    parent.ui.label_segmentation_image.setGeometry(QtCore.QRect(0, 0, 0, 0))
    CEToolkit.contador_framework_orthognatic = 0
    CEToolkit.band_framework_button = 0
    parent.ui.label_segmentation_image.setPixmap(QtGui.QPixmap(""))
    parent.ui.textEdit_segmentation_image.clear()
    if parent.ui.comboBox_segmentation_surgery.currentIndex() == 0:
        text_reader('\segmentation\orthognatic\preplanning_folders.txt', parent.ui.textEdit_segmentation_image)
    else:
        text_reader('\segmentation\preplanning_folders.txt', parent.ui.textEdit_segmentation_image)

def preplanning_cuts_button():
    """show the correct framework images, depends on the combobox"""

    parent.ui.label_segmentation_image.setGeometry(QtCore.QRect(0, 0, 0, 0))
    CEToolkit.contador_framework_orthognatic = 0
    CEToolkit.band_framework_button = 0
    parent.ui.textEdit_segmentation_image.setPlainText("")

    if parent.ui.comboBox_segmentation_surgery.currentIndex() == 0:
        path_images = "/media/img/segmentation/orthognatic/preplanning/"
        initial_image(path_images)
    elif parent.ui.comboBox_segmentation_surgery.currentIndex() == 1 or parent.ui.comboBox_segmentation_surgery.currentIndex() == 2 or parent.ui.comboBox_segmentation_surgery.currentIndex() == 3:
        path_images = "/media/img/segmentation/mandible_reconstruction/preplanning/"
        initial_image(path_images)
    
def next():
    """logic when user press  button"""

    def next_image(path_file):
        path = os.getcwd()+path_file
        dirs = os.listdir(path)
        CEToolkit.contador_framework_orthognatic += 1
        if CEToolkit.contador_framework_orthognatic == len(dirs):
            CEToolkit.contador_framework_orthognatic = 0
        path_image = path + dirs[CEToolkit.contador_framework_orthognatic]
        parent.ui.label_segmentation_image.setPixmap(QtGui.QPixmap(path_image))

    if CEToolkit.band_framework_button == 1:
        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 0:
            path_file = "/media/img/segmentation/orthognatic/framework/"
            next_image(path_file)

        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 1:
            path_file = "/media/img/segmentation/grafts/framework/"
            next_image(path_file)
    
        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 2:
            path_file = "/media/img/segmentation/mandible_reconstruction/framework/"
            next_image(path_file)
        
        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 3:
            path_file = "/media/img/segmentation/midface_reconstruction/framework/"
            next_image(path_file)

        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 4:
            path_file = "/media/img/segmentation/psi/framework/"
            next_image(path_file)

        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 5:
            path_file = "/media/img/segmentation/craniofacial_distraction/framework/"
            next_image(path_file)

        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 6:
            path_file = "/media/img/segmentation/cranial_vault_reconstruction/framework/"
            next_image(path_file)

        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 7:
            path_file = "/media/img/segmentation/midface_aesthetic/framework/"
            next_image(path_file)

def back():
    """logic when user press back button"""

    def back_image(path_file):
        """logic to shor thw back image"""
        path = os.getcwd()+path_file
        dirs = os.listdir(path)
        CEToolkit.contador_framework_orthognatic -= 1
        if CEToolkit.contador_framework_orthognatic < 0:
            CEToolkit.contador_framework_orthognatic = len(dirs) - 1
        path_image = path + dirs[CEToolkit.contador_framework_orthognatic]
        parent.ui.label_segmentation_image.setPixmap(QtGui.QPixmap(path_image))

    if CEToolkit.band_framework_button == 1:
        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 0:
            path_file="/media/img/segmentation/orthognatic/framework/"
            back_image(path_file)

        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 1:
            path_file="/media/img/segmentation/grafts/framework/"
            back_image(path_file)

        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 2:
            path_file="/media/img/segmentation/mandible_reconstruction/framework/"
            back_image(path_file)

        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 3:
            path_file="/media/img/segmentation/midface_reconstruction/framework/"
            back_image(path_file)
          
        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 4:
            path_file = "/media/img/segmentation/psi/framework/"
            back_image(path_file)

        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 5:
            path_file = "/media/img/segmentation/craniofacial_distraction/framework/"
            back_image(path_file)

        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 6:
            path_file = "/media/img/segmentation/cranial_vault_reconstruction/framework/"
            back_image(path_file)

        if parent.ui.comboBox_segmentation_surgery.currentIndex() == 7:
            path_file = "/media/img/segmentation/midface_aesthetic/framework/"
            back_image(path_file)