from easygui import *
import os

f = open('C:\Windows\System32\drivers\etc\hosts','w')

checked = ccbox(msg='请选择',title='host修改器',choices=('翻墙','恢复'))
if checked:
    fq = open('hosts',encoding='UTF-8') .read()
    f.write(fq)
else:
    hf = open('oldhost').read()
    f.write(hf)

cmd = os.popen('ipconfig /flushdns');
info = cmd.readlines()
msgbox(msg=str(info),title='执行结果：',ok_button='确定')
