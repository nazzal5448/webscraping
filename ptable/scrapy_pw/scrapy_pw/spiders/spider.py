import scrapy
from scrapy.loader import ItemLoader
from scrapy_pw.items import PtableElement

class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["pubchem.ncbi.nlm.nih.gov"]
    start_urls = ["https://pubchem.ncbi.nlm.nih.gov/ptable/"]
    custom_settings = {
        "PLAYWRIGHT_LAUNCH_OPTIONS":{
            "headless": True,
            "timeout": 60 * 1000, 
        }
    }

    def start_requests(self):

        yield scrapy.Request(self.start_urls[0],
                             meta={
                                 "playwright":True
                             })

    def parse(self, response):
        for element in response.css("div.ptable div.element"):
            item = ItemLoader(PtableElement(), element,response)

            item.add_css("name", "button.block div.hidden[data-tooltip='Name']::text")
            item.add_css("symbol", "button.block div[data-tooltip='Symbol']::text")
            item.add_css("atomicNumber", "button.block div.w-full div[data-tooltip='Atomic Number']::text")
            item.add_css("atomicMass", "div.w-full div[data-tooltip='Atomic Mass, u']::text")
            item.add_css("chemicalGroup", "button.block div.hidden[data-tooltip='Chemical Group Block'] span.capitalize::text")
            
            yield item.load_item()