# -*- coding: utf-8 -*-
# @Date    : 2017-06-12
# @Author  : lileilei 
import os,time,platform,time
def starttime_app(packagename,packagenameactivicy):#启动耗时
	cmd='adb shell am start -W -n %s'%packagenameactivicy
	me=os.popen(cmd).read().split('\n')[-7].split(':')#获取启动时间
	cmd2='adb shell am force-stop %s'%packagename
	os.system(cmd2)
	return me
def makesure_system():
	if platform.system =='Windows':
		find='findstr'
	else:
		find='grep'
def liulang(packagename):
	cmd='adb shell cat /data/system/packages.list | findstr %s'%packagename
	cm=os.popen(cmd).read().split()[1]
	cmd1='adb shell cat /proc/net/xt_qtaguid/stats | findstr %s'%cm
	me1_shou=os.popen(cmd1).read().split()[5]#接受
	me2_shou=os.popen(cmd1).read().split()[7]#上传
	cmd2='adb shell cat /proc/net/xt_qtaguid/stats | findstr %s'%cm
	me1_xia=os.popen(cmd1).read().split()[5]#接受
	me2_xia=os.popen(cmd1).read().split()[7]#上传
	liulang_sum_1=(int(me1_shou)+int(me2_shou))#过程产生流量计算为执行后的流量-执行前的流量，
	liulang_sum_xia=(int(me1_xia)+int(me2_xia))
	liulang_sum=int(liulang_sum_xia)-int(liulang_sum_1)
	me1=int(me1_xia)-int(me1_shou)
	me2=int(me2_xia)-int(me2_shou)
	return me1 ,me2,liulang_sum
def caijicpu(packagename):#这里采集的cpu时候可以是执行操作采集 就是-n  -d  刷新间隔
	cpu='adb shell top -n 1| findstr %s'%packagename
	re_cpu=os.popen(cpu).read().split()[2]
	return re_cpu
def getnencun(packagename):#Total 的 PSS 信息内存
	cpu='adb shell  dumpsys  meminfo %s'%packagename
	re_cpu=os.popen(cpu).read().split()[118]
	return re_cpu
def huoqufps(packagename):
	cmd ='adb shell dumpsys gfxinfo packagename '#获取fps
def adb_monkey(packagename,s_num,throttle,pct_touch,pct_motion,pct_trackball,pct_nav,pct_syskeys,pct_appswitch,num,logfilepath):
	cmden='adb shell monkey -p %s -s %s --throttle %s --pct-touch %s --pct-motion %s  --pct-trackball  %s  --pct-trackball %s  --pct-syskeys  %s  --pct-appswitch  %s   -v -v -v %s >%s'%(packagename,s_num,throttle,pct_touch,pct_motion,pct_trackball,pct_nav,pct_syskeys,pct_appswitch,num,logfilepath)
	os.popen(cmden)
def huoqushebeizhuangtai():
	cmd1='adb get-state'
	devices_status=os.popen(cmd1).read().split()[0]
	return devices_status
if __name__ == '__main__':
	print(getnencun('com.tencent.mobileqq'))