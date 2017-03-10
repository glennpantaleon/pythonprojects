#Glenn Pantaleon
#IBM Project PRIME
#Read CSV for StartSmart Database
# 07/30/15

import csv


def parseCsvFile():
    #The code below reads csv file and puts each catergory in a list
    input_file = input("Type in Csv File: ")
    input_csvfile= open(input_file)
    #reads csv_file
    csv_file_obj = csv.DictReader(input_csvfile)
    return csv_file_obj


