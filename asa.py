#!/usr/bin/python
from netmiko import ConnectHandler
import sys
import time
import select
import paramiko
import re

old_stdout = sys.stdout   
 
platform = 'cisco_asa'
username = 'cisco'
password = 'cisco123'
secret = 'cisco123'
host = '10.25.103.40'

device = ConnectHandler(device_type=platform, ip=host, username=username, password=password, secret=secret)
output = device.send_command('terminal length 0')
output = device.send_command('sh int ip brief')
print(output)
device.disconnect()

