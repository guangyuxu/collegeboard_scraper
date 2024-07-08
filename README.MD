* NOTE: Please register in https://scrapeops.io/ and generate api key, it used to be free with 1000 request for new users
```
SCRAPEOPS_API_KEY=7aec179d-cae3-47e0-a059-************
```

* NOTE: This project is built with Flask + Scrapy + Beautifulsoup4
  * Flask: provide the Restful API to trigger the scraper
  * Scrapy: The most popular scraper framework, it supports html parsing as well
  * Beautifulsoup4: The required html parser tools

* NOTE: Since this app provide Restful API for triggering the scraper, additional download scripts is not necessary anymore. 

# Run the project
## 1. Run in IDE
```shell
run app.py
```
Environment Variable
```
SCRAPEOPS_API_KEY=7aec179d-cae3-47e0-a059-************
```

## 2. Run in Docker
```shell
docker build -t gavin/collegeboard_scraper .
docker run --init -d --rm \
-p 5000:5000 \
-e SCRAPEOPS_API_KEY=7aec179d-cae3-47e0-a059-************ \
gavin/collegeboard_scraper
```

# 2. Calling the scraper APIs
## 2.1. Scrape college list
```shell
curl -X POST http://localhost:5000/run_spider/colleges
```
## 2.2. Scrape data of a university
```shell
curl -X POST http://localhost:5000/run_spider/colleges/<university uri>
curl -X POST http://localhost:5000/run_spider/colleges/massachusetts-institute-of-technology
```