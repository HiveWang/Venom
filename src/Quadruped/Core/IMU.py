import FaBo9Axis_MPU9250
import time
import math

Roll, Pitch, = 0,0
RAD_TO_DEG = 57.2957795
mpu9250 = FaBo9Axis_MPU9250.MPU9250()

def getYPR():
	
	global Roll,Pitch,mpu9250

	accel = mpu9250.readAccel()
	gyro = mpu9250.readGyro()

	start = time.time()

	acce_x = accel['x']
	acce_y = accel['y']	
	acce_z = accel['z']

	gyro_x = gyro['x']
	gyro_y = gyro['y']
	gyro_z = gyro['z']
		
	acce_roll = math.atan2(acce_y, acce_x) * RAD_TO_DEG
	acce_pitch = math.atan2(-acce_z, acce_y) * RAD_TO_DEG
	
	if Roll==0 and Pitch==0:
		Roll = acce_roll
		Pitch = acce_pitch
	
	end = time.time()

	dt = (end - start) 
	print("dt" ,dt)

	gyro_roll = (gyro_z/131) * dt
	gyro_pitch = (gyro_x/131) * dt
	
	Roll = 0.9934 * (Roll + gyro_roll) + 0.0066 * (acce_roll)     
	Pitch = 0.9934 * (Pitch + gyro_pitch) + 0.0066 * (acce_pitch) 
	Yaw = 0

	return Yaw,Pitch,Roll


if __name__=="__main__":
	while True:
		print(getYPR())
		time.sleep(0.1)