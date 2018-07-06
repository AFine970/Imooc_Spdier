# coding:utf8
# python2.7
# 爬取慕课网免费课程30页的基本内容
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json
import pandas as pd
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


'''
网页中需要提取的元素
<div class="course-card-content">
	<h3 class="course-card-name">C4D创意字母教程</h3>
		<div class="clearfix course-card-bottom">
			<div class="course-card-info">
				<span>初级</span><span><i class="icon-set_sns"></i>75</span>
			</div>
			<p class="course-card-desc">综合运用C4D知识，完成案例实践，提升设计技能！</p>
		</div>
</div>
'''

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)" "AppleWebKit 537.36 (KHTML, like Gecko) Chrome"}

class Spider(object):
    def __init__(self):
        print '开始爬虫...'

    def to_txt(self, info):
        f.writelines(str(info['all_info']) + '\n')


    def spider(self, url):
        html = requests.session().get(url, headers=headers)
        selector = etree.HTML(html.text)
        # main_info =selector.xpath('//div[@class="course-card-content"]')
        # print html.encoding
        # print len(main_info)

        title = selector.xpath('//h3[@class="course-card-name"]/text()')
        meta = selector.xpath('//div[@class="course-card-info"]//span/text()')
        content = selector.xpath('//p[@class="course-card-desc"]/text()')


        # 利用切片对mata中的数据进行切割
        grade = meta[::2]
        nums = meta[1::2]

        # 利用json格式将list里的中文数据
        utitle = json.dumps(title, encoding="utf-8", ensure_ascii=False)
        ugrade = json.dumps(grade, encoding="utf-8", ensure_ascii=False)
        unums = json.dumps(nums, encoding='utf-8', ensure_ascii=False)
        ucontent = json.dumps(content, encoding="utf-8", ensure_ascii=False)
        print '标题', utitle
        print '级别', ugrade
        print '学习人数', unums
        print '简介', ucontent

        # 利用zip函数将4个LIST的下标一样的元素进行提取,变成一个新的序列
        main_info = zip(title, grade, nums, content)
        # print main_info
        final_info = json.dumps(main_info, encoding='utf-8', ensure_ascii=False)

        print '信息综合：', final_info
        print '\n'

        item = {}

        item['all_info'] = final_info
        self.to_txt(item)


if __name__ == '__main__':

    pool = ThreadPool(4)
    f = open('info.txt', 'a')
    page = []
    obj = Spider()

    # page = 'http://www.imooc.com/course/list?page=1' # 目标网址
    for i in range(1, 31):
        new_url = 'https://www.imooc.com/course/list?page=' + str(i)
        print '爬取的链接',new_url
        page.append(new_url)

    pool.map(obj.spider, page)     # 执行多线程爬取
    pool.close()
    pool.join()
    f.close()



