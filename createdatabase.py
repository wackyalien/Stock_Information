def create_database():
    import sqlite3 as sq
    try:
        with sq.connect('stockmarket') as db:
            cursor = db.cursor()
            cursor.execute('''create table buyers(clientid int,name text,address text,phone int,stock_name text,email text,lastprice int,date date)''')
    except Exception as E:
        print 'error',E

    return 'database schema and table create successfully.'
