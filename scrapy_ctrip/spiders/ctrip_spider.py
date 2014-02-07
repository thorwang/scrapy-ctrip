from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector 
class ctripSpider(BaseSpider):
	name = 'ctrip'
	allowed_domains = 'http://www.ctrip.com/'
	start_urls = ['http://hotels.ctrip.com/hotel/dianping/441507_p2t0.html']
	
	#callback function when received response
	def parse(self, response):
		filename = response.url.split('/')[-1]
		with open(filename, 'w+') as file:
			content = str(response.body).decode('GB2312').encode('utf8')
			file.write(content)


