#!/usr/bin/with-contenv bashio
CONFIG_PATH=/data/options.json

SERIAL_PORT="$(bashio::config 'serial_port')"

echo AIS Reporter Starting...

python3 UDPbroadcast.py -p $SERIAL_PORT

