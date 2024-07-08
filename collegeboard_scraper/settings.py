import os

BOT_NAME = "collegeboard_scraper"

SPIDER_MODULES = ["collegeboard_scraper.spiders"]
NEWSPIDER_MODULE = "collegeboard_scraper.spiders"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

ROBOTSTXT_OBEY = False

SCRAPEOPS_API_KEY = os.environ.get("SCRAPEOPS_API_KEY")

SCRAPEOPS_PROXY_ENABLED = True

SCRAPEOPS_MONITORING = True
EXTENSIONS = {
    'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500,
}
DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

CONCURRENT_REQUESTS = 2
CONCURRENT_REQUESTS_PER_DOMAIN = 50
CONCURRENT_REQUESTS_PER_IP = 50
RETRY_ENABLED = True
REDIRECT_ENABLED = False
DOWNLOAD_TIMEOUT = 15

DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True

COOKIES_ENABLED = False

SPIDER_MIDDLEWARES = {
   "collegeboard_scraper.middlewares.CollegeboardScraperSpiderMiddleware": 543,
}


AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 50.0
AUTOTHROTTLE_DEBUG = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

LOG_LEVEL = 'INFO'