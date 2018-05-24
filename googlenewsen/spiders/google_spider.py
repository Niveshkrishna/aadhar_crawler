# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import json

class GoogleSpider(scrapy.Spider):
    name = "googlenews"
    allowed_domains = ["news.google.co.in"]
    start_urls = [
        "https://news.google.com/search?q=aadhaar&hl=en-IN&gl=IN&ceid=IN:en" ]

    def parse(self, response):
        json_file = open('aadhar_news.json', 'w')
        titles = response.xpath('//div/div/a/span/text()').extract()[2:-1]
        links = response.xpath('//div/div/a/@href').extract()[2:-1]
        intros = response.xpath('//div/div/p/text()').extract()
        authors = response.xpath('//div/div/div/a/text()').extract()[3:]
        times = response.xpath('//div/div/time/text()').extract()
        article = {}
        for i in range(len(titles)):
            article["intro"] = intros[i]
            article["link"] = "https://news.google.com" + links[i][1:]
            article["time"] = times[i]
            try:
                article["author"] = authors[i]
            except:
                article["author"] = ""
            article["title"] = titles[i]
            json.dump(article, json_file, indent=2)
            json_file.write('\n')
            