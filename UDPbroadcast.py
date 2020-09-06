import json
import serial
import socket
import sys

# Error checking around the existance and proper format of options.json is
# intentionally not implemented since the user will have no way to fix the
# issue (it is a developer issue). A python exception printed out in the log
# is the most useful thing for them to put in a bug report.
options_file = open('/data/options.json')
options = json.load(options_file);

serialPort = options['serial_port']
print('Using serial port: ' + serialPort, flush=True)

try:
    ser = serial.Serial(serialPort, 38400)
except serial.SerialException:
    print('Failed to open serial port, check that it is connected and specified '
          'using the serial_port config option. Default is /dev/ttyUSB0')
    sys.exit(3)

destinations = []
for dest in options['destinations']:
    destinations.append((dest['address'], dest['port']))

print('Destinations:')
for dest in destinations:
    print(*dest, sep=':', flush=True)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
    string = ser.readline()
    if string.startswith(b'!AIVDM'):
        for dest in destinations:
            sock.sendto(string, dest)
                                            
