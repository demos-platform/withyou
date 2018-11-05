#coding=utf-8
import itchat, time
import datetime as dt
from apscheduler.schedulers.background import BackgroundScheduler

def tick():
  print '123'

itchat.auto_login() # 在命令行中展示二维码，默认展示的是图片二维码
itchat.auto_login(hotReload=True) # 这个是方便调试用的，不用每一次跑程序都扫码
now = dt.datetime.now() # 获取当前时间
scheduler = BackgroundScheduler()
scheduler.add_job(tick, 'date', run_date=now)
scheduler.start()

itchat.run()      # 跑微信服务