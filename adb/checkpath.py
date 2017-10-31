# encoding: utf-8
"""
@author: lileilei
@file: checkpath.py
@time: 2017/10/31 9:14
"""
import  platform,subprocess,os,re
def getsystemsta():#获取系统的名称，使用对应的指令
    system=platform.system()
    if system=='Windows':
        find_manage='findstr'
    else:
        find_manage='grep'
    return  find_manage
def get_device_list():#获取设备列表
    devices = []
    result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    result.reverse()
    for line in result[1:]:
        if "attached" not in line.strip():
            devices.append(line.split()[0])
        else:
            break
    return devices


