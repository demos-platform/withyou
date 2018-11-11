#coding=utf-8
import itchat, time
import datetime as dt

def my_scheduler(runTime):
  users = itchat.search_friends(name=u'牧云云')
  print users
  userName = users[0]['UserName']
  itchat.send(u'做我男朋友可以么',toUserName=userName)

itchat.auto_login() # 在命令行中展示二维码，默认展示的是图片二维码
# itchat.auto_login(enableCmdQR=True) # 在命令行中展示二维码，默认展示的是图片二维码
itchat.auto_login(hotReload=True) # 这个是方便调试用的，不用每一次跑程序都扫码
my_scheduler(now) # 启用定时操作
itchat.run()      # 跑微信服务