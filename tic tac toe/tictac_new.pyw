from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QTabWidget, QApplication, QStatusBar
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys

class tictacui(QMainWindow):
	def __init__(self):
		super(tictacui, self).__init__()

		uic.loadUi('tictactoe.ui',self)

		self.setFixedSize(390, 521)  # Set the fixed size as per your requirement

		#Window stuff
		self.setWindowTitle('TicTacToe')
		self.setWindowIcon(QtGui.QIcon(r"C:\Python Code\fugue-icons-3.5.6\icons\tic-tac-toe.png"))

		#Buttons
		self.pushButton1 = self.findChild(QPushButton,'pushButton')
		self.pushButton2 = self.findChild(QPushButton,'pushButton_2')
		self.pushButton3 = self.findChild(QPushButton,'pushButton_3')
		self.pushButton4 = self.findChild(QPushButton,'pushButton_4')
		self.pushButton5 = self.findChild(QPushButton,'pushButton_5')
		self.pushButton6 = self.findChild(QPushButton,'pushButton_6')
		self.pushButton7 = self.findChild(QPushButton,'pushButton_7')
		self.pushButton8 = self.findChild(QPushButton,'pushButton_8')
		self.pushButton9 = self.findChild(QPushButton,'pushButton_9')
		self.resetButton = self.findChild(QPushButton,'resetButton')
		self.statusbar = self.findChild(QStatusBar,'statusbar')

		#Connecting buttons
		self.pushButton1.clicked.connect(lambda: self.changeText(1))
		self.pushButton2.clicked.connect(lambda: self.changeText(2))
		self.pushButton3.clicked.connect(lambda: self.changeText(3))
		self.pushButton4.clicked.connect(lambda: self.changeText(4))
		self.pushButton5.clicked.connect(lambda: self.changeText(5))
		self.pushButton6.clicked.connect(lambda: self.changeText(6))
		self.pushButton7.clicked.connect(lambda: self.changeText(7))
		self.pushButton8.clicked.connect(lambda: self.changeText(8))
		self.pushButton9.clicked.connect(lambda: self.changeText(9))
		self.resetButton.clicked.connect(self.reset)


		self.turn = 'x'
		self.statusbar.showMessage('X\'s turn')

		# #Set fixed size of grid so that it doesn't change
		# for i in range(1,10):
		# 	button = getattr(self, f'pushButton{i}')
		# 	button.setFixedSize(120,120)





	def changeText(self,id):
		button = getattr(self, f'pushButton{id}')
		if button.text() == '':
			button.setText(self.turn)
			button.setEnabled(False)
			win = self.checkWin()
			if win != True:
				if self.turn == 'x':
					self.turn = 'o'
					self.statusbar.showMessage('O\'s turn')
				else:
					self.turn = 'x'
					self.statusbar.showMessage('X\'s turn')


	def reset(self):
		for i in range(1,10):
			button = getattr(self, f'pushButton{i}')
			button.setText('')
			button.setEnabled(True)
		self.turn = 'x'
		self.statusbar.showMessage('X\'s turn')

	#Function to check if someone has won

	def checkWin(self):
		#Check rows
		if self.pushButton1.text() == self.pushButton2.text() == self.pushButton3.text() != '':
			self.disableButtons()
			self.statusbar.showMessage(f'{self.pushButton1.text().upper()} wins')
			return True
		if self.pushButton4.text() == self.pushButton5.text() == self.pushButton6.text() != '':
			print('True')
			self.disableButtons()
			self.statusbar.showMessage(f'{self.pushButton4.text().upper()} wins')
			return True
		if self.pushButton7.text() == self.pushButton8.text() == self.pushButton9.text() != '':
			self.disableButtons()
			self.statusbar.showMessage(f'{self.pushButton7.text().upper()} wins')
			return True

		#Check columns
		if self.pushButton1.text() == self.pushButton4.text() == self.pushButton7.text() != '':
			self.disableButtons()
			self.statusbar.showMessage(f'{self.pushButton1.text().upper()} wins')
			return True
		if self.pushButton2.text() == self.pushButton5.text() == self.pushButton8.text() != '':
			self.disableButtons()
			self.statusbar.showMessage(f'{self.pushButton2.text().upper()} wins')
			return True
		if self.pushButton3.text() == self.pushButton6.text() == self.pushButton9.text() != '':
			self.disableButtons()
			self.statusbar.showMessage(f'{self.pushButton3.text().upper()} wins')
			return True

		#Check diagonals
		if self.pushButton1.text() == self.pushButton5.text() == self.pushButton9.text() != '':
			self.disableButtons()
			self.statusbar.showMessage(f'{self.pushButton1.text().upper()} wins')
			return True
		if self.pushButton3.text() == self.pushButton5.text() == self.pushButton7.text() != '':
			self.disableButtons()
			self.statusbar.showMessage(f'{self.pushButton3.text().upper()} wins')
			return True

		#Check if all buttons are filled
		if all([button.text() != '' for button in [self.pushButton1,self.pushButton2,self.pushButton3,self.pushButton4,self.pushButton5,self.pushButton6,self.pushButton7,self.pushButton8,self.pushButton9]]):
			self.disableButtons()
			self.statusbar.showMessage('It\'s a tie')
			return True





	def disableButtons(self):
		for i in range(1,10):
			button = getattr(self, f'pushButton{i}')
			button.setEnabled(False)






app = QApplication(sys.argv)
UIWindow = tictacui()
UIWindow.show()
app.exec_()
