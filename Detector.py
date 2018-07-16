#########################################################
#:Date: 2017/12/13
#:Version: 1
#:Authors:
#    - Elma Huang <huanghuei0206@gmail.com>
#    - LSC <sclee@g.ncu.edu.tw>
#:Python_Version: 2.7
#:Platform: Unix
#:Description:
#	This is a class which contains detect functions.
##########################################################


import socket
import subprocess
import FailureType
import time
import logging
import ConfigParser
from IPMIModule import IPMIManager


class Detector(object):
    def __init__(self, node, port):
        self.node = node.name
        self.ipmi_status = node.ipmi_status
        self.ipmi_manager = IPMIManager()
        self.port = port
        self.sock = None
        self.config = ConfigParser.RawConfigParser()
        self.config.read('/etc/hass.conf')
        self.max_message_size = int(self.config.get("default","max_message_size"))
        self.connect()

    def connect(self):
        # connect to FA
        try:
            print "[" + self.node + "] create socket connection"
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.setblocking(0)
            self.sock.settimeout(1)
            self.sock.connect((self.node, self.port))
        except Exception as e:
            logging.error("detector connect error %s" % str(e))
            print str(e)
            print "Init [" + self.node + "] connection failed"

    def checkNetworkStatus(self):
        heartbeat_time = int(self.config.get("default","heartbeat_time"))
        network_fail_time = 0
        while heartbeat_time > 0:
            try:
                response = subprocess.check_output(['timeout', '0.2', 'ping', '-c', '1', self.node],
                                                   stderr=subprocess.STDOUT, universal_newlines=True)
            except Exception as e:
                logging.error("network transient failure")
                network_fail_time += 1
                pass
            finally:
                time.sleep(1)
                heartbeat_time -= 1
        heartbeat_time = int(self.config.get("default","heartbeat_time"))
        if network_fail_time == heartbeat_time:
            return FailureType.NETWORK_FAIL
        return FailureType.HEALTH

    def checkServiceStatus(self):
        try:
            line = "polling request"
            self.sock.sendall(line)
            data, addr = self.sock.recvfrom(self.max_message_size)
            if data == "OK":
                return FailureType.HEALTH
            elif "error" in data:
                print data
                print "[" + self.node + "]service Failed"
            elif not data:
                print "[" + self.node + "]no ACK"
            else:
                print "[" + self.node + "]Receive:" + data
            return FailureType.SERVICE_FAIL
        except Exception as e:
            logging.error(str(e))
            fail_services = "agents"
            print "[" + self.node + "] connection failed"
            self.sock.connect((self.node, self.port))
            return FailureType.SERVICE_FAIL

    def checkPowerStatus(self):
        if not self.ipmi_status:
            return FailureType.HEALTH
        status = self.ipmi_manager.getPowerStatus(self.node)
        if status == "OK":
            return FailureType.HEALTH
        return FailureType.POWER_FAIL

    def checkOSStatus(self):
        if not self.ipmi_status:
            return FailureType.HEALTH
        status = self.ipmi_manager.getOSStatus(self.node)
        if status == "OK":
            return FailureType.HEALTH
        return FailureType.OS_FAIL

    def checkSensorStatus(self):
        if not self.ipmi_status:
            return FailureType.HEALTH
        status = self.ipmi_manager.getSensorStatus(self.node) 
        if status == "OK":
            return FailureType.HEALTH
        return FailureType.SENSOR_FAIL

    def getFailServices(self):
        try:
            line = "polling request"
            self.sock.sendall(line)
            data, addr = self.sock.recvfrom(self.max_message_size)
            if data != "OK":
                return data
        except Exception as e:
            return "agents"
