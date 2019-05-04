def algorithm():
    import currentprice,smtplib
    pricedetail = currentprice.current_price()
    lp1 = pricedetail[0]    #when stock buy
    dt1 = pricedetail[1]    #date when you buy
    cp1 = pricedetail[2]    #current price
    stockname = pricedetail[3]
    diff = float(cp1) - lp1
    if diff>=0:
        c= 'Profit, Buy more Shares!!!'
    else:
        c= 'Loss, sell immediately...'
    #---------------------------------------------------------------------------------------------#
    s= smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.login('kunaljain8527@gmail.com','kuttabhaiya')
    message = 'Hello Sir\nYour Stock is {}\nPrevious Price ={}\nCurrent Price={}\nYour stock is in {}'.format(stockname,lp1,cp1,c)
    emailid = pricedetail[4] #email sent
    s.sendmail('kunaljain8527@gmail.com',emailid,message)
    s.close()
    return
