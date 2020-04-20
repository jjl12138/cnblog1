import scrapy
from cnblog.items import CnblogItem   #新添加

class Cnblog_Spider(scrapy.Spider):

    name = "cnblog"
    allowed_domains = ["cnblogs.com"]
    start_urls = [
     'https://www.cnblogs.com/',
    ]

    def parse(self, response):
        item = CnblogItem()    #新添加
        item['title'] = response.xpath('//a[@class="titlelnk"]/text()').extract()   #修改
        item['link'] = response.xpath('//a[@class="titlelnk"]/@href').extract()     #修改
        yield item   #新添加
