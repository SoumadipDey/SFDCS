# GUI FILE
from spinachClassifierMainUI import Ui_MainWindow
from detailsWindowUI import Ui_detailsWindow
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys

#Telling windows to let me make my own taskbar icons
import ctypes
myappid = 'nexusteam.SFDC.gui.version1' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#Libraries that do the heavy lifting
import numpy as np
import tensorflow as tf
from keras.models import load_model
import cv2
import pathlib
import json as json

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cureBtn.setDisabled(True)
        self.ui.detailsBtn.setDisabled(True)
         
        #Initializing some variables and iterables for future use
        self.classification = None
        self.databasePath = "database"
        self.selectedImagePath = None
        self.modelPath = "models\SFDNet_best_val_accuracy.h5"
        self.IMAGE_SIZE = (256,256)
        self.label_map_indexed = [
                    'anthracnose', 
                    'cercospora_leaf_spot',
                    'cladosporium_leaf_spot',
                    'downy_mildew',
                    'healthy' ,
                    'stemphylium_leaf_spot'
        ]

        # Connecting methods to Button clicks / Actions
        self.ui.browseBtn.clicked.connect(self.fileSelector)
        self.ui.predictBtn.clicked.connect(self.predictClass)
        self.ui.detailsBtn.clicked.connect(self.openDetails)
        
    

    def fileSelector(self) -> None:
        #Show File Dialouge Box
        fname = QFileDialog.getOpenFileName(None, 'Open file','c:\\', "Image files (*.jpg *.png)")
        #Take fname[0] value only if its a valid file
        if(len(fname[0]) > 0):
            imagePath = fname[0]
            self.selectedImagePath = imagePath
            pixmap = QPixmap(imagePath)
            self.ui.selectedImageLabel.setPixmap(QPixmap(pixmap))
            self.classification = None
        else:
            if(self.selectedImagePath):
                self.ui.selectedImageLabel.setPixmap(QPixmap(self.selectedImagePath))
            else:
                self.ui.selectedImageLabel.setPixmap(QPixmap(u"assets/spinach.png"))
    
    def predictClass(self) -> None:

        imgPath = self.selectedImagePath
        
        if(imgPath):
            if(pathlib.Path(imgPath).is_file()):
                #Resizing the image for input 
                img = cv2.imread(str(imgPath))
                resized_img = cv2.resize(img,self.IMAGE_SIZE)
                #Scaling and normalizing the image
                resized_img = resized_img/255
                #Loading the pre-trained model
                model = load_model(self.modelPath)

                #Calculating prediction and confidence
                predictions = model.predict(np.array([resized_img]),verbose = 0)
                pred_class = np.argmax(predictions)
                pred_class_name = self.label_map_indexed[pred_class]
                confidence = np.round(predictions[0][pred_class]*100,3)
                self.classification = pred_class_name
                self.updateWidgets(pred_class_name,confidence)
            else:
                print("Image does not exists or could not be fetched!")
        else:
            print("No image given!")

    def updateWidgets(self,pred_class_name : str,confidence : float):
        with open(f"{self.databasePath}/collection_basicinfo.json") as json_file:
            collection = json.load(json_file)
            field = collection[pred_class_name]
            if(pred_class_name != "healthy"):
                self.ui.cureBtn.setEnabled(True)
                self.ui.detailsBtn.setEnabled(True)
                self.ui.diseaseNameLabel.setText(str(field["name"]))
                self.ui.confidenceProgressBar.setValue(confidence)
                description = "Disease Description :\n" + field["description"]
                self.ui.descriptionLabel.setText(description)
                
            else:
                self.ui.diseaseNameLabel.setText(str(field["name"]))
                self.ui.confidenceProgressBar.setValue(confidence)
                description = "Description :\n" + field["description"]
                self.ui.descriptionLabel.setText(description)

    def openDetails(self):
        #Code to open the details screen here
        self.detailsWindow = QMainWindow()
        message = self.classification
        self.detail_ui = Ui_detailsWindow(message,self.databasePath)
        self.detail_ui.setupUi(self.detailsWindow)
        self.detailsWindow.show()
        

if __name__ == "__main__":
    # Prevent Tesnsorflow from printing info / warning
    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    print("Tensorflow: ",tf.__version__)
    sys.exit(app.exec_())