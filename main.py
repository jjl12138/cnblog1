# -*- coding: utf-8 -*-
# @Author : 江河
# @Email  : 2516638426@qq.com
# @Time   : 2020/4/20 11:06
# @File   : main
# @Project: cnblog

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('cnblog')    #  你需要将此处的spider_name替换为你自己的爬虫名称
    process.start()
