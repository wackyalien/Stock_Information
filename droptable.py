import sqlite3 as sq
try:
    with sq.connect('stockmarket') as db:
        cursor = db.cursor()
        cursor.execute('''Drop table buyers''')
except Exception as E:
    print 'ERROR',E
