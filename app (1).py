#Comunicación TTL - Proyecto 2
#Programacion de microcontroladores
#--------------------------------------

#Angel Quiñonez - 20252
#Alexander Calí - 20765

#--------------------------------------

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

import serial

class App(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("Proyecto02.ui", self)			#Nombre del archivo a utilizar  "Proyecto02"

		#--IMPORTANTE-- tomar en cuaenta el puerto a utilizar, en este caso el puerto COM6
		self.ser = serial.Serial(port="COM6", baudrate = 9600, timeout = 1.0)
		self.ser.close()

		self.servo1.sliderReleased.connect( self.get_value_servo1 )
		self.servo2.sliderReleased.connect( self.get_value_servo2 )
		self.servo3.sliderReleased.connect( self.get_value_servo3 )
		self.servo4.sliderReleased.connect( self.get_value_servo4 )

#____________________________________________________________________________________________
#------------------Servo 1-------------------------------------------------------------------
	def get_value_servo1(self):
		value1 = self.servo1.value()
		valor1 = (value1 & 252)
		print(chr(valor1))
		self.ser.open()									# Abrir el puerto serial
		self.ser.write( chr(int(valor1)).encode() )		# Envió el valor del Slider 1
															# de modo que sea un caracter
		self.ser.close()								# Cerramos el puerto serial
		self.lbl_servo1.setText(str( value1 ))			# Mostrar el valor del Qslider1 en una etiqueta

#____________________________________________________________________________________________
#------------------Servo 2-------------------------------------------------------------------
	def get_value_servo2(self):
		value2 = self.servo2.value()
		valor2 = ((value2 | 1)& 253)
		print(chr(valor2))
		self.ser.open()									# Abrir el puerto serial
		self.ser.write( chr(int(valor2)).encode() )		# Envió el valor del Slider 2
															# de modo que sea un caracter
		self.ser.close() 								# Cerramos el puerto serial
		self.lbl_servo2.setText(str( value2 ))			# Mostrar el valor del Qslider2 en una etiqueta


#____________________________________________________________________________________________
#------------------Servo 3-------------------------------------------------------------------
	def get_value_servo3(self):
		value3 = self.servo3.value()
		valor3 = ((value3 | 2)& 254)
		print(chr(valor3))
		self.ser.open()									# Abrir el puerto serial
		self.ser.write( chr(int(valor3)).encode() )		# Envió el valor del Slider 3
															# de modo que sea un caracter
		self.ser.close()								# Cerramos el puerto serial
		self.lbl_servo3.setText(str( value3 ))			# Mostrar el valor del Qslider3 en una etiqueta


#____________________________________________________________________________________________
#------------------Servo 4-------------------------------------------------------------------
	def get_value_servo4(self):
		value4 = self.servo4.value()
		valor4 = (value4 | 3)
		print(chr(valor4))
		self.ser.open()									# Abrir el puerto serial
		self.ser.write( chr(int(valor4)).encode() )		# Envió el valor del Slider 4
															# de modo que sea un caracter
		self.ser.close()								# Cerramos el puerto serial
		self.lbl_servo4.setText(str( value4 ))			# Mostrar el valor del Qslider4 en una etiqueta




if __name__ == '__main__':
	app = QApplication(sys.argv)
	GUI = App()
	GUI.show()
	sys.exit(app.exec_())
