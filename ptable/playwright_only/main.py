from config.tools import get_config
from utils.extract import Extract
from utils.render_js import render
import asyncio
import pandas as pd

def extract_elements_info(output_format="csv"):
    '''
    Utilizes `render` and `Extract` module to render and extract all the details about
    periodic table elements.

    Args:
        output_format: The format you want the output file in. can be "csv" or "json" only.
    
    Returns:
        None. But saves the output file to "outputs/" dir.
    '''

    if output_format == "csv" or output_format == "json":

        html = asyncio.run(render("https://pubchem.ncbi.nlm.nih.gov/ptable/"))
        extractor = Extract(html, get_config())
        dict = extractor.extract_all()

        if output_format == "json":
            import json
            with open("outputs/output.json", "w") as f:
                json.dump(dict, f, indent=4, ensure_ascii=False)
        
        elif output_format =="csv":
            pd.DataFrame(dict).to_csv("outputs/output.csv", index=False)
    else:
        raise ValueError("Please specify correct output format! ['csv', 'json']")
    

if __name__ == "__main__":
    extract_elements_info(output_format="csv")
