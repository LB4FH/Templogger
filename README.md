# Templogger
Used for logging temperature / humidity with a DHT22 on a Raspberry Pi Zero W 

## Components
* Web: Contains a NodeJS application for running on the Pi Zero W. Refer to [Install NodeJS on a Raspberry Pi Zero W](https://hassancorrigan.com/blog/install-nodejs-on-a-raspberry-pi-zero/) for info about installing NodeJS.
* Datalogger: Contains a Python3 script for logging temperatures. Intended to be triggered via crontab or other similar tool
