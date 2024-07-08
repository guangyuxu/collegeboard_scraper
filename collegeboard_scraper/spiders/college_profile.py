import json
import scrapy
from bs4 import BeautifulSoup

host = "https://bigfuture.collegeboard.org/colleges"


class CollegeProfileSpider(scrapy.Spider):
    name = "college_profile"
    allowed_domains = ["bigfuture.collegeboard.org"]

    def __init__(self, key=None, output_folder=None, *args, **kwargs):
        super(CollegeProfileSpider, self).__init__(*args, **kwargs)
        url = f"{host}/{key}"
        self.start_urls = [url,
                           f'{url}/admissions',
                           f'{url}/academics',
                           f'{url}/tuition-and-costs',
                           f'{url}/campus-life'
                           ] if url else []
        self.data = {}
        self.output = f'{output_folder}/{key}.json'

    def parse(self, response):
        if response.url.endswith("/admissions"):
            self.parse_admissions(response)
        elif response.url.endswith("/academics"):
            self.parse_academics(response)
        elif response.url.endswith("/tuition-and-costs"):
            self.parse_tuition_and_costs(response)
        elif response.url.endswith("/campus-life"):
            self.parse_campus_life(response)
        else:
            self.parse_home(response)

    def parse_home(self, response):
        soup = BeautifulSoup(response.text)
        label = soup.select_one(".cb-tabs-menu > ul > li > a.cb-selected").text

        data = {}
        location = soup.select_one("#csp-banner-section").select_one('div[data-testid="csp-banner-section-school-location-label"]')
        data.update({"location": location.text})

        academics_stats_section = soup.select_one('ul#academics-stats-section')

        for st in academics_stats_section.select('li > div > div > div'):
            key = st.select_one("div:nth-child(1)")
            value = st.select_one("div:nth-child(2)")
            data.update({key.text: value.text})

        description = academics_stats_section.find_next_sibling(attrs={"data-testid": "more-about-text"})
        data.update({"Description": description.text})

        for_the = description.find_next_sibling("div")
        for_the_key = for_the.select_one('p[data-testid="csp-more-about-college-board-code-labelId"]')
        for_the_value = for_the.select_one("#csp-custom-description-id-text")
        data.update({for_the_key.text: for_the_value.text})

        self.data.update({label: data})

    def parse_admissions(self, response):
        soup = BeautifulSoup(response.text)
        label = soup.select_one(".cb-tabs-menu > ul > li > a.cb-selected").text
        data = {}
        self.data.update({label: data})

    def parse_academics(self, response):
        soup = BeautifulSoup(response.text)
        label = soup.select_one(".cb-tabs-menu > ul > li > a.cb-selected").text
        data = {}
        self.data.update({label: data})

    def parse_tuition_and_costs(self, response):
        soup = BeautifulSoup(response.text)
        label = soup.select_one(".cb-tabs-menu > ul > li > a.cb-selected").text
        data = {}
        self.data.update({label: data})

    def parse_campus_life(self, response):
        soup = BeautifulSoup(response.text)
        label = soup.select_one(".cb-tabs-menu > ul > li > a.cb-selected").text
        data = {}
        self.data.update({label: data})

    def closed(self, reason):
        with open(self.output, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
        return
