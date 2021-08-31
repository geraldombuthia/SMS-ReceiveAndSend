import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


class SendSms():
    def __init__(self, receiverNum, sms):
        sim800l = serial.Serial(
            port = "/dev/tty1",
            baudrate = 9600,
            timeout=1
        )
        time.sleep(1)
        sim800l.write(b'AT\r')
        print(sim800l.read(24))
        time.sleep(1)

        sim800l.write(b'AT+CMGF=1\r')
        print(sim800l.read(24))
        time.sleep(1)
        sim800l.write(b'AT+CMGS=' + bytes(str(receiverNum), "utf-8") + b'\r')
        print(sim800l.read(24))
        time.sleep(1)
        sim800l.write(str.encode(sms+chr(26)))
        print(sim800l.read(24))
        
        
SendSms(+254728127853, "Hello")
#add a + to AT+CMGS since converting phone number to string gets rid of + as it indicates a numeral