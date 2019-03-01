
"""
Send wechat message to participants in psychological experiments.
Created by Yuki Tang / yukitang0703@gmail.com / Feb 2019
"""
__author__ = "Yuki Tang"
__version__ = "1.0"
__email__ = "yukitang0703@gmail.com"
__status__ = "alpha"

import itchat
import time

class wechat:
    def __init__():
        
    def wechat_login(Status = True):
        """scan the qrcode to login in on web server
        Status -- True: stay signed in; False: scan qrcode to sign in each time 
        """
        itchat.auto_login(True)
        itchat.send('登录成功！登录状态为%s'%Status,toUserName = 'filehelper')
        return True
        
    def get_user():
        user = itchat.get_friends(update = True)
        #print(type(user))
        
    def search_user(who):
        friend = itchat.search_friends(name=who)
        itchat.send('找到用户'+who,toUserName = 'filehelper')
        return friend

    def send_msg(msg, who,lapse = 0):
        """
        """
        time.sleep(lapse)
        friend = wechat.search_user(who)
        if  friend!=None:
            username = friend[0]['UserName']
            itchat.send_msg(msg,username)
            itchat.send('已发送给用户'+who+'：'+msg,toUserName = 'filehelper')
            return True
        else:
            itchat.send('没有找到用户'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),toUserName = 'filehelper')
            return None

    def wechat_logout():
        itchat.send('登出',toUserName = 'filehelper')
        itchat.logout()
        print("成功登出！")
wechat.wechat_login()
#wechatSend.get_user()
wechat.send_msg('早上好呀','许相宜')