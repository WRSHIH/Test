import csv, os.path
from common import course_def 

file = "stutends.csv"

def load_data() -> dict:
    
    result = {}
    if os.path.exists(file):
        file_instance = open(file, encoding = "UTF8")
        csv_reader = csv.DictReader(file_instance)
        
        for row in csv_reader:
            name = row.get("name")
            result[name] = row 
    # result["zhangsan"] = {"name": "zhangsan", "chinese": 89, "english": 90, "math": 100}
    return result


def save_data(data: dict):
    file_instance = open(file,'w', encoding= "UTF8", newline = " ")
    
    if len(data) > 1:
        rows = list(data.values()) #將student_data (dict) 內的values做成rows清單
        headers = course_def.COURSE_NAME_SET.union({"name"})
        
        csv_writer = csv.DictWriter(file_instance, fieldnames = headers) 
        csv_writer.writeheader()
        csv_writer.writerows(rows)
        
    file_instance.close()