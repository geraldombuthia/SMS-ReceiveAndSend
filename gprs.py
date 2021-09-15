import serial
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#use dmesg | grep tty to check active port 
#however with serial communication with sudo raspi-config set to on, active port to use is /dev/serial0
# Enable Serial Communication
port = serial.Serial("/dev/serial0", baudrate=9600, timeout=1,
        parity = serial.PARITY_NONE,stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS
                     )
 
def send_data(url, data):
    port.write(b'AT\r\n')
    time.sleep(0.2)
    #print(len(data))
    
    port.write(b"AT+SAPBR=3,1,\"Contype\",\"GPRS\"")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+SAPBR=3,1,\"APN\",\"network\"")  # APN
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+SAPBR=1,1")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+SAPBR=2,1")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+HTTPINIT")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+HTTPPARA=\"CID\",1")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+HTTPPARA=\"URL\",\""+ bytes(url, "utf-8") + b"\""); #Server address
    time.sleep(0.2)
    print(port.read(24))

    port.write(b"AT+HTTPPARA=\"CONTENT\",\"application/json\"")
    time.sleep(0.2)
    print(port.read(24))
    
    var = bytes(str(len(data)), "utf-8")
    port.write(b"AT+HTTPDATA=" + var + b",100000")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(data)
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+HTTPACTION=1")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+HTTPREAD")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+HTTPTERM")
    time.sleep(0.2)
    print(port.read(24))
    
#encoding = "utf-8"
#GET removed from the url below to test how it works
send_data("https://api.thingspeak.com/update?api_key=5BN7WKZ260HOJMM6&field1=", str(50))
