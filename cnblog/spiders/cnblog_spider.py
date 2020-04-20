import scrapy
from ..items import CnblogsItem

class CnSpider(scrapy.Spider):
    name = 'cnblog'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/pick/']

    def parse(self, response):
        div_list = response.xpath("//div[@id='post_list']/div")
        for div in div_list:
            item = CnblogsItem()
            item["post_author"] = div.xpath(".//div[@class='post_item_foot']/a/text()").extract_first()
            item["author_link"] = div.xpath(".//div[@class='post_item_foot']/a/@href").extract_first()
            item["post_date"] = div.xpath(".//div[@class='post_item_foot']/text()").extract()
            item["comment_num"] = div.xpath(".//span[@class='article_comment']/a/text()").extract_first()
            item["view_num"] = div.xpath(".//span[@class='article_view']/a/text()").extract_first()
            item["title"] = div.xpath(".//h3/a/text()").extract_first()
            item["title_link"] = div.xpath(".//h3/a/@href").extract_first()
            item["item_summary"] = div.xpath(".//p[@class='post_item_summary']/text()").extract()
            item["digg_num"] = div.xpath(".//span[@class='diggnum']/text()").extract_first()
            yield item

        next_url = response.xpath(".//a[text()='Next >']/@href").extract_first()
        if next_url is not None:
            next_url = "https://www.cnblogs.com" + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
