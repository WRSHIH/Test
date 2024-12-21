import csv, os.path
from common.common_def import ITEMS_SET

file = "Accounting.csv"

def load_data() -> dict:
    
    result = {}
    if os.path.exists(file):
        file_instance = open(file, 'r', encoding = "UTF-8")
        csv_reader = csv.DictReader(file_instance)
        
        for row in csv_reader:
            date = row.get("date")
            result[date] = row 
    # result["20240101"] = {"date": "20240101", "name": dinner, "expense": 90, "category": food}
    return result


def save_data(data: dict):
    file_instance = open(file,'w', encoding= "UTF-8")
    
    if len(data) > 0:
        rows = list(data.values()) #將expensure_data (dict) 內的values做成rows清單
        headers = ITEMS_SET
        
        csv_writer = csv.DictWriter(file_instance, headers, delimiter=',') 
        csv_writer.writeheader()
        csv_writer.writerows(rows)
        
    file_instance.close()