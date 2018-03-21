import Adafruit_BMP.BMP085 as BMP085
s185 = BMP085.BMP085()
from mpu6050 import mpu6050
s6050 = mpu6050(0x68)
units = {0: 'x', 1: 'y', 2: 'z'}
f = open('OutputFile', 'w')
def fileWrite(info):
	info = ("{:.3f}".format(info))
	f.write(info)
	f.write(":")
def fileWriteArray(info):
	for i in range(0, 3):
		filWrite(info[units[i]])
def fileWriteNewLine(info):
	info = ("{0:3.3f}".format(info))
	f.write(info)
	f.write('\n')

while True:
	fileWriteArray(s6050.get_gyro_data())
	fileWriteArray(s6050.get_accel_data())
	fileWrite(s185.read_temperature())
	fileWrite(s185.read_pressure())
	fileWrite(s185.read_altitude())
	f.write('/n')