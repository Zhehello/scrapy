# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AngelItem
from scrapy.pipelines.images import ImagesPipeline

class AngelspiderSpider(CrawlSpider):
    name = 'ang'
    allowed_domains = ['angelimg.com']
    start_urls = ['http://www.angelimg.com/']
    #start_urls=['http://www.angelimg.com/ang/1440']    

    rules = (
        Rule(LinkExtractor(allow=r'http://www.angelimg.com/ang/\d+/\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'http://www.angelimg.com/ang/\d+'), follow=True),
        Rule(LinkExtractor(allow=r'http://www.angelimg.com/index/\d+'), follow=True),
        #Rule(LinkExtractor(allow=r'http://www.angelimg.com/ang/\d+/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = AngelItem()
        item['image_urls'] = response.xpath('.//div[@id="content"]/a/img/@src').extract()
        print(item,"-----------------------")
        yield item
        #item_["images"]
        
        
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i

#规则倒着写
#首页翻页-- 不需要回调
   #图集首页 --不要回调
      #对应的图集翻页 --提取图片url 供下载
