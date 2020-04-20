# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FilePipeline(object):
    '''
    实现保存到txt文件的类，类名这个地方为了区分，做了修改，
    当然这个类名是什么并不重要，你只要能区分就可以，
    请注意，这个类名待会是要写到settings.py文件里面的。
    '''
    def process_item(self, item, spider):
        with open('cnblog.txt', 'w', encoding='utf-8') as f:
            titles = item['title']
            links = item['link']
            for i,j in zip(titles, links):
                f.write(i + ':' + j + '\n')
        return item
