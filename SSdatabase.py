import pycrunchbase

import csv

import STARTSMART_CsvReader
from pymongo import MongoClient



def add_csvfile_to_mongodb(file):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.test_database
    collection = db.test_collection
    data_id = collection.insert(file).inserted_id
    collection.save(data_id)


def add_another_csvfile():
    repsonse = input("Do you want to add another file? ")
    if repsonse == "Yes":
        csvfile =  STARTSMART_CsvReader.parseCsvFile()
    return csvfile

if __name__ =="__main__":
    try:
        file_bulk1 = STARTSMART_CsvReader.parseCsvFile()
        add_csvfile_to_mongodb(file_bulk1)
        file_bulk2 = add_another_csvfile()
        add_another_csvfile(file_bulk2)
    except UnicodeDecodeError:
        pass
