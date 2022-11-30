# Importing libraries
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class QScrollLabel(QScrollArea):
	"""
	A Custom Scrollable QLabel Implementation
	"""
	def __init__(self, parent = None) -> None:
		QScrollArea.__init__(self, parent)
		self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		# Creating label
		self.label = QLabel(self)
		font1 = QFont()
		font1.setFamily(u"Product Sans Medium")
		font1.setPointSize(10)
		font1.setWeight(50)
		self.label.setFont(font1)
		
		self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
		self.label.setWordWrap(True)
		
		self.labelSizePolicy = QSizePolicy(
			QSizePolicy.Fixed, 
			QSizePolicy.MinimumExpanding
		)
		
		self.labelSizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(self.labelSizePolicy)
		self.label.setMinimumSize(QSize(345, 80))
		self.label.setMaximumSize(QSize(345, 1500))
		
		self.label.setText("NULL")

		# Making the internal QLabel
		self.setWidget(self.label)
		
		
	# Defining the setText method
	def setText(self, text : str) -> None:
		self.label.setText(text)
	