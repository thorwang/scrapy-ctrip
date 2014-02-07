# Scrapy settings for scrapy_ctrip project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_ctrip'

SPIDER_MODULES = ['scrapy_ctrip.spiders']
NEWSPIDER_MODULE = 'scrapy_ctrip.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_ctrip (+http://www.yourdomain.com)'
DEFAULT_REQUEST_HEADERS = {'Accept':'text/heml,application/xhtml+xml;q=0.9,*/*;q=0.8','Accept-Language':'ch',}