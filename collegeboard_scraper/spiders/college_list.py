import scrapy

from collegeboard_scraper.items import CollegeBaseItem


class CollegeListSpider(scrapy.Spider):
    name = "college_list"
    allowed_domains = ["bigfuture.collegeboard.org"]
    start_urls = ["https://bigfuture.collegeboard.org/colleges"]

    def parse(self, response):
        lis = response.css("#list-scroll-stop ~ .container li")
        for li in lis:
            yield {
                "name": li.css("a::text").get().strip(),
                "url": li.css("a::attr(href)").get().strip()
            }
