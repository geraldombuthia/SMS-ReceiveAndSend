import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

receiverNum = '+254xxxxxxxx'
sim800l = serial.Serial(
port='/dev/serial0',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)

sms = "Hello"
time.sleep(1)
sim800l.write(b'AT\r')
print(sim800l.read(24))
time.sleep(1)

sim800l.write(b'AT+CMGF=1\r')
print(sim800l.read(24))
time.sleep(1)
#cmd1 = b'AT+CMGS=\' '+str(receiverNum)+'\'\r'
sim800l.write(b'AT+CMGS="+254xxxxxxxxx"\r')
print(sim800l.read(24))

time.sleep(1)
sim800l.write(str.encode(sms+chr(26)))
#sim800l.write(chr(26))
print(sim800l.read(24))

