# %%
from bs4 import BeautifulSoup
import os
from dataclasses import dataclass
import json
from math import ceil
from prettytable import PrettyTable 
from operator import itemgetter

basedir = os.path.dirname(os.path.realpath(__file__)) + "//"

class Data:
  def __init__(self) -> None:
    self.dishesList: list =[]

  def calculating(self, filename: str):    
    with open(basedir + filename, "r") as file:
      self.dishesList = json.load(file) 

    for dish in self.dishesList:
     dish["kgPrice"] = ceil(int(dish["price"])/dish["weight"])

    dishesListSort = sorted(self.dishesList, key=itemgetter("kgPrice")) 
    listValues = []
    th = ['Название блюда', 'Цена', 'Масса', 'Цена за кг']
    columns = len(th)


    for dish in dishesListSort:
     for k, v in dish.items():
       listValues.append(v)

    table = PrettyTable(th)
    while listValues:
     table.add_row(listValues[:columns])
     listValues = listValues[columns:]
    return str(table)






