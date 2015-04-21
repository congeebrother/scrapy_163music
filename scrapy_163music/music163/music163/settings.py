# -*- coding: utf-8 -*-

# Scrapy settings for music163 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'music163'

SPIDER_MODULES = ['music163.spiders']
NEWSPIDER_MODULE = 'music163.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'music163 (+http://www.yourdomain.com)'
DOWNLOADER_MIDDLEWARES = {
    'music163.misc.middleware.CustomHttpProxyMiddleware': 400,
    'music163.misc.middleware.CustomUserAgentMiddleware': 401,
}

COOKIES_ENABLED = False

DOWNLOAD_DELAY = 30


ITEM_PIPELINES = {
    'scrapy.contrib.pipeline.images.ImagesPipeline': 1,
    'music163.pipelines.JsonWithEncodingPipeline':2,
}
IMAGES_STORE = './picture'
