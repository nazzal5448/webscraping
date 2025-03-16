from scrapy.exceptions import DropItem
from itemadapter import ItemAdapter
import sqlite3

class CountriesGdpPipeline:
    def process_item(self, item, spider):
        if not isinstance(item["gdp"], float):
            raise DropItem("The GDP is not found so it is excluded.")
        return item

class SaveToDatabasePipeline:
    def __init__(self):
        self.con = sqlite3.connect("countries_gdp.db")
        self.cur = self.con.cursor()
    
    def open_spider(self, spider):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS countries_gdp
                         (country_name TEXT PRIMARY_KEY,
                         gdp REAL,
                         year INTEGER)""")
        self.con.commit()
    
    def process_item(self, item, spider):
        self.con.execute("""
            INSERT INTO countries_gdp(country_name, gdp, year) VALUES (?,?,?)
            """, (item["country_name"], item["gdp"], item["year"]))
        self.con.commit()
    
    def close_spider(self, spider):
        self.con.close()
        
        