from utils.render import render
from utils.extract import Extractor
from config.tools import get_config
import json
import asyncio

url = get_config().get("url")
html = asyncio.run(render(url))
config = get_config()
extractor = Extractor(html, get_config())
extractor.extract_all()

