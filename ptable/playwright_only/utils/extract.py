from selectolax.parser import HTMLParser


class Extract:
    '''
    Extracts all the the details about each element of the periodic table from the given html.

    Args:
        html: HTML of the periodic table site.
        config: The config dict which stores info about each selector and item to be scraped along with url of the site.
    
    Returns:
        dict: {

            {name, symbol, atomicNumber, atomicMass, chemicalGroup},
            ....
            
            }
    '''
    def __init__(self, html, config):
        self.config = config
        self.tree = HTMLParser(html)
        self.elements = self.tree.css(config.get("parentContainer").get("selector"))

    def get_name(self):
        return [e.text() for element in self.elements for e in element.css(self.config.get("items").get("name").get("selector"))]
    
    def get_symbol(self):
        return [e.text() for element in self.elements for e in element.css(self.config.get("items").get("symbol").get("selector"))]
    
    def get_an(self):
        return [e.text() for element in self.elements for e in element.css(self.config.get("items").get("atomicNumber").get("selector"))]
    
    def get_am(self):
        return [e.text() for element in self.elements for e in element.css(self.config.get("items").get("atomicMass").get("selector"))]
    
    def get_chemical_group(self):
        return [e.text() for element in self.elements for e in element.css(self.config.get("items").get("chemicalGroup").get("selector"))]
    
    def extract_all(self):
        return {
            "Name": self.get_name(),
            "Symbol":self.get_symbol(),
            "Atomic Number": self.get_an(),
            "Atomic Mass": self.get_am(),
            "Chemical Group": self.get_chemical_group()
        }
    
