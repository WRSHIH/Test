"""
簡單記帳工具透過輸入以下指令來達成
1. 新增紀錄: add
2. 顯示紀錄: list
3. 刪除紀錄: delete
4. 離開程式: exit

#待解決問題
1. 新增同一日期花費會被覆蓋
2. 計算功能待新增  
"""



from commend.user_commend import get_user_commend
from commend.process_commed import process_commend
from store.csv_store import load_data, save_data


def main():
    
    try:
        expensure_data = load_data()
    except:
        print('error happend')
        return
    
    while True:
        commend = get_user_commend()
        if commend == "exit":
            break
        process_commend(commend, expensure_data)  
   
    try:
        save_data(expensure_data)
    except:
        print('error happend')
        return
        


if __name__ == "__main__":
    main()
    