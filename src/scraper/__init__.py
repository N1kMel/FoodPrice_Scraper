# %%
from bs4 import BeautifulSoup
import os
from dataclasses import dataclass
import json
from downloader import Downloader
from parse import Parser
from data import Data


def process(url: str, web_page_path=None, data_path=None):
    downloadhtml = Downloader(url, "raw.html")
    downloadhtml.download()

    parser = Parser("raw.html")
    parser.parse()
    parser.save()
    
    data = Data()
    outputTable = data.calculating("parsed.json")
    return outputTable

url = 'https://adjiki.ru/catalog/hachapuri/'
print(process(url))



