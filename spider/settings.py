# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spider'

SPIDER_MODULES = ['spider.spiders']
NEWSPIDER_MODULE = 'spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
#不按照rebots进行爬取
ROBOTSTXT_OBEY = False

# Redis
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
#SCHEDULER_IDLE_BEFORE_CLOSE = 10
#REDIS_HOST = 'localhost'
#REDIS_PORT = 6379

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#处理并发数
#CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = True
TELNETCONSOLE_HOST = '127.0.0.1'
TELNETCONSOLE_PORT = '6023'

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# 中间件
# KEY=中间件;VALUE=中间件顺序
SPIDER_MIDDLEWARES = {
    #'spider.middlewares.TutorialSpiderMiddleware': 543,
    #'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 531,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'spider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': 500,
#    'tutorial.openextension.SpiderOpenCloseLogging': 501
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# 执行的优先度
# KEY=管道文件;VALUE=管道顺序
ITEM_PIPELINES = {
    'spider.pipelines.SpiderPipeline': 300,
    #'scrapy_redis.pipelines.RedisPipeline': 301
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#开启爬取速度间隔
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#开始间隔时间为3秒
#AUTOTHROTTLE_START_DELAY = 3
# The maximum download delay to be set in case of high latencies
#如果请求未响应,最大延迟时间为20秒
#AUTOTHROTTLE_MAX_DELAY = 20
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#爬取时Debug信息
#AUTOTHROTTLE_DEBUG = True
DOWNLOAD_DELAY = 5

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#测试扩展
#MYEXT_ENABLED = True

################日志################
#开启日志
#LOG_ENABLED = True
#日志文件位置
#LOG_FILE = "日志路径"
#日志编码
#LOG_ENCODING = "utf-8"
#日志级别
#LOG_LEVEL = "DEBUG"
#标准输出
#LOG_STDOUT = False

#开启Cookie追踪
COOKIES_ENABLED = True
COOKIES_DEBUG = True

##################Web###############
#开启web服务
WEBSERVICE_ENABLED = True
#日志文件位置
WEBSERVICE_LOGFILE = "日志路径"
#端口
WEBSERVICE_PORT = [6080, 7030]
#主机
WEBSERVICE_HOST = '127.0.0.1'

#################自动限速###############
#启用AutoThrottle扩展
#AUTOTHROTTLE_ENABLED = True
#初始下载延迟(单位:秒)
#AUTOTHROTTLE_START_DELAY = 1.0
#在高延迟情况下最大的下载延迟(单位秒)
#AUTOTHROTTLE_MAX_DELAY = 60.0
#起用AutoThrottle调试(debug)模式，展示每个接收到的response
#AUTOTHROTTLE_DEBUG = True
#DOWNLOAD_DELAY = 1.0