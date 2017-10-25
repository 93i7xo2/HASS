#!/usr/bin/python
# -*- coding: utf-8 -*-

BASE_CMD = "ipmitool -I lanplus -H %s -U %s -P %s " # %(NODEID , USER , PASSWD)

REBOOTNODE = "chassis power reset"
REBOOTNODE_SUCCESS_MSG = "Reset"

STARTNODE = "chassis power on"
STARTNODE_SUCCESS_MSG = "Up/On"

SHUTOFFNODE = "chassis power off"
SHUTOFFNODE_SUCCESS_MSG = "Down/Off"

NODEINFO = "sdr elist full -v -c sensor reading"
NODEINFO_BY_TYPE = "sensor get '%s'"
HP_NODE_CPU_SENSOR_INFO = "sensor get '%s' " % "02-CPU 1"
DELL_NODE_CPU_SENSOR_INFO = "sensor get '%s' " % "Temp"

GET_OS_STATUS = "mc watchdog get"

WATCHDOG_THRESHOLD = 4

SENSOR_STATUS = "sdr elist full -v -c sensor reading"

RESET_WATCHDOG = "mc watchdog reset"
RESET_WATCHDOG_SUCCESS_MSG = "countdown restarted"

POWER_STATUS = "power status"
POWER_STATUS_SUCCESS_MSG = "Power is on"

RAW_DATA = "sdr get %s"