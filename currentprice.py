def current_price():
    import fetching_specific_data as fsd,requests,re,sys
    fetchdata = fsd.fetching()
    lp = fetchdata[0]
    dt = fetchdata[1]
    stockname = fetchdata[2]
    email = fetchdata[3]
    baseurl = r'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='
    url = baseurl+stockname
    response = requests.get(url)
    if response.status_code != 200:
        sys.exit(1)
    else:
        content = response.content.split('\n')
        for line in content:
            match = re.search('^{"tradedDate":.*"lastPrice":"(.*)"}]',line)
            if match:
                cur_price =  match.group(1)
    return  lp,dt,cur_price,stockname,email
