# -*- coding: utf-8 -*-
# @Date    : 2017-06-12
# @Author  : lileilei 
import threading
import tkinter
from tkinter import *
from tkinter import messagebox, ttk
from adb.ab_python import starttime_app, adb_monkey, huoqushebeizhuangtai, caijicpu, liulang, getnencun
from ulit.py_excel import qidongceshi, getcpu
from ulit.log import LOG,logger
@logger('启动app时间测试')
def qidongapp():
	start_tim=[]
	cishu=[]
	status_shebei=huoqushebeizhuangtai()
	if status_shebei =='device':
		try:
			packname=baoming_t.get('0.0',END)
			acti=activ_t.get('0.0',END)
			cish=cishu_ac.get()
		except:
			LOG.info('获取不到测试数据，请检查！')
			messagebox.showinfo('提醒', '获取不到测试数据，请检查！')
		if len(acti)<=1 or len(packname)<=1:
			messagebox.showinfo('提醒','包命或者包名activity不能为空')
			LOG.info('包命或者包名activity不能为空')
		else:
			if len(cish)<=1:
				messagebox.showinfo('提醒','次数不能为空')
				LOG.info('次数不能为空')
			else:
				i=0
				e1['state']= 'normal'
				e1.delete(1.0,tkinter.END)
				sum=0
				for i in range(int(cish)):
					start_time=starttime_app(packagename=packname,packagenameactivicy=acti)
					start_tim.append(int(start_time[1]))

					cishu.append(i)
					if start_time is None:
						messagebox.showwarning('警告','请检查您输入的包或者包的启动activity')
						break
					text='第%s次启动时间：%s'%(i+1,start_time[1])
					LOG.info('第%s次启动时间：%s'%(i+1,start_time[1]))
					sum+=int(start_time[1])
					e1['state']= 'normal'
					e1.insert(tkinter.END,text)
					e1.insert(tkinter.END,'\n')
					e1.see(END)
					btn_start['state']= 'disabled'
				e1.insert(tkinter.END,('平均用时:%s'%(sum/int(cish))))
				LOG.info(('平均用时:%s'%(sum/int(cish))))
				qidongceshi(cishu=cishu,start=start_tim)
				messagebox.showinfo('提示','测试报告已经生成，请到当前目录查看')
				LOG.info('测试报告已经生成，请到当前目录查看')
				e1['state']= 'disabled'
				btn_start['state']= 'normal'
				messagebox.showinfo('通知','测试已经完成')
				LOG.info('测试已经完成')
	else:
		messagebox.showerror('警告','设备连接异常')
		LOG.info('设备连接异常')
@logger('monkey测试')
def monkey_app():
	status_shebei=huoqushebeizhuangtai()
	if status_shebei =='device':
		try:
			packname=baoming_t1.get('0.0',END).split()[0]
			zhongzi=zhongzi_t.get('0.0',END).split()[0]
			time=time_t.get().split()[0]
			touch=touch_t.get('0.0',END).split()[0]
			huadong=huadong_t.get('0.0',END).split()[0]
			guiji=guiji_t.get('0.0',END).split()[0]
			xitong=xitong_t.get('0.0',END).split()[0]
			acti=acti_t.get('0.0',END).split()[0]
			event=event_t.get('0.0',END).split()[0]
			log=log_t.get('0.0',END).split()[0]
			danghang=danghang_t.get('0.0',END).split()[0]
			if len(packname)<=5:
				LOG.info('请正确填写包名')
				messagebox.showwarning('提醒','请正确填写包名')
			if int(touch)+int(huadong)+int(guiji)+int(danghang)+int(xitong)+int(acti) >100:
				messagebox.showerror('提醒','您输入的所有的事件的比例和不能超过100%')
				LOG.info('您输入的所有的事件的比例和不能超过100')
			adb_monkey(packagename=packname,s_num=zhongzi,throttle=time,pct_touch=touch,pct_motion=huadong,pct_trackball=guiji,pct_nav=danghang,pct_syskeys=xitong,pct_appswitch=acti,num=event,logfilepath=log)
		except :
			messagebox.showwarning('警告','必须填写monkey相关数据')
			LOG.info('monkey 测试出错，原因:%s'%Exception)
	else:
		LOG.info('设备连接异常 请重新连接设备!')
		messagebox.showwarning('警告','设备连接异常 请重新连接设备!')
@logger('cpu占用率,上传下载流量，内存的测试')
def cpu_app():
	status_shebei=huoqushebeizhuangtai()
	if status_shebei =='device':
		xingneng_bao=xingneng_baoming.get('0.0',END).split()[0]
		xing=xing_t.get()
		if len(xingneng_bao)<=5:
			LOG.info('包名必须真实有效')
			messagebox.showwarning('警告','请检查您的包名')
		cishu_list=[]
		cpu_list=[]
		rescv_list=[]
		send_list=[]
		total_list=[]
		pass_list=[]
		i=0
		for i in range(int(xing)):
			nen_cun=getnencun(xingneng_bao)
			rescv,send,liulang_sum=liulang(xingneng_bao)
			cpu_caiji=caijicpu(xingneng_bao)
			neicun_t['state']= 'normal'
			pass_list.append(int(nen_cun[:-1]))
			neicun_t.insert(tkinter.END,('Pass值：%s'%nen_cun))
			LOG.info('第%s次：Pass：%s' % (i, nen_cun))
			neicun_t.insert(tkinter.END,'\n')
			neicun_t.see(END)
			neicun_t['state']= 'disabled'
			cpu_t['state']= 'normal'
			cpu_list.append(int(cpu_caiji.split('%')[0]))
			cpu_t.insert(tkinter.END,('CPU占有率：%s'%cpu_caiji))
			LOG.info('第%s次：CPU占用率：%s'%(i,cpu_caiji))
			cpu_t.insert(tkinter.END,'\n')
			cpu_t.see(END)
			cpu_t['state']= 'disabled'
			liulang_t['state']= 'normal'
			total_list.append(int(liulang_sum))
			rescv_list.append(int(rescv))
			send_list.append(int(send))
			liulang_t.insert(tkinter.END,('总流量：%sk,上传流量:%sk,下载流量：%sk'%(liulang_sum,rescv,send)))
			LOG.info('第%s次：总流量：%sk,上传流量:%sk,下载流量：%sk' % (i, liulang_sum,rescv,send))
			liulang_t.insert(tkinter.END,'\n')
			liulang_t.see(END)
			liulang_t['state']= 'disabled'
			xingneng_btn['state']= 'disabled'
			i+=1
			cishu_list.append(int(i))
		getcpu(cishu=cishu_list,start_cpu=cpu_list,recv_list=rescv_list,send_list=send_list,total_list=total_list,Pass_list=pass_list)
		xingneng_btn['state']= 'normal'
		LOG.info('测试完成')
		messagebox.showinfo('提醒','测试完毕，测试报告已经生成！')
	else:
		LOG.info('测试的设备必须正常连接，请注意')
		messagebox.showwarning('警告','设备连接异常 请重新连接设备!')
@logger('次用线程来启动测试！采集cpu占用率,上传下载流量，内存')
def teread():#如果不是ui界面，可以不用线程
	for i in range(1):
		t=threading.Thread(target=cpu_app,args=())
		t.start()
@logger('启动app时间线程测试')
def teread_start():#如果不用ui界面，可以不用线程
	for i in range(1):
		t=threading.Thread(target=qidongapp,args=())
		t.start()
if __name__ == '__main__':
	LOG.info('测试小程序开始启动！测试开启！')
	try:
		status_shebei=huoqushebeizhuangtai()
		if status_shebei =='device':
			root=tkinter.Tk()
			root.title('雷子的安卓adb小工具')
			# root.geometry("1000x900")
			# root.resizable(width=False, height=False)
			tkinter.Label(root,text='性能参数展示',fg='red',font=("黑体", 15, "bold"),).grid(row=0,column=3)
			cpu_t=tkinter.Text(root,height=5,width=30)
			cpu_t.grid(row=1,column=2)
			liulang_t=tkinter.Text(root,height=5,width=40)
			liulang_t.grid(row=1,column=4)
			liulang_t.see(END)
			neicun_t=tkinter.Text(root,height=5,width=30)
			neicun_t.grid(row=3,column=2)
			neicun_t.see(END)
			suji_ev=[50,100,150,200,300]#这里还原可以增加可以选择的次数
			xing_t=ttk.Combobox(root,values=suji_ev,width=5)
			xing_t.current(0)
			xing_t.grid(row=1,column=6)
			tkinter.Label(root,text='cpu').grid(row=2,column=2)
			tkinter.Label(root,text='参数次数').grid(row=1,column=5)
			tkinter.Label(root,text='流量').grid(row=2,column=4)
			tkinter.Label(root,text='内存').grid(row=6,column=2)
			tkinter.Label(root,text='包名：').grid(row=7,column=1)
			xingneng_baoming=tkinter.Text(root,height=1,width=30)
			xingneng_baoming.grid(row=7,column=2)
			xingneng_btn=tkinter.Button(root,text='开始测试',font=("黑体", 15, "bold"),command=teread)
			xingneng_btn.grid(row=7,column=3)
			tkinter.Label(root,text='启动时间测试',fg='red',height=2,font=("黑体", 15, "bold")).grid(row=8,column=3)
			tkinter.Label(root,text='测试包名').grid(row=9,column=1)
			baoming_t=tkinter.Text(root,height=1,width=30)
			baoming_t.grid(row=9,column=2)
			tkinter.Label(root,text='测试包Activity').grid(row=9,column=3)
			activ_t=tkinter.Text(root,height=1,width=30)
			activ_t.grid(row=9,column=4)
			tkinter.Label(root,text='测试次数').grid(row=9,column=5)
			num=[10,20,30,50,100]
			cishu_ac=ttk.Combobox(root,values=num,state='readonly',width=5)
			cishu_ac.current(0)
			cishu_ac.grid(row=9,column=6)
			tkinter.Label(root,text='启动时间展示').grid(row=10,column=1)
			e1 = tkinter.Text(root,width=30,height=10, state="disabled")
			e1.grid(row=10,column=2,padx=20,pady=30)
			btn_start=tkinter.Button(root,text='测试',font=("黑体", 15, "bold"),command=teread_start)
			btn_start.grid(row=10,column=3)
			tkinter.Label(root,text='Monkey 测试',fg='red',font=("黑体", 15, "bold")).grid(row=11,column=3)
			tkinter.Label(root,text='测试包名：').grid(row=12,column=1)
			baoming_t1=tkinter.Text(root,height=1,width=30)
			baoming_t1.insert('0.0',0)
			baoming_t1.grid(row=12,column=2)
			tkinter.Label(root,text='随机种子个：').grid(row=12,column=3)
			zhongzi_t=tkinter.Text(root,height=1,width=30)
			zhongzi_t.grid(row=12,column=4)
			zhongzi_t.insert('0.0',0)
			tkinter.Label(root,text='时间间隔：').grid(row=12,column=5)
			suji_event=[500,1000,1500,2000,3000]
			time_t=ttk.Combobox(root,values=suji_event,width=5)
			time_t.current(0)
			time_t.grid(row=12,column=6)
			tkinter.Label(root,text='导航事件百分比：').grid(row=13,column=1)
			danghang_t=tkinter.Text(root,height=1,width=30)
			danghang_t.insert('0.0',0)
			danghang_t.grid(row=13,column=2)
			tkinter.Label(root,text='触摸事件百分比：').grid(row=13,column=3)
			touch_t=tkinter.Text(root,height=1,width=30)
			touch_t.grid(row=13,column=4)
			touch_t.insert('0.0',0)
			tkinter.Label(root,text='滑动事件百分比：').grid(row=14,column=1)
			huadong_t=tkinter.Text(root,height=1,width=30)
			huadong_t.grid(row=14,column=2)
			huadong_t.insert('0.0',0)
			tkinter.Label(root,text='轨迹球事件百分比:').grid(row=14,column=3)
			guiji_t=tkinter.Text(root,height=1,width=30)
			guiji_t.grid(row=14,column=4)
			guiji_t.insert('0.0',0)
			tkinter.Label(root,text='系统按键百分比：').grid(row=15,column=1)
			xitong_t=tkinter.Text(root,height=1,width=30)
			xitong_t.grid(row=15,column=2)
			xitong_t.insert('0.0',0)
			tkinter.Label(root,text='activity之间的切换百分比:').grid(row=15,column=3)
			acti_t=tkinter.Text(root,height=1,width=30)
			acti_t.grid(row=15,column=4)
			acti_t.insert('0.0',0)
			tkinter.Label(root,text='伪随机数:').grid(row=16,column=1)
			event_t=tkinter.Text(root,height=1,width=30)
			event_t.insert('0.0',0)
			event_t.grid(row=16,column=2)
			tkinter.Label(root,text='日志存放路径:').grid(row=16,column=3)
			log_t=tkinter.Text(root,height=1,width=30)
			log_t.grid(row=16,column=4)
			log_t.insert('0.0','F:\\monekey.txt')
			btn_monkey=tkinter.Button(root,text='启动Monkey测试',font=("黑体", 15, "bold"),command=monkey_app)
			btn_monkey.grid(row=17,column=3)
			root.mainloop()
		else:
			LOG('设备未连接或者连接异常!目前连接状态:%s'%status_shebei)
			print(status_shebei)
			print('设备未连接或者连接异常')
	except Exception as e:
		print(e)
		LOG.info('测试异常，原因：%s'%e)

