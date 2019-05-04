def insert():
    import sqlite3 as sq,requests,re,sys,datetime
    clientid = input('enter Client Id')
    name = raw_input('enter Name')
    address = raw_input('enter Address')
    phone = input('enter phone')
    stock_name = raw_input('enter Stock Symbol')
    email = raw_input('enter Email')
    date = datetime.date.today()


    baseurl = r'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='
    url = baseurl+stock_name
    response = requests.get(url)
    if response.status_code != 200:
        sys.exit(1)
    else:
        content = response.content.split('\n')
        for line in content:
            match = re.search('^{"tradedDate":.*"lastPrice":"(.*)"}]',line)
            if match:
                lastprice = match.group(1)
    try:
        with sq.connect('stockmarket') as db:
            cursor = db.cursor()
            cursor.execute('''Insert into buyers values(:clientid,:name,:address,:phone,:stock_name,:email,:lastprice,:date)''',{'clientid':clientid,
                                                                                                           'name':name,
                                                                                                           'address':address,
                                                                                                           'phone':phone,
                                                                                                           'stock_name':stock_name,
                                                                                                           'email':email,
                                                                                                           'lastprice':lastprice,
                                                                                                           'date':date})
            db.commit()
    except Exception as E:
        print 'ERROR',E
    return 'Data enter successfully'
