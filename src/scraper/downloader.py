# %%
import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
from dataclasses import dataclass

@dataclass
class Downloader:
  url: str
  file_path: str
  html_text: str = None

  def download(self):
   basedir = os.path.dirname(os.path.realpath(__file__)) + "//"
   try:
    self.html_text = requests.get(self.url).text
   except Exception as ex:
    print(ex.args)
   try:
    with open(basedir + self.file_path, "w") as file:
     file.write(self.html_text)
   except Exception as ex:
    print(ex.args)











