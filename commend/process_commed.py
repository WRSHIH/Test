from common import course_def


def process_list(student_data: dict):
    records = list(student_data.values())
    records.sort(key = lambda a: a.get("name"))
    
    for record in records:
        print(record.get("name"))
        for course in course_def.COURSE_NAME_SET:
            print(f"{course} score: {record.get(course)}")
        print("  ")


def process_add(student_data: dict):
    name = input("Please enter name: ")
    chinese_score = input("Please input chinese score: ")
    english_score = input("Please input english score: ")
    math_score = input("Please input math score: ")
    
    records = {
        "name":name,
        "chinese":int(chinese_score),
        "english":int(english_score),
        "math":int(math_score)
    }
    student_data[name] = records
    print(f"Added student scores for {name} succcessfully")
    
def process_edit(student_data: dict):
    name = input("Please input name: ")
    if name in student_data:
        course = input("Please input course name: ")
        if course in course_def.COURSE_NAME_SET:
            score = input("Please input score: ")
            student_data[name].update({course:int(score)})
            print(f"Updated score for '{name}' successfully")
            
        else:
            print(f"Course {course} is not supported.")
            
    
    else:
        print(f"Student {name} dose not exist.")


def process_delete(student_data: dict):
    name = input("Please input name: ")
    if name in student_data.keys(): 
        student_data.pop(name)
        print(f"Delete '{name}' successfully")
    else:
        print(f"Student '{name}' dose not exist!")
        


def process_average(student_data: dict):
    student_account = len(student_data)
    if student_account == 0:
        print("No student scores")
        return
    
    total_result = {}
    for course in course_def.COURSE_NAME_SET:
        total_result[course] = 0
        
    for record in student_data.values():
        for course in course_def.COURSE_NAME_SET:
            total_result[course] = total_result[course] + int(record.get(course))
    
    for course in course_def.COURSE_NAME_SET:
        average = total_result[course]/ student_account
        print(f"average score of {course} is {average}")


def process_exit(student_data: dict):
    pass




def process_commend(cmd: str, student_data: dict):
    if cmd == "list":
        process_list(student_data)
    elif cmd == "add":
        process_add(student_data)
    elif cmd == "edit":
        process_edit(student_data)
    elif cmd == "delete":
        process_delete(student_data)
    elif cmd == "average":
        process_average(student_data)