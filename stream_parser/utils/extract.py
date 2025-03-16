from selectolax.parser import HTMLParser
import re
import json
# def extract(html:str, attribs_list:list[str]):
#     '''
#     It extracts the given list of attribs from the html given.
#     '''
#     tree = HTMLParser(html)
#     attribs_dict = {}
#     for attrib in attriEA SPORTS FC™ 25"bs_int(re.sub("^[0-9.]$", string = price, repl="")) for price in priceslist:
#         extracted = tree.css(attrib)
#         attribs = [e.attribs for e in extracted]
#         attribs_dict[attrib] = attribs
#     return attribs_dict

class Extractor:
    '''
    Extracts the required info from HTML.
    '''
    def __init__(self, html, config):
        self.tree = HTMLParser(html)
        self.config = config
        self.parent_nodes = self.tree.css(self.config.get("container").get("game_on_sale")["selector"])
    
    def title(self):
        nodes = [node for parent_node in self.parent_nodes for node in parent_node.css(self.config.get("items").get("title")["selector"])]
        return [node.text() for node in nodes]
    

    def thumbnail_url(self):
        urls = []
        nodes = [node for parent_node  in self.parent_nodes for node in parent_node.css(self.config.get("items").get("thumbnail_url")["selector"])]
        for node in nodes:
            src = node.attributes.get("src", "")
            if src and src not in urls:
                urls.append(src)
        return urls
    
    def get_tags(self):
        tags=[]
        for parent_node in self.parent_nodes:
            tags_per_node=[]
            for node in parent_node.css(self.config.get("items").get("tags")["selector"])[:5]:
                tags_per_node.append(node.text())
            tags.append(tags_per_node)
        return tags

    def discounted_price(self):
        nodes = [node for parent_node in self.parent_nodes for node in parent_node.css(self.config.get("items").get("discounted_price")["selector"])]
        prices = [node.text() for node in nodes]
        prices = [re.sub(r"[^\d.]", "", price) for price in prices]
        return [float(price) if price else None for price in prices]
    
    def original_price(self):
        nodes = [node for parent_node in self.parent_nodes for node in parent_node.css(self.config.get("items").get("original_price")["selector"])]
        prices = [node.text() for node in nodes]
        prices = [re.sub(r"[^\d.]", "", price) for price in prices]
        return [float(price) if price else None for price in prices]
    
    def discount_prcnt(self):
        nodes = [node for parent_node in self.parent_nodes for node in parent_node.css(self.config.get("items").get("discount_prcnt")["selector"])]
        discounts = [node.text() for node in nodes]
        return [re.sub(r"[^\d]", "", discount) for discount in discounts]
        
    
    def reviews_sentiment(self):
        nodes = [node for parent_node in self.parent_nodes for node in parent_node.css(self.config.get("items").get("reviews_sentiment")["selector"])]
        return [node.text() if node.text() else None for node in nodes]
    
    def n_reviews(self):
        nodes = [node for parent_node in self.parent_nodes for node in parent_node.css(self.config.get("items").get("n_reviews")["selector"])]
        n_reviews = [node.text() if node.text() else None for node in nodes]
        return [re.sub(r"[^\d]", "", review) for review in n_reviews]
    def extract_all(self):
        dict = {
            "Title": self.title(),
            "Thumbnail": self.thumbnail_url(),
            "Tags": self.get_tags(),
            "Original Price": self.original_price(),
            "Discounted Price":self.discounted_price(),
            "Discount Percentage": self.discount_prcnt(),
            "Total Reviews": self.n_reviews(),
            "Reviews Sentement": self.reviews_sentiment()
            }
        with open("outputs/output.json", "w") as f:
            json.dump(dict, f, indent=4, ensure_ascii=False)
    

    


if __name__=="__main__":
    import asyncio
    from render import render
    from config.tools import get_config
    # offset=0
    # dict={}
    # while True:
    #     url = f"https://store.steampowered.com/specials?offset={offset}"
    #     html = asyncio.run(render(url))
    #     extractor = Extractor(html)
    #     data = extractor.extract_all()
    #     for key, values in data.items():
    #         if key not in dict:
    #             dict[key]=[]
    #         dict[key].extend(values)
    #     offset = len(dict["Title"])
    #     print(offset)
    #     print("Records updated...")
    #     print(len(dict["Title"]))
    #     if len(dict["Title"]) < 240:
    #         continue
    #     else:
    #         break
    config = get_config()
    url = config.get("url")
    html = asyncio.run(render(url))
    extractor = Extractor(html)
    extractor.extract_all()
    
        
