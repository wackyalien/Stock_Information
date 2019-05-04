def fetching():
    import sqlite3 as sq
    clientid = input('enter Client_Id')
    try:
        with sq.connect('stockmarket') as db:
            cursor = db.cursor()
            cursor.execute('''select lastprice,date,stock_name,email from buyers where clientid =?''', (clientid,))
            for row in cursor.fetchall():
                pass
    except Exception as E:
        print 'ERROR', E
    return row
