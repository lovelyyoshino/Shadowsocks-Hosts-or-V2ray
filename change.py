from easygui import *
import os

f = open('C:\Windows\System32\drivers\etc\hosts','w')

checked = ccbox(msg='请选择是否翻墙',title='host修改器',image="google.gif",choices=('翻墙','恢复'))
if checked:
	checked1 = ccbox(msg='请选择网络类型',title='网络类型',image="google.gif",choices=('IPv4','IPv6'))
	if checked1:
		fq = open('hostsv4',encoding='UTF-8') .read()
		f.write(fq)
	else:
		fq = open('hostsv6',encoding='UTF-8') .read()
		f.write(fq)
else:
	hf = open('oldhost').read()
	f.write(hf)

cmd = os.popen('ipconfig /flushdns');
info = cmd.readlines()
msgbox(msg=str(info),title='执行结果：',ok_button='确定')