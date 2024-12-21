from common.common_def import ITEMS_SET


def process_list(expensure_data: dict):
    records = list(expensure_data.values())
    
    for record in records:
        print(record.get("date"))
        for item in ITEMS_SET:
            print(f"{item}: {record.get(item)}")
        print("  ")


def process_add(expensure_data: dict):
    date = input("Please enter date (YYYYMMDD): ")
    name = input("Please input expense name: ")
    expense = input("Please input expense amount: ")
    category = input("Please input category: ")
    
    records = {
        "date":date,
        "name":str(name),
        "expense":int(expense),
        "category":str(category)
    }
    expensure_data[date] = records
    print(f"Expense for {name} on {date} was added succcessfully")
    
def process_edit(expensure_data: dict):
    date = input("Please enter date (YYYYMMDD): ")
    if date in expensure_data:
        name = input("Please input expense name: ")
        expense = input("Please input expense amount: ")
        category = input("Please input category: ")
         
        expensure_data[date].update({
            "date":date,
            "name":str(name),
            "expense":int(expense),
            "category":str(category)
            })
        print(f"Record updated on '{date}' successfully")
            
    else:
        print(f"Record on {date} dose not exist.")



def process_delete(expensure_data: dict):
    date = input("Please enter date (YYYYMMDD): ")
    if date in expensure_data.keys(): 
        expensure_data.pop(date)
        print(f"Delete record on '{date}' successfully")
    else:
        print(f"Record on {date} dose not exist.")
        




def process_commend(cmd: str, expensure_data: dict):
    if cmd == "list":
        process_list(expensure_data)
    elif cmd == "add":
        process_add(expensure_data)
    elif cmd == "edit":
        process_edit(expensure_data)
    elif cmd == "delete":
        process_delete(expensure_data)