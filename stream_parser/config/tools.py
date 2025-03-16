import json


_config ={
    "url": "https://store.steampowered.com/specials",
    "container": {
        "game_on_sale": {
            "selector": "div.gASJ2lL_xmVNuZkWGvrWg",
            "match": "all",
            "type": "node"
            }
},
    "items": {
        "title": {
            "selector": "div.StoreSaleWidgetTitle",
            "match": "all",
            "type": "text"
                },
        "thumbnail_url": {
            "selector": "div.CapsuleImageCtn > img",
            "match": "all",
            "type": "text"
                },
        "tags": {
            "selector": "div._2bkP-3b7dvr0a_qPdZEfHY > a",
            "match": "5",
            "type": "node"
            },
        "discounted_price": {
            "selector": "div._3j4dI1yA7cRfCvK8h406OB",
            "match": "all",
            "type": "node"
            },
        "original_price": {
            "selector": "div._3fFFsvII7Y2KXNLDk_krOW",
            "match": "all",
            "type": "node"
            },
        "discount_prcnt": {
            "selector": "div.cnkoFkzVCby40gJ0jGGS4",
            "match": "all",
            "type": "node"
            },
        "reviews_sentiment": {
            "selector": "div._2nuoOi5kC2aUI12z85PneA",
            "match": "all",
            "type": "node"
        },
        "n_reviews": {
            "selector": "div._1wXL_MfRpdKQ3wZiNP5lrH",
            "match": "all",
            "type": "node"
        }
    }
}

def get_config(load_from_file=False):
    if load_from_file:
        with open("config.json", "r") as f:
            return json.load(f)
        
    return _config

def generate_config():
    with open("config.json", "w") as f:
        json.dump(_config, f, indent=4)
if __name__ == "__main__":
    generate_config()