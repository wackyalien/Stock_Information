def read():
    import sqlite3 as sq
    try:
        with sq.connect('stockmarket') as db:
            cursor = db.cursor()
            cursor.execute('''Select * from buyers''')
            for row in cursor.fetchall():
                pass
    except Exception as E:
        print 'ERROR',E
    return row
