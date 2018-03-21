import time
from multithreading import threadpool as pool
import Adafruit_BMP.BMP085 as BMP085
from mpu6050 import mpu6050

s185 = BMP085.BMP085()
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
startTime = time.time()
while True:
	filWrite(time.time()-startTime)
	fileWriteArray(s6050.get_gyro_data())
	fileWriteArray(s6050.get_accel_data())
	fileWrite(s185.read_temperature())
	fileWrite(s185.read_pressure())
	fileWrite(s185.read_altitude())
	f.write('/n')
	
	
def main():
	p = pool(20)
	q = queue()
	p.apply(readGPS, q)
	p.apply(readI2c, q)
	
	while true:
		data = new [] ''' check new object syntax'''
		for range(0, 500):
			currData = makeCurrData()
			data.append(currData)
			
		p.apply(dataToFile, data)	
		
		
	
if __name__ is "__main__":
	main()