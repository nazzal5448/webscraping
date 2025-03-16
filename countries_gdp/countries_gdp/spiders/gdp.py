import scrapy
from countries_gdp.items import CountryGdpItem
from itemloaders import ItemLoader
class GdpSpider(scrapy.Spider):
    name = "gdp"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"]

    def parse(self, response):
        # for country in response.xpath("//table[contains(@class, 'wikitable sortable')]//tbody//tr"):
        #     yield{
        #         "country_name": country.xpath(".//td[1]//a/text()").get(),
        #         "gdp":country.xpath(".//td[2]/text()").get(),
        #         "year":country.xpath(".//td[3]/text()").get()
        #     }
        for country in response.css("table.wikitable.sortable tbody tr:not([class])"):
            item = ItemLoader(item=CountryGdpItem(), selector=country)
            item.add_css("country_name","td:nth-child(1) a")
            item.add_css("gdp","td:nth-child(2)")
            item.add_css("year","td:nth-child(3)")
            yield item.load_item()