#!/usr/bin/with-contenv bashio
CONFIG_PATH=/data/options.json

SERIAL_PORT="$(bashio::config 'serial_port')"

echo AIS Reporter Starting...
echo Using serial port: $SERIAL_PORT

python3 UDPbroadcast.py

