import scrapy
from project2.items import JobInfo

class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['jobs.51job.com']
    start_urls = ['http://jobs.51job.com/hy01/p1']

    def parse(self, response):
        divs = response.xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div')
        if divs is None:
            return
        items = []
        for div in divs:
            item = JobInfo()
            item['title'] = div.xpath('./p[1]/span/a/@title').extract_first()
            item['company'] = div.xpath('./p[1]/a/@title').extract_first()
            item['addr'] = div.xpath('./p[1]/span[2]/text()').extract_first()
            item['salary'] = div.xpath('./p[1]/span[3]/text()').extract_first()
            items.append(item)
        for item in items:
            yield item
        domain = response.request.url[0:28]
        pageid = response.request.url[28::]
        if int(pageid) > 20:
            return
        url = domain + str(int(pageid) + 1)
        yield scrapy.Request(
            url=url,
            callback=self.parse
        )
