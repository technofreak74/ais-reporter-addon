import getopt
import serial
import socket
import sys

try:
    opts, nots = getopt.getopt(sys.argv[1:], 'p:')
except getopt.GetoptError:
    print('UDPbroadcast.py -p <serial-port>')
    sys.exit(2)

# Default serial port
serialPort = '/dev/ttyUSB0'

for opt, arg in opts:
    if opt == "-p":
        serialPort = arg

try:
    ser = serial.Serial(serialPort, 38400)
except serial.SerialException:
    print('Failed to open serial port, check that it is connected and specified '
          'using the serial_port config option. Default is /dev/ttyUSB0')
    sys.exit(3)

print ('Using serial port: ' + serialPort, flush=True)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
  string = ser.readline()
  if string.startswith(b'!AIVDM'):
    sock.sendto(string, ("192.168.0.176",12650))
    sock.sendto(string, ("5.9.207.224",5928))
                                            
