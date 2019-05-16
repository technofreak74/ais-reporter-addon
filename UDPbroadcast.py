import serial
import socket

ser = serial.Serial('/dev/ttyUSB0', 38400)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
  string = ser.readline()
  if string.startswith(b'!AIVDM'):
    print (string)
    sock.sendto(string, ("192.168.0.176",12650))
    sock.sendto(string, ("5.9.207.224",5928))
                                            
