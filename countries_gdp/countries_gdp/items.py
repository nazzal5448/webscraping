import scrapy
from itemloaders.processors  import MapCompose, TakeFirst
from w3lib.html import remove_tags


def remove_commas(value:str):
    return value.replace(",","")

def try_float(value):
    try:
        return float(value)
    except Exception:
        return value

def strip_year(value):
    try:
        return int(value[-4:])
    except Exception:
        return value

class CountryGdpItem(scrapy.Item):
    country_name = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )
    gdp = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip, remove_commas, try_float),
        output_processor=TakeFirst()
    )
    year = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip, strip_year),
        output_processor=TakeFirst()
    )

