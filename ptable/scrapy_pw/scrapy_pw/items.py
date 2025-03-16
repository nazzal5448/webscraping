import scrapy
from itemloaders.processors import MapCompose, TakeFirst

class PtableElement(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    symbol = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    atomicNumber = scrapy.Field(
        input_processor=MapCompose(int),
        output_processor=TakeFirst()
    )
    atomicMass = scrapy.Field(
        input_processor=MapCompose(float),
        output_processor=TakeFirst()
    )
    chemicalGroup = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )