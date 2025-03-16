_config = {

    "url": "https://pubchem.ncbi.nlm.nih.gov/ptable/",
    "parentContainer":{
        "selector":"div.ptable div.element",
        "returns": "[Node]"
    },

    "items":{

        "name":{
            "selector":"button.block > div.hidden[data-tooltip='Name']",
            "returns": "[Node]"
        },

        "symbol":{
            "selector":"button.block > div[data-tooltip='Symbol']",
            "returns": "[Node]"
        },

        "atomicNumber":{
            "selector":"button.block > div.w-full > div[data-tooltip='Atomic Number']",
            "returns": "[Node]"
        },

        "atomicMass":{
            "selector":"button.block > div.w-full  div.hidden[data-tooltip='Atomic Mass, u']",
            "returns": "[Node]"
        },

        "chemicalGroup":{
            "selector":"button.block > div.hidden[data-tooltip='Chemical Group Block']",
            "returns": "[Node]"
        },
        
    }
}

def get_config(load_from_file=False):
    if load_from_file:
        with open("config.json", "r") as f:
            return json.load(f)
    
    return _config

def generate_config():
    with open("config/config.json", "w") as f:
        json.dump(_config, f, indent=4 )
    f.close()


if __name__ == "__main__":
    import json
    generate_config()
    # print(_config.get("url"))