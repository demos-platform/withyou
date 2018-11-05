#coding=utf-8
import itchat, time
import datetime as dt
from apscheduler.schedulers.background import BackgroundScheduler
import random

def my_scheduler(runTime):
  users = itchat.search_friends(name=u'無風')
  print users
  userName = users[0]['UserName']
  itchat.send(u'test',toUserName=userName)

# if __name__ == '__main__':
itchat.auto_login() # 在命令行中展示二维码，默认展示的是图片二维码
# itchat.auto_login(enableCmdQR=True) # 在命令行中展示二维码，默认展示的是图片二维码
itchat.auto_login(hotReload=True) # 这个是方便调试用的，不用每一次跑程序都扫码
now = dt.datetime.now() # 获取当前时间
nextTickTime = now + dt.timedelta(days=1) #下一个问候时间为明天的现在
nextTickTime = nextTickTime.strftime("%Y-%m-%d 00:00:00") # 把下一个问候时间设定为明天的零点
my_scheduler(nextTickTime) # 启用定时操作
itchat.run() # 跑微信服务

# def my_scheduler(runTime):
#   scheduler = BackgroundScheduler() # 生成对象
#   scheduler.add_job(tick, 'date', run_date=runTime)  # 在指定的时间，只执行一次
#   scheduler.start()

# 一些备选问候语
# greetList = ['快去睡觉别熬夜','好好找工作加油','注意身体多喝热水','想你了求自拍']
# def tick():
#   users = itchat.search_friends(name=u'xxx') # 找到你女朋友的名称
#   userName = users[0]['UserName']
#   meetDate = dt.date(2015,9,29)  # 这是你跟你女朋友相识的日期
#   now = dt.datetime.now()     # 现在的时间
#   nowDate = dt.date.today()  # 今天的日期
#   passDates = (nowDate-meetDate).days # 你跟你女朋友认识的天数
#   itchat.send(u'今天是我们认识第%d天，%s,晚安'%(passDates,random.sample(greetList,1)[0]),toUserName=userName) # 发送问候语给女朋友
#   nextTickTime = now + dt.timedelta(days=1)
#   nextTickTime = nextTickTime.strftime("%Y-%m-%d 00:00:00")
#   my_scheduler(nextTickTime) # 设定一个新的定时任务，明天零点准时问候