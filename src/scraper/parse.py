# %%
from bs4 import BeautifulSoup
import os
from dataclasses import dataclass
import json

basedir = os.path.dirname(os.path.realpath(__file__)) + "//"

class Parser:
  def __init__(self, fileName) -> None:
    self.fileName: str = fileName
    self.dishesList: list =[]

  
  def parse(self):    
    with open(basedir + self.fileName, "r") as file:
      html_text = file.read()

    soup = BeautifulSoup(html_text,  "html.parser")

    results = soup.find(id = "catalog-products")

    cards = results.findAll(class_ =  "product-info")

    dishesList = []

    for card in cards:
     _price = card.find("span", class_ = "price", itemprop="price")
     _name = card.find("div", class_ = "name")
     _weight = card.find("div", class_ = "weight")
     info = {
       "name": _name.text,
       "price": _price.text,
       "weight": int(_weight.text[:-2])/1000,
        }

     dishesList.append(info)

  def save(self):
    with open("parsed.json", "w") as file:
      file.write(json.dumps(self.dishesList, ensure_ascii=False))






