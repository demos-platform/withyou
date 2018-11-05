#coding=utf-8
import itchat, time
import datetime as dt

def my_scheduler(runTime):
  users = itchat.search_friends(name=u'牧云云')
  print users
  userName = users[0]['UserName']
  itchat.send(u'做我xxx可以么',toUserName=userName)