from commend.user_commend import get_user_commend
from commend.process_commed import process_commend
from store.csv_store import load_data, save_data


def main():
        
    try:
        student_data = load_data()
    except:
        print('error happend')
        return
    
    while True:
        commend = get_user_commend()
        if commend == "exit":
            break
        process_commend(commend, student_data)
        




if __name__ == "__main__":
    main()
    