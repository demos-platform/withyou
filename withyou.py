#coding=utf-8
import itchat, time
import datetime as dt
from apscheduler.schedulers.background import BackgroundScheduler
import random
import requests
import logging
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def my_scheduler(runTime):
  scheduler = BackgroundScheduler()
  scheduler.add_job(tick, 'date', run_date=runTime)
  scheduler.start()

# 获取天气
def getWeatherInfo(userName):
  weatherResult = requests.get('https://api.seniverse.com/v3/weather/daily.json?key=wexzetwpe7cwud8i&location=陕西西安&language=zh-Hans&unit=c&start=0&days=5')
  todayweatherInfo = weatherResult.json()['results'][0]['daily'][0]
  tomorrowweatherInfo = weatherResult.json()['results'][0]['daily'][1]
  return (u'西安今日%s, 最高温度%d°, 最低温度%d°; 明日%s, 最高温度%d°, 最低温度%d°; 容宝宝注意保暖哦，晚安🌙'%(todayweatherInfo['text_day'],
  int(todayweatherInfo['high']), int(todayweatherInfo['low']), tomorrowweatherInfo['text_day'],
  int(tomorrowweatherInfo['high']), int(tomorrowweatherInfo['low'])))

greetList = ['看好你哟，又是元气满满的一天(*^▽^*)','好好完成实验加油哟^_^','注意身体多喝热水哟(*^▽^*)','想你了求自拍，^_^']
def tick():
  users = itchat.search_friends(name=u'me')
  userName = users[0]['UserName']
  meetDate = dt.date(2018,11,05)                 # 开始打卡日期
  nowDate = dt.date.today()                      # 今天的日期
  passDates = int((nowDate - meetDate).days) + 1 # 打卡天数
  weatherMsg = getWeatherInfo(userName)

  itchat.send(u'暖心服务与昭容一起度过%d天啦^_^，%s'%(passDates,str(random.sample(greetList,1)[0])),toUserName=userName)
  itchat.send(weatherMsg, toUserName=userName)
  # nextTickTime = now + dt.timedelta(days=1)
  # nextTickTime = nextTickTime.strftime("%Y-%m-%d 07:30:00")
  # my_scheduler(nextTickTime) # 设定一个新的定时任务，明天 7 点半准时问候

log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO) # DEBUG
fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)
itchat.auto_login() # 在命令行中展示二维码，默认展示的是图片二维码
# itchat.auto_login(enableCmdQR=True) # 在命令行中展示二维码，默认展示的是图片二维码
itchat.auto_login(hotReload=True) # 这个是方便调试用的，不用每一次跑程序都扫码
now = dt.datetime.now() # 获取当前时间
# nextTickTime = now + dt.timedelta(days=0)
# nextTickTime = now + dt.timedelta(days=0)
# nextTickTime = nextTickTime.strftime("%Y-%m-%d 07:20:00")
my_scheduler(now) # 启用定时操作
itchat.run()      # 跑微信服务