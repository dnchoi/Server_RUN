#!/bin/bash

sudo apt install -y python3-pip python-pip

sudo -H pip install -U jetson-stats
sudo -H pip3 install -U jetson-stats

sudo reboot

#jtop