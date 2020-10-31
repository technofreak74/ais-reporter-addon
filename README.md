# Ais Reporter Addon

A custom addon for [home assistant](https://www.home-assistant.io/) that reads data from a serial port and rebroadcasts it over UDP. It was written to provide a convenient way to provide data to an AIS aggregator like [Marine Traffic](https://marinetraffic.com) from a locally connected AIS receiver.

## Example Setup

USB serial adapter connected to AIS Receiver. Check to see what device name it gets enumerated as by opening Supervisor -> System -> Host System -> ... -> Hardware. The popup lists lots of information about the system that homeassistant is running on. At the top there should be a "Serial:" section containing entries like "/dev/ttyUSB0" or "/dev/ttyACM0". You may have multiple if you have other USB serial devices (such as Zigbee/Z-Wave sticks). 
