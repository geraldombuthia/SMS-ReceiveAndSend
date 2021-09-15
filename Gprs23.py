import RPi.GPIO as GPIO
import time
import serial

port = serial.Serial("/dev/serial0", baudrate=9600, timeout=1,
        parity = serial.PARITY_NONE,stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS
                     )

def senddata(data):
    port.write(b"AT+CPIN?\r\n")
    time.sleep(0.2)
    port.read(24)
    
    port.write(b"AT+CREG?\r\n")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+CGATT?\r\n")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+CIPSHUT\r\n")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+CIPSTATUS\r\n")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+CIPMUX=0\r\n")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+CSTT=\"network\", \"\", \"\"\r\n")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+CIICR\r\n")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+CIFSR\r\n")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+CIPSPRT=0\r\n")
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+CIPSTART=\"TCP\", \"api.thingspeak.com\", \"80\"\r\n")#Error occurs here
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+CIPSEND\r\n")#Error occurs here
    time.sleep(0.2)
    print(port.read(24))
    
    var = bytes(data)
    string = b"GET http://api.thingspeak.com/update?api_key=LHZNROJCOL8NAVGE&field1=" + var + b'\r\n' #Error occurs here
    port.write(string)
    time.sleep(0.2)
    print(port.read(50))
    
    port.write(bytes(chr(26), "utf-8"))
    time.sleep(0.2)
    print(port.read(24))
    
    port.write(b"AT+CIPSHUT\r\n")
    time.sleep(0.2)
    print(port.read(24))
    
    
senddata(str.encode(str(50)))