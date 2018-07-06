# coding:utf8
# 测试文件
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pandas as pd
import numpy as np
# data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
data = [["UE4 基础入门教程", "入门", "48", "轻松入门虚幻引擎 UE4"], ["C4D创意字母教程", "初级", "217", "综合运用C4D知识，完成案例实践，提升设计技能！"], ["Python最火爬虫框架Scrapy入门与实践", "初级", "792", "做为爬虫工程师Python Scrapy主流爬虫框架你必须要会！"],
        ["MAYA四足动画", "入门", "1252", "根据老师所讲步骤一步一步学会四足动画的创建"], ["Swift之基于CALayer的图形绘制", "中级", "361", "了解CoreAnimation框架，掌握CALayer绘制实现方式。"], ["Retrofit网络库", "初级", "970", "介绍Retrofit网络框架及其使用，并使用Retrofit完成用户登录案例。"],
        ["MAYA- NURBS曲线建模", "入门", "534", "MAYA—2017NURBS曲线以及曲面工具的介绍"], ["mobx入门基础教程", "入门", "2264", "mobx框架基础入门,使用mobx做状态管理"], ["用GO语言构建自己的区块链", "初级", "3589", "区块链自己动手实现一把，啥都明白了。"], ["Crontab不知疲倦的时间表", "初级", "1802", "Crontab不知疲倦的时间表"],
        ["用Jenkins自动化搭建测试环境", "入门", "5219", "利用Jenkins实现测试环境的一键自动化部署。"], ["C4D基础入门案例", "入门", "1533", "C4D，设计师进军三维视界的必备技能"], ["PullToRefresh", "初级", "1931", "介绍APP中刷新和加载数据的解决方案，以及PullToRefresh框架如何使用"]]

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_colwidth',500)
name = ['id', 'uid', 'name', 'content']
try:
        test = pd.DataFrame(columns=name, data=data)
        test.to_html('1.html')
except Exception as e:
        print e
# s1=pd.Series(data)
# s2=pd.Series(data)
# df=pd.DataFrame({"a":data,"b":s2});
# print df


# d = {"Title":["one","two","three"],"Description":["first","second","third"],"PicUrl":["1","2","3"], "Url":["u1","u2","u3"]}
# def re_dic():
#     arr = []
#     for (k,v) in d.iteritems():
#         arr.append(v)
#     print zip(*arr)
# re_dic()

# a = [1, 2, 3]
# b= [4, 5, 6]
# c= [7, 8, 9]
# d=zip(a,b,c)
# print d
