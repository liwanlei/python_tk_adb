# -*- coding: utf-8 -*-
# @Date    : 2017-06-12
# @Author  : lileilei 
import os,time,platform,time
from adb.checkpath import getsystemsta
from ulit.log import logger,LOG
find=getsystemsta()
@logger('获取启动耗时')
def starttime_app(packagename,packagenameactivicy):#启动耗时
	cmd='adb shell am start -W -n %s'%packagenameactivicy
	me=os.popen(cmd).read().split('\n')[-7].split(':')#获取启动时间
	cmd2='adb shell am force-stop %s'%packagename
	os.system(cmd2)
	return me
@logger('获取流量')
def liulang(packagename):
	cmd='adb shell ps  | %s %s'%(find,packagename)
	cm=os.popen(cmd).read().split()[1]
	cmd1="adb shell cat /proc/"+cm+"/net/dev | findstr wlan0"
	liul = os.popen(cmd1).read().split()
	me1_shou=liul[1]#接受
	me2_shou=liul[9]#上传
	time.sleep(2)
	cmd2="adb shell cat /proc/"+cm+"/net/dev | findstr wlan0"
	liul1 = os.popen(cmd2).read().split()
	me1_xia=liul1[1]#接受
	me2_xia=liul1[9]#上传
	me1=int(int(me1_xia)-int(me1_shou))/1024
	me2=int(int(me2_xia)-int(me2_shou))/1024
	liulang_sum=me1+me2
	return me1 ,me2,liulang_sum
@logger('获取cpu信息')
def caijicpu(packagename):#这里采集的cpu时候可以是执行操作采集 就是-n  -d  刷新间隔
	cpu='adb shell top -n 1| %s %s'%(find,packagename)
	re_cpu=os.popen(cpu).read().split()[2]
	return re_cpu
@logger('获取内存')
def getnencun(packagename):#Total 的实际使用过物理内存
	cpu = 'adb shell top -n 1| %s %s' % (find, packagename)
	re_cpu=int(os.popen(cpu).read().split()[8][:-1])/1024
	return re_cpu
@logger('执行monkey测试')
def adb_monkey(packagename,s_num,throttle,pct_touch,pct_motion,pct_trackball,pct_nav,pct_syskeys,pct_appswitch,num,logfilepath):
	cmden='adb shell monkey -p %s -s %s --throttle %s --pct-touch %s --pct-motion %s  --pct-trackball  %s  --pct-trackball %s  --pct-syskeys  %s  --pct-appswitch  %s   -v -v -v %s >%s'%(packagename,s_num,throttle,pct_touch,pct_motion,pct_trackball,pct_nav,pct_syskeys,pct_appswitch,num,logfilepath)
	os.popen(cmden)
@logger('获取设备状态')
def huoqushebeizhuangtai():#获取设备状态
	cmd1='adb get-state'
	devices_status=os.popen(cmd1).read().split()[0]
	return devices_status
