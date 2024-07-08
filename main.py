import os

from flask import Flask, request, jsonify, send_file
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.reactor import install_reactor
from twisted.internet import asyncioreactor
from scrapy import signals
from scrapy.signalmanager import dispatcher

app = Flask(__name__)

# Set the Twisted reactor to use AsyncioSelectorReactor
os.environ['TWISTED_REACTOR'] = 'asyncio'
install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
list_file = "college_list.json"


@app.route('/run_spider/colleges', methods=['POST'])
def run_spider_colleges():
    settings = get_project_settings()
    settings.set('FEED_URI', list_file)
    settings.set('FEED_FORMAT', "json")
    process = CrawlerProcess(settings)
    process.crawl(crawler_or_spidercls="college_list")
    process.start()
    process.stop()
    return send_file(list_file, as_attachment=True)


@app.route('/run_spider/colleges/<string:college_key>', methods=['POST'])
def run_spider_college(college_key):
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(crawler_or_spidercls="college_profile", key=college_key, output_folder=os.getcwd())
    process.start()
    process.stop()
    return send_file(f'{college_key}.json', as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("FLASK_RUN_PORT", 5000)), use_reloader=False, threaded=False)
