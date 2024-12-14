import csv, os

def load_data() -> dict:
    file = "stutends.csv"
    
    result = {}
    if os.path.exists(file):
        file_instance = open(file, encoding = "UTF8")
        csv_reader = csv.DictReader(file_instance)
        
        for row in csv_reader:
            name = row.get("name")
            result[name] = row
    
    result["zhangsan"] = {"name": "zhangsan", "chinese": 89, "english": 90, "math": 100}
    
    return result


def save_data(data: dict):
    pass