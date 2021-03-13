import sqlite3 as db
import sys


def init():
    '''
    Initialize a new database that will store all
    the expenditures
    '''
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS EXPENSES (
    amount NUMBER,
    category STRING,
    message STRING,
    date STRING
    )'''
    cur.execute(sql)
    conn.commit()


def log(amount, category, message=''):
    '''
    Logs the expenditure in database.
    Message is optional.
    '''
    from datetime import datetime
    date = str(datetime.now())
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
    INSERT INTO EXPENSES VALUES(
    {},'{}','{}','{}')
    '''.format(amount, category, message, date)
    cur.execute(sql)
    conn.commit()


def view(category=None):
    '''
    Returns a list of all the expenditures incurred,
    and the total expense. If a category is specified,
    it only returns infor from that category
    '''
    conn = db.connect("spent.db")
    cur = conn.cursor()
    if (category):
        sql = '''
        SELECT * FROM EXPENSES WHERE CATEGORY='{}'
        '''.format(category)
        sql2 = '''
        SELECT SUM(amount) FROM EXPENSES WHERE CATEGORY='{}'
        '''.format(category)
    else:
        sql = 'SELECT * FROM EXPENSES'
        sql2 = 'SELECT SUM(amount) FROM EXPENSES'
    cur.execute(sql)
    results = cur.fetchall()
    print("Total rows are:  ", len(results))
    for row in results:
        print("Amount: ", row[0])
        print("Category: ", row[1])
        print("Message: ", row[2])
        print("Date: ", row[3])
        print("\n")
    cur.execute(sql2)
    total_amount = cur.fetchone()[0]
    print("Total amount spent:", total_amount)
    


def month_view(month):
    '''
    Returns the list of expenditured incurred,
    for only the month specified by user.
    '''
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
        SELECT amount,category,message,strftime("%Y/%m/%d", date) FROM EXPENSES
        WHERE strftime('%m', date) = '{}'
        '''.format(month)
    sql2 = '''
          SELECT MAX(amount),category FROM EXPENSES
          WHERE strftime('%m', date) = '{}'
        '''.format(month)
    cur.execute(sql)
    result = cur.fetchall()
    print("Total rows are:  ", len(result))
    for row in result:
        print("Amount: ", row[0])
        print("Category: ", row[1])
        print("Message: ", row[2])
        print("Date: ", row[3])
        print("\n")
    cur.execute(sql2)
    max_spent = cur.fetchone()[0]
    print("Maximum spent: ", max_spent)
    


def year_view(year):
    '''
    Returns the list of expenditure incurred,
    for only the year specified by user.
    '''
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
        SELECT amount,category,message,strftime("%Y/%m/%d", date) FROM EXPENSES
        WHERE strftime('%Y', date) = '{}'
        '''.format(year)
    cur.execute(sql)
    result = cur.fetchall()
    print("Total rows are:  ", len(result))
    for row in result:
        print("Amount: ", row[0])
        print("Category: ", row[1])
        print("Message: ", row[2])
        print("Date: ", row[3])
        print("\n")

    

def main():

    if __name__ == "__main__":
        print("*********************************************************")
        print("EXPENSE TRACKER APPLICATION")
        print("*********************************************************")
        choice = int(input(
            "Enter your choice: \n 1. Log into Tracker \n 2. View expense report \n 3. View monthly report \n 4. View yearly report \n 5. Exit\n\n"))
        if (choice == 1):
            amount = int(input("How much did you spend?\t"))
            category = input("What did you spend on?\t")
            message = input("Any additional message? Enter '' to leave blank.\t")
            log(amount, category, message)
        elif (choice == 2):
            category = input(
                "Do you want to see expenses of particular category? Press Enter to leave blank and view complete report. \t")
            print(view(category))
        elif (choice == 3):
            month = input("For which month do you want the expense report? (Enter in numerical form) \t")
            print(month_view(month))
        elif (choice == 4):
            year = input("For which year do you want the expense report? (Enter in numerical form) \t")
            print(year_view(year))
        elif (choice == 5):
            sys.exit()
        else:
            print("Choose the correct option")
            main()
        while choice == 5:
            break
        else:
            replayMenu()


def replayMenu():
    startover = ""
    startover = input("Would you like to start from the beginning, yes or no? ")
    while startover.lower() != "yes":
        print("Thanks for using Budget Tracker! ")
        break
    else:
        main()

def display():
    print("           \\\ //                 ")
    print("            (@)      \\\ //    ")
    print("          //  \\\      (@)")
    print("        //      \\\   //  \\\  WELCOME TO BUDGET TRACKER  !!  ")
    print("        \\\      //   \\\__//       ")
    print("         \\\____//   ")

display()
main()
