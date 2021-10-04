import os
import os.path
import scrapy

class BlogSpider(scrapy.Spider):
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    settings = {'LOG_LEVEL' :'INFO',
            'COOKIES_ENABLED' : False,
            'DOWNLOADER_MIDDLEWARES' : {
            'scrapy_cloudflare_middleware.middlewares.CloudFlareMiddleware': 560,
            }
            }
    test = []
    name = 'manga_spider'
    fo = open("manga.md", "w", encoding='gbk')

    def start_requests(self):
        for file in os.listdir("./"):
            if file.endswith("zip") and file.find('中国翻訳') == -1:
                file = file.replace("[自压]","")
                file = file.replace(".zip","")
                print(file)
                url = "https://btsow.one/search/" + file
                request = scrapy.Request(url=url, callback=self.btsow)
                yield request
                url = "https://sukebei.nyaa.si/?f=0&c=1_4&q="+ file
                request = scrapy.Request(url=url, callback=self.nyaa)
                yield request

    def btsow(self, response):
        for title in response.css('div.row'):
            name = title.css('a::attr(title)').get()
            url = title.css('a::attr(href)').get()
            if name and name.find('中国') != -1 or name and name.find('中文') != -1:
                md = "[" + name + "](magnet:?xt=urn:btih:" + url[-40:] + ")"
                self.fo.write( "BTSOW " + md +"\n\n")

    def nyaa(self, response):
        for title in response.css('tbody').css('tr'):
            name = title.css('td:nth-child(2)').css('a::text').get()
            url = title.css('td:nth-child(3)').css('a:nth-child(2)::attr(href)').get()
            if name and name.find('中国') != -1 or name and name.find('中文') != -1:
                md = "[" + name + "](" + url[:60] + ")"
                self.fo.write( "NYAA " + md +"\n\n")